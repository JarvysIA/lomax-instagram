"""Reels do lote 5 com as vozes/trilhas do plano pago da ElevenLabs (v2).
A narração nova fica no ritmo natural (sem acelerar). As pausas longas são encurtadas,
as legendas passam a usar os tempos reais da voz nova e as animações são "esticadas"
(time-warp por trecho) para cada cena continuar casando com a frase que a acompanha.
Uso: python3 remix.py r1|r2|r3 [audio|render|encode|all]
"""
import json, re, subprocess, sys, os, importlib
sys.path.insert(0, "/home/claude/l5")
from mix import mix
import reel_lib

NEW = "/home/claude/l5/audio/new/"
REELS = "/home/claude/l5/reels/"
PARTS = NEW + "parts"
SR = 44100
MAXGAP = 0.38   # pausa máxima entre frases (a não ser que a antiga fosse maior)


def words_of(name):
    out, inside = [], False
    for x in json.load(open(NEW + name + "_words.json"))["words"]:
        if x["type"] != "word":
            continue
        t = x["text"]
        if t.startswith("["):
            inside = True
        if not inside:
            out.append(x)
        if t.endswith("]"):
            inside = False
    return out


def phrases(caps, words, voice, offset_old):
    """Agrupa as palavras novas pelas frases da legenda antiga."""
    i, res = 0, []
    for a, b, txt in caps:
        n = len(txt.split()); ws = words[i:i + n]; i += n
        res.append(dict(old_a=offset_old + a, old_b=offset_old + b, txt=txt, s=ws[0]["start"], e=ws[-1]["end"],
                        voice=voice))
    assert i == len(words), (voice, i, len(words))
    return res


def place(ph, first_start_new):
    """Define onde cada frase entra na linha do tempo nova."""
    t = first_start_new
    for k, p in enumerate(ph):
        if k:
            q = ph[k - 1]
            old_gap = p["old_a"] - q["old_b"]
            nat = p["s"] - q["e"] if p["voice"] == q["voice"] else old_gap
            gap = min(nat, max(old_gap, MAXGAP)) if p["voice"] == q["voice"] else old_gap
            t = q["new_b"] + max(gap, 0.08)
        p["new_a"] = t
        p["new_b"] = t + (p["e"] - p["s"])
    return ph


def cut_parts(ph, tag):
    os.makedirs(PARTS, exist_ok=True)
    out = []
    for k, p in enumerate(ph):
        prev_e = ph[k - 1]["e"] if k and ph[k - 1]["voice"] == p["voice"] else 0.0
        nxt_s = ph[k + 1]["s"] if k + 1 < len(ph) and ph[k + 1]["voice"] == p["voice"] else p["e"] + 0.6
        s = max(p["s"] - 0.08, (prev_e + p["s"]) / 2)
        e = min(p["e"] + 0.18, (p["e"] + nxt_s) / 2)
        d = e - s
        f = f"{PARTS}/{tag}_{k:02d}.wav"
        filt = f"atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={max(0, d - 0.05):.3f}:d=0.05,aresample={SR}"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", p["voice"], "-af", filt, "-ac", "1", f], check=True)
        out.append((f, p["new_a"] - (p["s"] - s)))
    return out


def build_voice(parts, duration, out):
    inputs, fl, lab = [], [], []
    for j, (f, st) in enumerate(parts):
        inputs += ["-i", f]; ms = int(round(st * 1000))
        fl.append(f"[{j}:a]adelay={ms}|{ms}[p{j}]"); lab.append(f"[p{j}]")
    fl.append(f"{''.join(lab)}amix=inputs={len(lab)}:normalize=0,apad=whole_dur={duration},atrim=0:{duration}[o]")
    subprocess.run(["ffmpeg", "-y", "-v", "error"] + inputs + ["-filter_complex", ";".join(fl), "-map", "[o]", "-ac", "1", out], check=True)


def anchors(ph, old_dur, extra=()):
    """Pares (novo, antigo) para o time-warp. extra: pontos antigos fixos com deslocamento herdado."""
    A = [(0.0, 0.0)]
    for p in ph:
        A.append((p["new_a"], p["old_a"]))
    last = ph[-1]
    new_dur = last["new_b"] + (old_dur - last["old_b"])
    A.append((new_dur, old_dur))
    A = sorted(set(A))
    return A, round(new_dur, 2)


def to_new(A, t_old):
    for (n0, o0), (n1, o1) in zip(A, A[1:]):
        if o0 <= t_old <= o1:
            return n0 + (t_old - o0) * (n1 - n0) / (o1 - o0) if o1 > o0 else n0
    return A[-1][0] + (t_old - A[-1][1])


SFX = {
    "r1": [("click", 0.6, .30), ("shutter", 1.6, .45), ("off", 3.0, .40), ("ping", 4.5, .35), ("ping", 5.0, .35),
           ("ping", 7.15, .35), ("whoosh", 8.7, .30), ("ping", 10.1, .35), ("whoosh", 11.25, .30), ("click", 13.3, .28),
           ("click", 14.2, .28), ("whoosh", 15.5, .30), ("whoosh", 18.0, .30), ("chime", 19.3, .45)],
    "r2": [("ping", 5.02, .35), ("click", 7.2, .25), ("whoosh", 10.35, .28), ("ping", 10.45, .35), ("ping", 12.2, .35),
           ("ping", 14.1, .35), ("whoosh", 16.6, .28), ("off", 17.9, .40), ("whoosh", 20.4, .30), ("ping", 26.3, .35),
           ("click", 27.5, .25), ("ping", 30.8, .35), ("whoosh", 31.0, .25), ("whoosh", 33.0, .25), ("ping", 34.9, .35),
           ("ping", 36.55, .35), ("whoosh", 36.7, .25), ("click", 37.0, .25), ("chime", 38.2, .45)],
    "r3": [("ping", 1.5, .35), ("whoosh", 4.0, .28), ("click", 5.15, .28), ("click", 5.95, .28), ("click", 7.1, .28),
           ("whoosh", 9.5, .30), ("off", 9.9, .40), ("whoosh", 11.15, .30), ("click", 13.75, .25), ("click", 14.0, .25),
           ("click", 14.6, .25), ("click", 15.4, .25), ("ping", 16.5, .35), ("whoosh", 17.7, .28), ("whoosh", 18.5, .25),
           ("ping", 19.7, .35), ("whoosh", 21.05, .28), ("click", 21.3, .22), ("click", 21.6, .22), ("click", 21.9, .22),
           ("click", 22.2, .22), ("chime", 23.05, .45)],
}


def make_mus2x(switch_at, dur):
    """Trilha da R2: melancólica até a 'volta a fita' e animada depois, com laço de compassos até o fim."""
    src = NEW + "mus2.mp3"; out = NEW + "mus2x.wav"
    jump, bar = 24.284, 2.857
    a0 = jump - switch_at
    loop_s = jump + bar
    pieces = [(a0, jump + 3 * bar)]
    total = pieces[0][1] - pieces[0][0]
    tail = 36.0 - loop_s
    while total + tail < dur + 0.5:
        pieces.append((loop_s, jump + 3 * bar)); total += 2 * bar
    pieces.append((loop_s, 36.0))
    fl, lab = [], []
    for j, (s, e) in enumerate(pieces):
        fl.append(f"[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,aresample={SR}[m{j}]"); lab.append(f"[m{j}]")
    fl.append(f"{''.join(lab)}concat=n={len(lab)}:v=0:a=1[o]")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-filter_complex", ";".join(fl), "-map", "[o]", out], check=True)
    return out


def plan(r):
    mod = importlib.import_module(r)
    old_dur = {"r1": 24.8, "r2": 43.8, "r3": 28.4}[r]
    if r == "r2":
        ph = phrases(mod.capsA, words_of("r2a"), NEW + "r2a_voz.mp3", mod.A0) + \
             phrases(mod.capsB, words_of("r2b"), NEW + "r2b_voz.mp3", mod.B0)
    else:
        ph = phrases(mod.caps, words_of(r), NEW + f"{r}_voz.mp3", 0.0)
    place(ph, ph[0]["old_a"])
    A, new_dur = anchors(ph, old_dur)
    return mod, ph, A, new_dur, old_dur


def do(r, steps):
    mod, ph, A, new_dur, old_dur = plan(r)
    print(f"{r}: duração {old_dur}s -> {new_dur}s")
    newcaps = [(round(p["new_a"], 2), round(p["new_b"] + 0.1, 2), p["txt"]) for p in ph]
    if "audio" in steps:
        parts = cut_parts(ph, r)
        vo = NEW + f"{r}_aligned.wav"; build_voice(parts, new_dur, vo)
        sfx = [(n, round(to_new(A, t), 2), v) for n, t, v in SFX[r]]
        extra = []
        if r == "r2":
            music, ms, mv = make_mus2x(to_new(A, 20.4), new_dur), 0.0, 0.30
            extra = [(NEW + "sfx_rewind.mp3", round(to_new(A, 18.85), 2), 0.55)]
        else:
            music, mv = NEW + "mus1.mp3", 0.28
            ms = max(0.0, 20.5 - to_new(A, 18.0)) if r == "r1" else 0.0
        mix(REELS + f"{r}_audio_v2.wav", new_dur, [(vo, 0.0)], music, music_start=ms, music_vol=mv, sfx=sfx, extra=extra)
    if "render" in steps:
        old_js = "buildCaps(" + json.dumps(mod.caps) + ");"
        assert old_js in mod.script
        warp = "const WA=" + json.dumps([[round(n, 4), round(o, 4)] for n, o in A]) + ";" + \
               "function W(t){for(let i=0;i<WA.length-1;i++){const a=WA[i],b=WA[i+1];if(t>=a[0]&&t<=b[0])" \
               "return b[0]>a[0]?a[1]+(t-a[0])*(b[1]-a[1])/(b[0]-a[0]):a[1];}return WA[WA.length-1][1]+(t-WA[WA.length-1][0]);}"
        script = mod.script.replace(old_js, "buildCaps(" + json.dumps(newcaps) + ");" + warp)
        css = getattr(mod, "extra_css", "")
        page = reel_lib.html(mod.body, script, css) if css else reel_lib.html(mod.body, script)
        only = None
        if len(sys.argv) > 3:
            only = [int(float(x) * reel_lib.FPS) for x in sys.argv[3:]]
        fdir = reel_lib.render(f"l5_{r}v2", page, new_dur, only=only, expr="render(W({t:.4f})); caps({t:.4f})")
        print(fdir)
    if "encode" in steps:
        reel_lib.encode(f"l5_{r}v2", REELS + f"l5_{r}v2_frames", REELS + f"{r}_audio_v2.wav", REELS + f"l5_{r}v2.mp4")
        print(REELS + f"l5_{r}v2.mp4")
    return new_dur


if __name__ == "__main__":
    r = sys.argv[1]
    st = sys.argv[2] if len(sys.argv) > 2 else "all"
    steps = ["audio", "render", "encode"] if st == "all" else [st]
    do(r, steps)
