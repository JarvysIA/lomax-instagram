"""Edição do depoimento do Gustavo: cortes, punch-in, legendas, lower third, chips, logo, end card, trilha."""
import json, os, subprocess, sys
sys.path.insert(0, "/home/claude/l5")
from base import font_faces, ROOT

SRC = os.environ.get("SRC", "/home/claude/gus/in/bruto.mov")
OUT = "/home/claude/gus/out"; os.makedirs(OUT, exist_ok=True)
FPS = 30

# (inicio, fim, zoom) no tempo do bruto
SEGS = [
    (18.02, 19.24, 1.18),   # Todos eles travavam,
    (21.86, 23.80, 1.18),   # diferente do Lomax, que não trava.
    (1.10, 3.46, 1.00),     # Oi, meu nome é Gustavo, eu trabalho aqui na Star
    (3.98, 7.26, 1.08),     # e eu uso o CRM Lomax diariamente aqui na loja.
    (8.90, 11.30, 1.00),    # posso dizer que ele tá mais do que aprovado, porque
    (12.08, 17.22, 1.10),   # já usei vários CRMs aqui na loja durante anos e nenhum deles era realmente eficiente.
    (19.38, 21.22, 1.00),   # eram bem difíceis de se localizar,
    (21.86, 29.26, 1.12),   # diferente do Lomax, que não trava, ... no aplicativo.
    (30.58, 30.80, 1.00),   # eu
    (31.02, 35.20, 1.00),   # super recomendo ... pra sua empresa.
    (35.72, 38.78, 1.14),   # Você pode ter certeza ... com o Lomax.
]
END = 3.4  # end card

WORDS = json.load(open("/home/claude/gus/words.json"))

def build():
    # mapa de palavras para a nova linha do tempo
    t = 0.0; out_words = []; seg_bounds = []
    for (a, b, z) in SEGS:
        seg_bounds.append((t, t + (b - a), z))
        for w in WORDS:
            if w["start"] >= a - 0.02 and w["end"] <= b + 0.05:
                out_words.append({"text": w["text"], "start": t + (w["start"] - a), "end": t + (min(w["end"], b) - a)})
        f = f"{OUT}/seg{len(seg_bounds)-1:02d}.mp4"
        if os.path.exists(f):
            d = float(subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","stream=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
            seg_bounds[-1] = (seg_bounds[-1][0], seg_bounds[-1][0] + d, z)
            t += d
        else:
            t += b - a
    return out_words, seg_bounds, t

def cut_video(seg_bounds, total):
    parts = []
    for i, (a, b, z) in enumerate(SEGS):
        p = f"{OUT}/seg{i:02d}.mp4"
        cw = f"iw/{z}"; ch = f"ih/{z}"
        # recorta com zoom levemente acima do centro (rosto)
        vf = (f"hflip,crop={cw}:{ch}:(iw-{cw})/2:(ih-{ch})*0.42,scale=1080:1920:flags=lanczos,"
              f"unsharp=5:5:0.6:5:5:0.0,eq=contrast=1.06:saturation=1.08:brightness=-0.01,fps={FPS},format=yuv420p")
        af = "afade=t=in:d=0.012,areverse,afade=t=in:d=0.02,areverse"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a}", "-to", f"{b}", "-i", SRC,
                        "-vf", vf, "-af", af, "-c:v", "libx264", "-crf", "16", "-preset", "fast",
                        "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2", p], check=True)
        parts.append(p)
    # end card: último quadro congelado e desfocado
    last = parts[-1]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-sseof", "-0.05", "-i", last, "-frames:v", "1", f"{OUT}/last.png"], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", f"{END}", "-i", f"{OUT}/last.png",
                    "-f", "lavfi", "-t", f"{END}", "-i", "anullsrc=r=48000:cl=stereo",
                    "-vf", f"gblur=sigma=24,eq=brightness=-0.18,fps={FPS},format=yuv420p", "-c:v", "libx264", "-crf", "16",
                    "-c:a", "pcm_s16le", "-shortest", f"{OUT}/endcard.mp4"], check=True)
    parts.append(f"{OUT}/endcard.mp4")
    with open(f"{OUT}/list.txt", "w") as f:
        for p in parts: f.write(f"file '{p}'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/list.txt",
                    "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-c:a", "pcm_s16le", f"{OUT}/base.mov"], check=True)

CSS = font_faces() + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;background:transparent;overflow:hidden;font-family:'Barlow',sans-serif;color:#fff}
.abs{position:absolute}
#cap{position:absolute;left:60px;right:60px;top:1470px;text-align:center;font-weight:900;font-style:italic;font-size:74px;line-height:1.12;letter-spacing:-1px;
 text-shadow:0 4px 0 rgba(0,0,0,.35),0 0 24px rgba(0,0,0,.45)}
#cap span{display:inline-block;margin:0 8px;opacity:0;transform:translateY(14px) scale(.9)}
#cap span.on{opacity:1;transform:none}
#cap span.now{color:#fff;background:#0E8DFE;border-radius:14px;padding:0 12px;margin:0 2px;text-shadow:none}
#cap span.kw{color:#7fc4ff}
#hook{position:absolute;left:70px;right:70px;top:250px;text-align:center}
#hook .t{display:inline-block;background:#fff;color:#0A192C;font-weight:900;font-style:italic;font-size:62px;letter-spacing:-1px;padding:14px 30px 22px;border-radius:22px;box-shadow:0 18px 40px rgba(0,0,0,.35);line-height:1.05}
#hook .t b{color:#0E8DFE}
#lt{position:absolute;left:60px;top:1300px;display:flex;align-items:stretch;opacity:0}
#lt .bar{width:12px;background:#0E8DFE;border-radius:6px}
#lt .box{background:rgba(10,25,44,.86);padding:18px 28px 20px;border-radius:0 18px 18px 0;margin-left:0}
#lt .n{font-weight:900;font-style:italic;font-size:52px;letter-spacing:-.5px}
#lt .r{font-size:30px;font-weight:600;color:#cfe3ff;margin-top:2px}
#wm{position:absolute;right:50px;top:140px;opacity:0;background:rgba(10,25,44,.82);border-radius:14px;padding:12px 18px}
#wm img{height:36px;display:block}
#chips{position:absolute;left:60px;right:60px;top:300px;display:flex;flex-wrap:wrap;gap:16px;justify-content:center}
.chip{background:rgba(255,255,255,.95);color:#0A192C;font-weight:800;font-size:36px;padding:14px 26px;border-radius:999px;box-shadow:0 10px 26px rgba(0,0,0,.3);opacity:0}
.chip i{font-style:normal;color:#0E8DFE;margin-right:8px}
#end{position:absolute;inset:0;background:rgba(10,25,44,.55);display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0}
#end img{height:110px}
#end .q{font-weight:900;font-style:italic;font-size:76px;text-align:center;line-height:1.05;margin-top:60px;letter-spacing:-1.5px}
#end .q b{color:#0E8DFE}
#end .cta{margin-top:60px;background:#0E8DFE;border-radius:999px;padding:30px 56px;font-weight:800;font-size:46px}
#end .lk{margin-top:30px;font-size:40px;font-weight:700;color:#cfe3ff}
#flash{position:absolute;inset:0;background:#fff;opacity:0}
"""

KEYWORDS = {"Lomax", "Lomax,", "Lomax.", "trava,", "travavam,", "intuitivo,", "aprovado,", "recomendo,", "fácil", "eficiente."}

def overlay_html(words, seg_bounds, total):
    logo = f"file://{ROOT}/logo_on_dark.png"
    # agrupa palavras em frases de até ~3 palavras / 18 caracteres
    groups = []; cur = []
    for w in words:
        cur.append(w)
        txt = " ".join(x["text"] for x in cur)
        if len(cur) >= 3 or len(txt) > 17 or w["text"].endswith((".", ",", "?")):
            groups.append(cur); cur = []
    if cur: groups.append(cur)
    G = [{"a": g[0]["start"], "b": g[-1]["end"], "w": [[x["start"], x["text"], x["text"] in KEYWORDS] for x in g]} for g in groups]
    t_intro = seg_bounds[2][0]          # início do "Oi, meu nome é Gustavo"
    t_mod = [w["start"] for w in words if w["text"].startswith("modalidades")][0]
    body = f"""
<div id="hook"><div class="t">Já usou vários CRMs<br>que <b>travavam?</b></div></div>
<div id="lt"><div class="bar"></div><div class="box"><div class="n">Gustavo</div><div class="r">Vendedor · Star Serviços Automotivos</div></div></div>
<div id="wm"><img src="{logo}"></div>
<div id="chips">
 <div class="chip" id="c0"><i>●</i>Funil por etapas</div><div class="chip" id="c1"><i>●</i>Retornos automáticos</div>
 <div class="chip" id="c2"><i>●</i>Agendamentos</div><div class="chip" id="c3"><i>●</i>Equipes</div></div>
<div id="cap"></div>
<div id="end"><img src="{logo}"><div class="q">Atendimento organizado.<br><b>Sem dor de cabeça.</b></div>
<div class="cta">Teste 30 dias grátis · sem cartão</div><div class="lk">🔗 Link na bio</div></div>
<div id="flash"></div>"""
    js = f"""
const G={json.dumps(G)}, TOTAL={total:.3f}, TI={t_intro:.3f}, TM={t_mod:.3f}, CUTS={json.dumps([s[0] for s in seg_bounds[1:]])};
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), p=(t,a,b)=>clamp((t-a)/(b-a)), eo=x=>1-Math.pow(1-x,3);
const back=x=>{{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)}};
const $=id=>document.getElementById(id);
let last=-1;
function render(t){{
  // hook (abertura fria)
  const h=$('hook'); const hi=eo(p(t,0.05,0.35)), ho=1-p(t,TI-0.25,TI);
  h.style.opacity=Math.min(hi,ho); h.style.transform=`translateY(${{(1-hi)*-40}}px) rotate(-1.5deg)`;
  // flash branco no corte da abertura para a apresentação
  $('flash').style.opacity = Math.max(0, 0.55*(1-p(t,TI,TI+0.18))*(t>=TI?1:0));
  // lower third
  const li=eo(p(t,TI+0.3,TI+0.7)), lo=1-p(t,TI+4.6,TI+5.0);
  $('lt').style.opacity=Math.min(li,lo); $('lt').style.transform=`translateX(${{(1-li)*-80}}px)`;
  // marca d'água depois da abertura
  $('wm').style.opacity = 0.9*p(t,TI,TI+0.4)*(1-p(t,TOTAL-{END}-0.2,TOTAL-{END}));
  // chips de modalidades
  for(let i=0;i<4;i++){{ const c=$('c'+i); const x=p(t,TM+0.08*i-0.15,TM+0.08*i+0.2); const o=1-p(t,TM+2.4,TM+2.8);
     c.style.opacity=Math.min(x,o); c.style.transform=`scale(${{0.6+0.4*back(x)}})`; }}
  // legenda
  const cap=$('cap'); let idx=-1;
  for(let i=0;i<G.length;i++){{ if(t>=G[i].a-0.06 && t<(G[i+1]?G[i+1].a-0.06:G[i].b+0.5)) idx=i; }}
  if(t>TOTAL-{END}) idx=-1;
  if(idx!==last){{ cap.innerHTML = idx<0?'':G[idx].w.map(w=>`<span data-k="${{w[2]?1:0}}">${{w[1]}}</span>`).join(' '); last=idx; }}
  if(idx>=0){{ const sp=cap.querySelectorAll('span'); let cur=-1; G[idx].w.forEach((w,i)=>{{if(t>=w[0]-0.03)cur=i}});
    sp.forEach((s,i)=>{{ const on=i<=cur; s.className=(on?'on':'')+(i===cur?' now':'')+(on&&i!==cur&&s.dataset.k==='1'?' kw':'');
      s.style.transition='none'; if(on){{const x=eo(p(t,G[idx].w[i][0]-0.03,G[idx].w[i][0]+0.09)); s.style.opacity=x; s.style.transform=`translateY(${{(1-x)*14}}px) scale(${{0.9+0.1*x}})`;}} else {{s.style.opacity=0}} }}); }}
  // end card
  const e=eo(p(t,TOTAL-{END},TOTAL-{END}+0.45)); $('end').style.opacity=e; $('end').style.transform=`translateY(${{(1-e)*40}}px)`;
}}"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}<script>{js}</script></body></html>"

def render_overlay(html, total, only=None):
    from playwright.sync_api import sync_playwright
    fdir = f"{OUT}/ov"; os.makedirs(fdir, exist_ok=True)
    for f in os.listdir(fdir): os.remove(os.path.join(fdir, f))
    path = f"{OUT}/overlay.html"; open(path, "w").write(html)
    n = int(total * FPS)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto("file://" + path); pg.wait_for_timeout(400); pg.evaluate("document.fonts.ready")
        for i in (only if only is not None else range(n)):
            pg.evaluate(f"render({i/FPS:.4f})")
            pg.screenshot(path=f"{fdir}/o{i:05d}.png", omit_background=True)
        b.close()
    return fdir

if __name__ == "__main__":
    words, bounds, speech = build()
    total = speech + END
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("all", "cut"):
        cut_video(bounds, total)
    html = overlay_html(words, bounds, total)
    if mode == "preview":
        ts = [float(x) for x in sys.argv[2:]]
        render_overlay(html, total, [int(t * FPS) for t in ts])
    elif mode in ("all", "ov"):
        render_overlay(html, total)
    json.dump({"total": total, "speech": speech, "bounds": bounds}, open(f"{OUT}/meta.json", "w"))
    print(total, speech)
