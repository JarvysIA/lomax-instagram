"""Mistura voz(es) + trilha (com ducking) + efeitos, normaliza para -14 LUFS."""
import subprocess

SFX = "/home/claude/l5/sfx/"
AUD = "/home/claude/l5/audio/"

def mix(out, duration, voices, music, music_start=0.0, music_vol=0.28, sfx=(), extra=()):
    """voices: [(arquivo, inicio)], sfx: [(nome, inicio, volume)], extra: [(arquivo, inicio, volume)]"""
    inputs, filters, labels = [], [], []
    i = 0
    vlabels = []
    for f, st in voices:
        inputs += ["-i", AUD + f]
        filters.append(f"[{i}:a]aresample=44100,adelay={int(st*1000)}|{int(st*1000)},volume=1.0[v{i}]")
        vlabels.append(f"[v{i}]"); i += 1
    filters.append(f"{''.join(vlabels)}amix=inputs={len(vlabels)}:normalize=0[voice]")
    filters.append(f"[voice]apad=whole_dur={duration},asplit=2[vo][sc]")
    inputs += ["-i", AUD + music]
    filters.append(f"[{i}:a]aresample=44100,atrim=start={music_start},asetpts=PTS-STARTPTS,volume={music_vol},"
                   f"afade=t=in:d=0.4,afade=t=out:st={duration-1.4}:d=1.4[m0]")
    filters.append("[m0][sc]sidechaincompress=threshold=0.04:ratio=6:attack=20:release=350[mus]")
    i += 1
    fx = []
    for name, st, vol in sfx:
        inputs += ["-i", SFX + name + ".wav"]
        filters.append(f"[{i}:a]aresample=44100,volume={vol},adelay={int(st*1000)}|{int(st*1000)}[s{i}]")
        fx.append(f"[s{i}]"); i += 1
    for f, st, vol in extra:
        inputs += ["-i", f]
        filters.append(f"[{i}:a]aresample=44100,volume={vol},adelay={int(st*1000)}|{int(st*1000)}[s{i}]")
        fx.append(f"[s{i}]"); i += 1
    allin = ["[vo]", "[mus]"] + fx
    filters.append(f"{''.join(allin)}amix=inputs={len(allin)}:normalize=0,atrim=0:{duration},"
                   f"loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[out]")
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"] + inputs + [
        "-filter_complex", ";".join(filters), "-map", "[out]", "-ac", "2", "-c:a", "pcm_s16le", out]
    subprocess.run(cmd, check=True)
