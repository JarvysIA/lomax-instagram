"""Reels do lote 12 (13/11), série "Reclamações": a frase do cliente na tela desde o 1º quadro, a resposta do Lomax
só com recurso confirmado e fechamento "link na bio". 15 a 18 s.
R1 suporte sumiu (Nayara) · R2 implantação sem fim (Jhony) · R3 promessa de venda (Nayara).
Uso: python3 reels12.py r1|r2|r3 [render|audio|encode|all] [t1 t2 ... só esses quadros]
"""
import sys, json, os
sys.path.insert(0, "/home/claude/l7"); sys.path.insert(0, "/home/claude/l5")
import reels7
from reels7 import EXTRA_CSS, CAPJS, LOGO
from reel_lib import html, render, encode, FPS
from mix import mix

reels7.A = "/home/claude/l12/audio/"
OUT = "/home/claude/l12/reels/"

reels7.LAYOUT["r1"] = ["O suporte sumiu.", "Já passou por isso?", "No Lomax, o suporte é grátis.", "Tira-dúvida pelo WhatsApp",
    "e ajuda por vídeo,", "com hora marcada.", "Durante o teste e depois,", "sem pagar nada a mais.", "Lomax CRM.",
    "Teste trinta dias grátis."]
reels7.LAYOUT["r2"] = ["Três meses e a implantação", "não terminou.", "No Lomax, é uma chamada de vídeo.",
    "A gente conecta o seu número", "e monta as equipes e o funil", "junto com você.", "Sem taxa de implantação.",
    "Lomax CRM.", "Teste trinta dias grátis."]
reels7.LAYOUT["r3"] = ["Prometeram tudo na venda", "e não entregaram.", "No Lomax, você testa antes de pagar.",
    "São trinta dias grátis,", "sem cartão,", "com a sua equipe e o seu número.", "Se servir, você continua.",
    "Se não servir, é só não continuar.", "Lomax CRM."]

CSS = EXTRA_CSS + """
.rev{background:#fff;color:#0A192C;border-radius:30px;padding:40px 44px;box-shadow:0 24px 60px rgba(0,0,0,.45)}
.rev .who{display:flex;align-items:center;gap:20px}
.rev .av2{width:76px;height:76px;border-radius:50%;background:#d9e2ee;display:flex;align-items:center;justify-content:center;font-size:40px}
.rev .stars{font-size:40px;letter-spacing:4px;color:#f5a623}
.rev .stars i{color:#d0d7e2;font-style:normal}
.rev .txt{font-size:64px;font-weight:900;font-style:italic;line-height:1.08;margin-top:26px;letter-spacing:-1px}
.lab{display:inline-block;background:#ff4d5e;color:#fff;border-radius:999px;padding:12px 28px;font-weight:800;font-size:32px;letter-spacing:1px}
.ck{display:flex;align-items:center;gap:24px;background:#16253a;border-radius:24px;padding:26px 30px;margin-bottom:22px}
.ck .i{flex:none;width:70px;height:70px;border-radius:18px;background:#123a2a;color:#4fe08f;font-size:44px;font-weight:900;display:flex;align-items:center;justify-content:center}
.ck p{font-size:48px;font-weight:800;line-height:1.1}
.big{font-size:180px;font-weight:900;font-style:italic;color:#0E8DFE;line-height:1;letter-spacing:-4px}
"""

END = lambda line1, pill: f"""
<div id="end" class="abs" style="left:0;right:0;top:250px;text-align:center;opacity:0">
  <img src="{LOGO}" style="height:118px">
  <div class="h" style="font-size:88px;margin-top:80px">{line1}</div>
  <div class="h" style="font-size:88px;margin-top:20px"><span class="pill">{pill}</span></div>
  <div style="margin-top:60px;font-size:40px;font-weight:700;color:#cfe3ff">Sem fidelidade · sem taxa de implantação</div>
  <div id="cta" style="display:inline-block;margin-top:40px;background:#0E8DFE;border-radius:999px;padding:30px 56px;font-weight:800;font-size:46px">Teste 30 dias grátis · sem cartão</div>
  <div style="margin-top:34px;font-size:40px;font-weight:700;color:#cfe3ff">🔗 Link na bio</div>
</div>"""

REV = lambda quote, extra="": f"""
<div id="q" class="abs" style="left:80px;right:80px;top:400px">
  <div style="text-align:center;margin-bottom:34px"><span class="lab">RECLAMAÇÃO COMUM</span></div>
  <div class="rev"><div class="who"><div class="av2">🙁</div><div><div style="font-size:30px;font-weight:800">Cliente de um sistema de WhatsApp</div>
  <div class="stars">★<i>★★★★</i></div></div></div><div class="txt">“{quote}”</div>{extra}</div>
</div>"""

NOTE = '<div class="disc" id="disc" style="top:1560px">Frase resumida de avaliações públicas.</div>'


def ck(id_, t):
    return f'<div id="{id_}" class="ck" style="opacity:0"><div class="i">✓</div><p>{t}</p></div>'


def r1():
    body = '<div class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C)"></div>' + REV(
        "O suporte sumiu.", '<div id="q2" style="margin-top:26px;font-size:40px;font-weight:700;color:#c0283a;opacity:0">Já passou por isso? 👀</div>') + f"""
<div id="a" class="abs" style="left:80px;right:80px;top:330px;opacity:0">
  <div class="h" style="font-size:96px;margin-bottom:46px">No Lomax:</div>
  {ck("k1", "Suporte grátis.")}{ck("k2", "Tira-dúvida pelo WhatsApp.")}{ck("k3", "Ajuda por vídeo, com hora marcada.")}
  <div id="k4" style="margin-top:30px;opacity:0"><span class="lab" style="background:#0E8DFE">Durante o teste</span> <span id="k5" class="lab" style="background:#0E8DFE;opacity:0">E depois</span> <span id="k6" class="lab" style="background:#0E8DFE;opacity:0">Sem pagar a mais</span></div>
</div>""" + NOTE + END("Suporte de verdade.", "E de graça.")
    script = r"""
function render(t){
  S('q',{opacity:1-p(t,2.3,2.55),transform:`scale(${1+0.03*Math.sin(Math.min(t,2)*3)})`});
  pop('q2',t,0.88,.3,.6);
  S('a',{opacity:p(t,2.4,2.65)*(1-p(t,12.6,12.85))});
  slideUp('k1',t,4.19,.35,50); slideUp('k2',t,4.84,.35,50); slideUp('k3',t,6.96,.35,50);
  pop('k4',t,9.36,.3,.6); pop('k5',t,10.4,.3,.6); pop('k6',t,11.04,.3,.6);
  const e=eo(p(t,12.8,13.2)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>14.3?1+0.03*Math.sin((t-14.3)*5):1})`});
  S('disc',{opacity:t<2.45?1:0});
}
"""
    sfx = [("whoosh", 2.4, .25), ("click", 4.19, .22), ("click", 4.84, .22), ("click", 6.96, .22), ("click", 9.36, .2),
           ("click", 10.4, .2), ("click", 11.04, .2), ("whoosh", 12.8, .3), ("chime", 13.3, .45)]
    return body, script, 17.0, sfx, "/home/claude/l5/audio/new/gus_music.mp3", 0.0, 0.22


def r2():
    body = '<div class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C)"></div>' + REV(
        "Três meses e a implantação não terminou.", '<div id="q2" style="margin-top:26px;font-size:40px;font-weight:700;color:#c0283a;opacity:0">⏳ E nada de começar...</div>') + f"""
<div id="a1" class="abs" style="left:0;right:0;top:360px;text-align:center;opacity:0">
  <div class="h" style="font-size:88px">No Lomax, é uma</div>
  <div class="h" style="font-size:112px;margin-top:24px"><span class="pill">chamada de vídeo.</span></div>
  <div id="cam" style="font-size:240px;margin-top:50px;opacity:0">📹</div>
</div>
<div id="a2" class="abs" style="left:80px;right:80px;top:340px;opacity:0">
  <div class="h" style="font-size:80px;margin-bottom:46px">Junto com você:</div>
  {ck("k1", "Conecta o seu número.")}{ck("k2", "Monta as equipes.")}{ck("k3", "Monta o funil.")}
</div>
<div id="pr" class="abs" style="left:0;right:0;top:470px;text-align:center;opacity:0">
  <div style="font-size:60px;font-weight:800">Taxa de implantação:</div>
  <div class="big" style="margin-top:30px">R$ 0</div>
</div>""" + NOTE + END("Uma chamada.", "E pronto.")
    script = r"""
function render(t){
  S('q',{opacity:1-p(t,2.9,3.15),transform:`scale(${1+0.03*Math.sin(Math.min(t,2)*3)})`});
  pop('q2',t,1.2,.3,.6);
  S('a1',{opacity:p(t,3.0,3.25)*(1-p(t,5.0,5.2))});
  pop('cam',t,4.0,.35,.5);
  S('a2',{opacity:p(t,5.1,5.35)*(1-p(t,9.15,9.35))});
  slideUp('k1',t,5.6,.35,50); slideUp('k2',t,7.24,.35,50); slideUp('k3',t,7.76,.35,50);
  const pr=eo(p(t,9.3,9.6)); S('pr',{opacity:pr*(1-p(t,10.85,11.05)),transform:`scale(${0.8+0.2*pr})`});
  const e=eo(p(t,11.0,11.4)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>12.6?1+0.03*Math.sin((t-12.6)*5):1})`});
  S('disc',{opacity:t<3.05?1:0});
}
"""
    sfx = [("whoosh", 3.0, .25), ("whoosh", 4.0, .2), ("click", 5.6, .22), ("click", 7.24, .22), ("click", 7.76, .22),
           ("ping", 9.36, .35), ("whoosh", 11.0, .3), ("chime", 11.5, .45)]
    return body, script, 15.0, sfx, "/home/claude/l5/audio/new/mus1.mp3", 0.0, 0.22


def r3():
    body = '<div class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C)"></div>' + REV(
        "Prometeram tudo na venda e não entregaram.", '<div id="q2" style="margin-top:26px;font-size:40px;font-weight:700;color:#c0283a;opacity:0">🤝 Na reunião era lindo...</div>') + f"""
<div id="a1" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0">
  <div class="h" style="font-size:88px">No Lomax, você</div>
  <div class="h" style="font-size:112px;margin-top:24px"><span class="pill">testa antes</span></div>
  <div class="h" style="font-size:112px;margin-top:20px"><span class="pill">de pagar.</span></div>
</div>
<div id="a2" class="abs" style="left:80px;right:80px;top:360px;opacity:0">
  <div class="h" style="font-size:80px;margin-bottom:46px">O teste:</div>
  {ck("k1", "30 dias grátis.")}{ck("k2", "Sem cartão.")}{ck("k3", "Sua equipe, seu número.")}
</div>
<div id="a3" class="abs" style="left:80px;right:80px;top:520px;opacity:0">
  <div id="s1" class="h" style="font-size:84px;opacity:0">Serviu? <span class="blue">Continua.</span></div>
  <div id="s2" class="h" style="font-size:84px;margin-top:50px;opacity:0">Não serviu? <span class="blue">Não continua.</span></div>
</div>""" + NOTE + END("Testa antes.", "Decide depois.")
    script = r"""
function render(t){
  S('q',{opacity:1-p(t,3.05,3.3),transform:`scale(${1+0.03*Math.sin(Math.min(t,2)*3)})`});
  pop('q2',t,1.2,.3,.6);
  S('a1',{opacity:p(t,3.15,3.4)*(1-p(t,5.9,6.1))});
  S('a2',{opacity:p(t,6.0,6.25)*(1-p(t,10.7,10.9))});
  slideUp('k1',t,6.08,.35,50); slideUp('k2',t,7.76,.35,50); slideUp('k3',t,8.64,.35,50);
  S('a3',{opacity:p(t,10.8,11.0)*(1-p(t,14.95,15.15))});
  slideUp('s1',t,10.88,.35,40); slideUp('s2',t,12.72,.35,40);
  const e=eo(p(t,15.1,15.5)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>16.5?1+0.03*Math.sin((t-16.5)*5):1})`});
  S('disc',{opacity:t<3.2?1:0});
}
"""
    sfx = [("whoosh", 3.15, .25), ("whoosh", 6.0, .25), ("click", 6.08, .22), ("click", 7.76, .22), ("click", 8.64, .22),
           ("ping", 10.88, .3), ("ping", 12.72, .3), ("whoosh", 15.1, .3), ("chime", 15.6, .45)]
    return body, script, 18.0, sfx, "/home/claude/l5/audio/new/gus_music.mp3", 0.0, 0.22


def main():
    r = sys.argv[1]
    st = sys.argv[2] if len(sys.argv) > 2 else "all"
    body, script, dur, sfx, music, ms, mv = {"r1": r1, "r2": r2, "r3": r3}[r]()
    caps = reels7.layout(r, reels7.words(r))
    os.makedirs(OUT, exist_ok=True)
    page = html(body, CAPJS + "setCaps(" + json.dumps(caps) + ");" + script, CSS)
    steps = ["audio", "render", "encode"] if st == "all" else [st]
    if "audio" in steps:
        mix(OUT + f"l12_{r}_audio.wav", dur, [(reels7.A + f"{r}_voz.mp3", 0.0)], music, music_start=ms, music_vol=mv, sfx=sfx)
    if "render" in steps:
        only = [int(float(x) * FPS) for x in sys.argv[3:]] or None
        print(render(f"l12_{r}", page, dur, outdir=OUT, only=only))
    if "encode" in steps:
        encode(f"l12_{r}", OUT + f"l12_{r}_frames", OUT + f"l12_{r}_audio.wav", OUT + f"l12_{r}.mp4")
        print(OUT + f"l12_{r}.mp4")


if __name__ == "__main__":
    main()
