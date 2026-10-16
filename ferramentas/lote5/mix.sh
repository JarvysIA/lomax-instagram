#!/bin/bash
set -e
cd /home/claude/gus
TOTAL=$(python3 -c "import json;print(json.load(open('out/meta.json'))['total'])")
TI=$(python3 -c "import json;print(json.load(open('out/meta.json'))['bounds'][2][0])")
SP=$(python3 -c "import json;print(json.load(open('out/meta.json'))['speech'])")
FO=$(python3 -c "print($TOTAL-1.6)")
TIMS=$(python3 -c "print(int(($TI-0.25)*1000))")
SPMS=$(python3 -c "print(int(($SP-0.1)*1000))")
ffmpeg -y -loglevel error -i out/base.mov -i music.mp3 \
  -i /home/claude/l5/sfx/whoosh.wav -i /home/claude/l5/sfx/chime.wav -filter_complex "
[0:a]aresample=48000,highpass=f=85,afftdn=nr=8:nf=-42,equalizer=f=3200:t=q:w=1.2:g=2,equalizer=f=250:t=q:w=1:g=-2,
acompressor=threshold=0.09:ratio=3:attack=8:release=120:makeup=1.6,alimiter=limit=0.9,asplit=2[v][sc];
[1:a]aresample=48000,volume=0.20,afade=t=in:d=0.6,afade=t=out:st=$FO:d=1.6,atrim=0:$TOTAL[m0];
[m0][sc]sidechaincompress=threshold=0.03:ratio=5:attack=25:release=400[m1];
[2:a]aresample=48000,volume=0.35,adelay=${TIMS}|${TIMS}[w];
[3:a]aresample=48000,volume=0.45,adelay=${SPMS}|${SPMS}[c];
[v][m1][w][c]amix=inputs=4:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=9,aresample=48000[out]" \
  -map "[out]" -ac 2 -c:a pcm_s16le out/mix.wav
ffmpeg -hide_banner -i out/mix.wav -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak):"
