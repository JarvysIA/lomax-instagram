"""Reels do lote 11 (06/11), série "Reclamações": a frase do cliente na tela desde o 1º quadro, a resposta do Lomax
só com recurso confirmado e fechamento "link na bio". 15 a 18 s.
R1 cancelamento (Jhony) · R2 cobrança surpresa (Nayara) · R3 computador ligado (Jhony).
Uso: python3 reels11.py r1|r2|r3 [render|audio|encode|all] [t1 t2 ... só esses quadros]
"""
import sys, json, os
sys.path.insert(0, "/home/claude/l7"); sys.path.insert(0, "/home/claude/l5")
import reels7
from reels7 import EXTRA_CSS, CAPJS, LOGO
from reel_lib import html, render, encode, FPS
from mix import mix

reels7.A = "/home/claude/l11/audio/"
OUT = "/home/claude/l11/reels/"

reels7.LAYOUT["r1"] = ["Quero cancelar e estão me enrolando.", "Já ouviu isso de algum sistema?", "No Lomax não tem fidelidade.",
    "Você paga mês a mês.", "Não quer mais?", "É só não renovar.", "Sem multa, sem cartão,", "sem burocracia.", "Lomax CRM.",
    "Teste trinta dias grátis."]
reels7.LAYOUT["r2"] = ["A cobrança veio maior", "do que o combinado.", "No Lomax, não tem", "cobrança por mensagem.",
    "Não tem taxa de implantação.", "E o suporte é grátis.", "É noventa e nove e noventa", "por mês, com dois usuários.",
    "Ponto.", "Lomax CRM.", "Teste trinta dias grátis."]
reels7.LAYOUT["r3"] = ["Tive que deixar o computador ligado", "o fim de semana inteiro.", "Com o Lomax, não precisa.",
    "Ele roda na nuvem.", "O retorno pra quem sumiu", "e a confirmação de horário", "saem sozinhos,", "com o computador desligado.",
    "Lomax CRM.", "Teste trinta dias grátis."]

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
        "Quero cancelar e estão me enrolando.", '<div id="q2" style="margin-top:26px;font-size:40px;font-weight:700;color:#c0283a;opacity:0">Já ouviu isso? 👀</div>') + f"""
<div id="a" class="abs" style="left:80px;right:80px;top:360px;opacity:0">
  <div class="h" style="font-size:96px;margin-bottom:46px">No Lomax:</div>
  {ck("k1", "Sem fidelidade.")}{ck("k2", "Paga mês a mês.")}{ck("k3", "Não quer mais? Não renova.")}
  <div id="k4" style="margin-top:30px;opacity:0"><span class="lab" style="background:#0E8DFE">Sem multa</span> <span id="k5" class="lab" style="background:#0E8DFE;opacity:0">Sem cartão</span> <span id="k6" class="lab" style="background:#0E8DFE;opacity:0">Sem burocracia</span></div>
</div>""" + NOTE + END("Sem fidelidade.", "É só não renovar.")
    script = r"""
function render(t){
  S('q',{opacity:1-p(t,4.25,4.5),transform:`scale(${1+0.03*Math.sin(Math.min(t,2)*3)})`});
  slideUp('q2',t,2.64,.3,30);
  S('a',{opacity:p(t,4.35,4.6)*(1-p(t,12.5,12.75))});
  slideUp('k1',t,5.5,.35,50); slideUp('k2',t,7.0,.35,50); slideUp('k3',t,9.2,.35,50);
  pop('k4',t,10.3,.3,.6); pop('k5',t,11.0,.3,.6); pop('k6',t,11.7,.3,.6);
  const e=eo(p(t,12.68,13.1)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>14.2?1+0.03*Math.sin((t-14.2)*5):1})`});
  S('disc',{opacity:t<4.4?1:0});
}
"""
    sfx = [("whoosh", 4.4, .25), ("click", 5.5, .22), ("click", 7.0, .22), ("ping", 9.2, .3), ("click", 10.3, .2),
           ("click", 11.0, .2), ("click", 11.7, .2), ("whoosh", 12.68, .3), ("chime", 13.2, .45)]
    return body, script, 17.6, sfx, "/home/claude/l5/audio/new/mus1.mp3", 0.0, 0.22


def r2():
    body = '<div class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C)"></div>' + REV(
        "A cobrança veio maior do que o combinado.", '<div id="q2" style="margin-top:26px;font-size:40px;font-weight:700;color:#c0283a;opacity:0">💸 Taxa aqui, taxa ali...</div>') + f"""
<div id="a" class="abs" style="left:80px;right:80px;top:280px;opacity:0">
  <div class="h" style="font-size:96px;margin-bottom:46px">No Lomax:</div>
  {ck("k1", "Sem cobrança por mensagem.")}{ck("k2", "Sem taxa de implantação.")}{ck("k3", "Suporte grátis.")}
</div>
<div id="pr" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0">
  <div class="big">R$ 99,90</div>
  <div style="font-size:56px;font-weight:800;margin-top:20px">por mês · 2 usuários</div>
  <div id="pt" style="margin-top:60px;opacity:0"><span class="pill h" style="font-size:110px">Ponto.</span></div>
</div>""" + NOTE + END("R$ 99,90 por mês.", "Sem surpresa.")
    script = r"""
function render(t){
  S('q',{opacity:1-p(t,2.75,3.0),transform:`scale(${1+0.03*Math.sin(Math.min(t,2)*3)})`});
  pop('q2',t,1.75,.3,.6);
  S('a',{opacity:p(t,2.85,3.1)*(1-p(t,8.9,9.15))});
  slideUp('k1',t,4.1,.35,50); slideUp('k2',t,6.2,.35,50); slideUp('k3',t,7.65,.35,50);
  const pr=eo(p(t,9.05,9.4)); S('pr',{opacity:pr*(1-p(t,12.85,13.05)),transform:`scale(${0.8+0.2*pr})`});
  pop('pt',t,12.1,.3,.5);
  const e=eo(p(t,13.0,13.4)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>14.6?1+0.03*Math.sin((t-14.6)*5):1})`});
  S('disc',{opacity:t<2.9?1:0});
}
"""
    sfx = [("whoosh", 2.9, .25), ("click", 4.1, .22), ("click", 6.2, .22), ("click", 7.65, .22), ("whoosh", 9.05, .3),
           ("ping", 12.1, .35), ("whoosh", 13.0, .3), ("chime", 13.5, .45)]
    return body, script, 18.0, sfx, "/home/claude/l5/audio/new/gus_music.mp3", 0.0, 0.22


def r3():
    body = '<div class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C)"></div>' + REV(
        "Tive que deixar o computador ligado o fim de semana inteiro.", '<div id="q2" style="margin-top:26px;font-size:40px;font-weight:700;color:#c0283a;opacity:0">🖥️ Sábado e domingo ligado...</div>') + f"""
<div id="a1" class="abs" style="left:0;right:0;top:330px;text-align:center;opacity:0">
  <div class="h" style="font-size:88px">Com o Lomax,</div>
  <div class="h" style="font-size:120px;margin-top:24px"><span class="pill">não precisa.</span></div>
  <div id="cl" style="font-size:260px;margin-top:40px;opacity:0">☁️</div>
  <div id="clt" class="h" style="font-size:72px;opacity:0">Roda na nuvem.</div>
</div>
<div id="a2" class="abs" style="left:80px;right:80px;top:380px;opacity:0">
  <div class="h" style="font-size:80px;margin-bottom:46px">Sai sozinho:</div>
  {ck("k1", "Retorno pra quem sumiu.")}{ck("k2", "Confirmação de horário.")}
  <div id="pc" style="margin-top:50px;display:flex;align-items:center;gap:30px;opacity:0">
    <div class="mon" style="position:relative;width:240px;height:150px;padding:14px"><div id="scr" class="scr" style="background:#0b1522"></div></div>
    <div style="font-size:48px;font-weight:800">Com o computador<br><span class="blue">desligado.</span></div>
  </div>
</div>""" + NOTE + END("Desliga o computador.", "O Lomax segue.")
    script = r"""
function render(t){
  S('q',{opacity:1-p(t,3.55,3.8),transform:`scale(${1+0.03*Math.sin(Math.min(t,2)*3)})`});
  pop('q2',t,2.1,.3,.6);
  S('a1',{opacity:p(t,3.75,4.0)*(1-p(t,6.55,6.75))});
  pop('cl',t,5.6,.35,.5); slideUp('clt',t,5.9,.3,30);
  S('a2',{opacity:p(t,6.65,6.9)*(1-p(t,11.5,11.7))});
  slideUp('k1',t,6.8,.35,50); slideUp('k2',t,8.1,.35,50); slideUp('pc',t,10.2,.35,50);
  const off=p(t,10.8,11.1); S('scr',{background:off>0.5?'#000':'#2a6fd6'});
  const e=eo(p(t,11.65,12.05)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>13.3?1+0.03*Math.sin((t-13.3)*5):1})`});
  S('disc',{opacity:t<3.8?1:0});
}
"""
    sfx = [("whoosh", 3.8, .25), ("whoosh", 5.6, .25), ("click", 6.8, .22), ("click", 8.1, .22), ("off", 10.8, .4),
           ("whoosh", 11.65, .3), ("chime", 12.2, .45)]
    return body, script, 16.6, sfx, "/home/claude/l5/audio/new/mus1.mp3", 6.0, 0.22


def main():
    r = sys.argv[1]
    st = sys.argv[2] if len(sys.argv) > 2 else "all"
    body, script, dur, sfx, music, ms, mv = {"r1": r1, "r2": r2, "r3": r3}[r]()
    caps = reels7.layout(r, reels7.words(r))
    os.makedirs(OUT, exist_ok=True)
    page = html(body, CAPJS + "setCaps(" + json.dumps(caps) + ");" + script, CSS)
    steps = ["audio", "render", "encode"] if st == "all" else [st]
    if "audio" in steps:
        mix(OUT + f"l11_{r}_audio.wav", dur, [(reels7.A + f"{r}_voz.mp3", 0.0)], music, music_start=ms, music_vol=mv, sfx=sfx)
    if "render" in steps:
        only = [int(float(x) * FPS) for x in sys.argv[3:]] or None
        print(render(f"l11_{r}", page, dur, outdir=OUT, only=only))
    if "encode" in steps:
        encode(f"l11_{r}", OUT + f"l11_{r}_frames", OUT + f"l11_{r}_audio.wav", OUT + f"l11_{r}.mp4")
        print(OUT + f"l11_{r}.mp4")


if __name__ == "__main__":
    main()
