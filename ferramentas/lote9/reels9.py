"""Reels do lote 9 (30/10): 'O seu WhatsApp no automático' (R1, Jhony) e 'Domingo no Rio' (R2, Nayara).
Uso: python3 reels9.py r1|r2 [render|audio|encode|all] [t1 t2 ... só esses quadros]
"""
import sys, json, os
sys.path.insert(0, "/home/claude/l7"); sys.path.insert(0, "/home/claude/l5")
import reels7
from reels7 import EXTRA_CSS, CAPJS, LOGO
from reel_lib import html, render, encode, FPS
from mix import mix

reels7.A = "/home/claude/l9/audio/"
OUT = "/home/claude/l9/reels/"

reels7.LAYOUT["r1"] = ["Oito da manhã.", "Chegou cliente novo?", "O Lomax já passou", "pra um atendente.", "Dez horas.",
    "Aquele cliente que pediu", "orçamento e sumiu?", "O retorno sai sozinho.", "Três da tarde.", "Tem horário marcado pra amanhã?",
    "A confirmação vai", "no dia anterior.", "Seis da tarde.", "Você desliga o computador", "e vai pra casa.", "E o Lomax segue na nuvem,",
    "sem depender de ninguém lembrar.", "Lomax CRM.", "O seu WhatsApp no automático.", "Teste trinta dias grátis."]
reels7.LAYOUT["r2"] = ["Domingo de sol no Rio.", "Praia, família,", "aquele mate gelado.", "E o celular?", "Fica no bolso.",
    "Porque o cliente que pediu", "orçamento na sexta e sumiu", "vai receber o retorno", "na segunda cedo, sozinho,", "em horário comercial.",
    "E quem chamar no domingo", "cai no funil, já com dono,", "esperando a equipe.", "Lomax CRM.", "Feito por carioca,",
    "pra você curtir o domingo.", "Teste trinta dias grátis."]

CSS = EXTRA_CSS + """
.clock{display:inline-flex;align-items:center;gap:18px;background:#fff;color:#0A192C;border-radius:999px;padding:18px 40px;font-weight:900;font-style:italic;font-size:76px;box-shadow:0 18px 40px rgba(0,0,0,.35)}
.lbl{display:inline-block;border-radius:12px;padding:6px 14px;font-size:24px;font-weight:800}
"""

END = lambda line1, pill: f"""
<div id="end" class="abs" style="left:0;right:0;top:250px;text-align:center;opacity:0">
  <img src="{LOGO}" style="height:118px">
  <div class="h" style="font-size:92px;margin-top:80px">{line1}</div>
  <div class="h" style="font-size:92px;margin-top:20px"><span class="pill">{pill}</span></div>
  <div id="cta" style="display:inline-block;margin-top:80px;background:#0E8DFE;border-radius:999px;padding:30px 56px;font-weight:800;font-size:46px">Teste 30 dias grátis · sem cartão</div>
  <div style="margin-top:34px;font-size:40px;font-weight:700;color:#cfe3ff">🔗 Link na bio</div>
</div>
<div class="disc" id="disc">Cena ilustrativa, com dados fictícios.</div>"""


def r1():
    body = f"""
<div id="bg" class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C)"></div>
<div id="clk" class="abs" style="left:0;right:0;top:200px;text-align:center"><span class="clock">🕗 <span id="ctime">08:00</span></span></div>

<div id="s1" class="abs" style="left:110px;right:110px;top:460px;opacity:0">
  <div class="card" style="padding:30px 34px"><div style="display:flex;justify-content:space-between;align-items:center"><b style="font-size:40px">Bruno Teixeira</b><span class="lbl" style="background:#e3f0ff;color:#0b6fd0">Novo</span></div>
  <div style="font-size:32px;color:#4a5a70;margin-top:10px">“Bom dia! Vocês fazem revisão?”</div>
  <div id="as1" style="margin-top:18px;opacity:0"><span class="lbl" style="background:#e1f6e9;color:#1f8a4c;font-size:30px">👤 Atendente: Ana</span></div></div>
</div>

<div id="s2" class="abs" style="left:110px;right:110px;top:460px;opacity:0">
  <div class="card" style="padding:30px 34px"><div style="display:flex;justify-content:space-between;align-items:center"><b style="font-size:40px">Rafael Souza</b><span class="lbl" style="background:#fde8ea;color:#c0283a">Sem resposta</span></div>
  <div style="font-size:32px;color:#4a5a70;margin-top:10px">📄 Orçamento enviado ontem</div>
  <div id="rt" style="margin-top:18px;opacity:0"><span class="lbl" style="background:#e3f0ff;color:#0b6fd0;font-size:30px">⏰ Retorno automático enviado</span></div></div>
</div>

<div id="s3" class="abs" style="left:110px;right:110px;top:440px;opacity:0">
  <div class="card" style="padding:30px 34px"><div style="display:flex;justify-content:space-between;align-items:center"><b style="font-size:40px">Juliana Lima</b><span class="lbl" style="background:#fff3d1;color:#9a6500">Agendado</span></div>
  <div style="font-size:32px;color:#4a5a70;margin-top:10px">📅 Amanhã, 9h</div></div>
  <div id="cf" class="bub out" style="position:relative;right:auto;margin:34px 0 0 140px;font-size:34px;max-width:none;opacity:0">Oi, Juliana! Confirmando seu horário amanhã às 9h. Tudo certo? 🙂<span class="meta">automático · dia anterior</span></div>
</div>

<div id="s4" class="abs" style="inset:0;opacity:0">
  <div class="mon" style="left:190px;top:470px;width:700px;height:430px"><div id="scr" class="scr" style="display:flex;align-items:center;justify-content:center"><img src="{LOGO}" style="height:60px"></div></div>
  <div style="position:absolute;left:470px;top:900px;width:140px;height:60px;background:#1d2b3f"></div>
  <div style="position:absolute;left:380px;top:955px;width:320px;height:20px;border-radius:10px;background:#1d2b3f"></div>
  <div id="home" class="abs" style="left:0;right:0;top:1000px;text-align:center;font-size:120px;opacity:0">🏠</div>
</div>

<div id="s5" class="abs" style="inset:0;opacity:0">
  <div id="cloud" class="abs" style="left:0;right:0;top:400px;text-align:center;font-size:300px;line-height:1">☁️</div>
  <div class="abs" style="left:0;right:0;top:730px;text-align:center"><img src="{LOGO}" style="height:64px"></div>
  <div id="c1" class="abs" style="left:120px;top:880px;opacity:0"><span class="lbl" style="background:#16253a;color:#9fd0ff;font-size:34px;padding:12px 22px">🔀 distribui</span></div>
  <div id="c2" class="abs" style="left:420px;top:980px;opacity:0"><span class="lbl" style="background:#16253a;color:#9fd0ff;font-size:34px;padding:12px 22px">⏰ retorna</span></div>
  <div id="c3" class="abs" style="left:680px;top:880px;opacity:0"><span class="lbl" style="background:#16253a;color:#9fd0ff;font-size:34px;padding:12px 22px">📅 confirma</span></div>
</div>
""" + END("O seu WhatsApp", "no automático.")
    script = r"""
function render(t){
  // relógio
  const T=[[0,'08:00','⏰'],[4.45,'10:00','⏰'],[9.37,'15:00','⏰'],[14.13,'18:00','⏰']];
  let cur=T[0]; T.forEach(x=>{if(t>=x[0])cur=x});
  S('ctime',{text:cur[1]}); document.querySelector('.clock').firstChild.textContent=cur[2]+' ';
  const tick=T.map(x=>p(t,x[0],x[0]+.25)*(1-p(t,x[0]+.25,x[0]+.5))).reduce((a,b)=>Math.max(a,b),0);
  S('clk',{opacity:1-p(t,17.5,17.8),transform:`scale(${1+.12*tick})`});
  // cenas
  const sc=(id,a,b)=>{const x=eo(p(t,a,a+.35)); S(id,{opacity:x*(1-p(t,b,b+.3)),transform:`translateY(${(1-x)*60}px)`})};
  sc('s1',0.9,4.3); pop('as1',t,2.9,.3,.5);
  sc('s2',5.45,9.2); pop('rt',t,8.0,.3,.5);
  sc('s3',10.4,13.95); slideUp('cf',t,12.05,.35,40);
  S('s4',{opacity:p(t,14.2,14.5)*(1-p(t,17.5,17.8))});
  const off=p(t,15.6,16.0); S('scr',{opacity:1-off*.95});
  pop('home',t,16.9,.35,.5);
  S('s5',{opacity:p(t,17.75,18.05)*(1-p(t,21.4,21.7))});
  S('cloud',{transform:`translateY(${Math.sin(t*2)*10}px)`});
  pop('c1',t,18.9,.3,.5); pop('c2',t,19.6,.3,.5); pop('c3',t,20.3,.3,.5);
  const e=eo(p(t,21.6,22.05)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>25.1?1+0.03*Math.sin((t-25.1)*5):1})`});
  S('disc',{opacity:(t>0.9&&t<17.5)?1:0});
}
"""
    sfx = [("ping", 0.95, .35), ("click", 2.9, .25), ("whoosh", 4.45, .25), ("ping", 5.5, .3), ("ping", 8.0, .35),
           ("whoosh", 9.37, .25), ("click", 10.45, .22), ("ping", 12.05, .35), ("whoosh", 14.13, .25), ("off", 15.6, .4),
           ("click", 16.9, .22), ("whoosh", 17.75, .3), ("click", 18.9, .2), ("click", 19.6, .2), ("click", 20.3, .2),
           ("whoosh", 21.6, .3), ("chime", 22.1, .45)]
    return body, script, 28.0, sfx, "/home/claude/l5/audio/new/mus1.mp3", 0.0, 0.26


def r2():
    body = f"""
<div id="sky" class="abs" style="inset:0;background:linear-gradient(180deg,#5cc6ff 0%,#9fdcff 45%,#ffe9b0 62%,#f6d38b 100%)"></div>
<div id="sun" class="abs" style="left:720px;top:160px;width:200px;height:200px;border-radius:50%;background:radial-gradient(#fff6c8,#ffd25a);box-shadow:0 0 120px #ffd25a"></div>
<svg id="sea" class="abs" style="left:0;top:780px" width="1080" height="260" viewBox="0 0 1080 260"><path id="wave" d="M0 60 Q 135 20 270 60 T 540 60 T 810 60 T 1080 60 L1080 260 L0 260 Z" fill="#1f8fd8"/><path d="M0 120 Q 135 90 270 120 T 540 120 T 810 120 T 1080 120 L1080 260 L0 260 Z" fill="#167ac0"/></svg>
<div id="sand" class="abs" style="left:0;right:0;top:1040px;bottom:0;background:#f3d79a"></div>
<div id="tag" class="abs" style="left:0;right:0;top:420px;text-align:center"><span class="clock" style="font-size:64px">☀️ Domingo · Rio</span></div>
<div id="band" class="abs" style="left:0;right:0;top:1215px;height:230px;background:rgba(10,25,44,.62)"></div>
<div id="e1" class="abs" style="left:170px;top:1050px;font-size:120px;opacity:0">⛱️</div>
<div id="e2" class="abs" style="left:480px;top:1050px;font-size:120px;opacity:0">🏐</div>
<div id="e3" class="abs" style="left:780px;top:1050px;font-size:120px;opacity:0">🥤</div>
<div id="ph" class="abs" style="left:430px;top:560px;width:220px;height:400px;border-radius:40px;background:#0d1117;border:8px solid #1f2a3a;opacity:0"></div>

<div id="s2" class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C);opacity:0">
  <div class="abs h" style="left:0;right:0;top:220px;text-align:center;font-size:78px">Enquanto isso,<br><span class="blue">o Lomax trabalha.</span></div>
  <div id="d1" class="abs card" style="left:110px;right:110px;top:520px;padding:30px 34px"><div style="font-size:26px;font-weight:800;color:#6a788c;letter-spacing:2px">SEXTA</div><div style="font-size:36px;margin-top:8px">📄 Orçamento enviado pro Rafael</div><div style="font-size:28px;color:#c0283a;margin-top:8px;font-weight:700">e ele sumiu...</div></div>
  <div id="d2" class="abs card" style="left:110px;right:110px;top:820px;padding:30px 34px;opacity:0"><div style="font-size:26px;font-weight:800;color:#0b6fd0;letter-spacing:2px">SEGUNDA · 9H</div><div style="font-size:36px;margin-top:8px">⏰ Retorno automático enviado</div><div id="hc" style="margin-top:12px;opacity:0"><span class="lbl" style="background:#e1f6e9;color:#1f8a4c;font-size:28px">🕘 só em horário comercial</span></div></div>
</div>

<div id="s3" class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C);opacity:0">
  <div class="mon" style="left:60px;top:380px;width:960px;height:640px"><div class="scr">
    <div class="col" style="left:22px;top:22px;height:570px;width:430px"><div class="colh">Novo</div></div>
    <div class="col" style="left:470px;top:22px;height:570px;width:430px"><div class="colh">Em atendimento</div></div>
    <div id="k1" class="abs card" style="left:40px;top:100px;width:394px;opacity:0"><b style="font-size:30px">Marcos</b><div style="font-size:24px;color:#4a5a70;margin-top:6px">domingo, 16:20 · “Tem horário essa semana?”</div><div id="ow" style="margin-top:12px;opacity:0"><span class="lbl" style="background:#e1f6e9;color:#1f8a4c">👤 Paulo</span></div></div>
  </div></div>
</div>
""" + END("Feito por carioca,", "pra curtir o domingo.")
    script = r"""
function render(t){
  S('wave',{transform:`translateX(${Math.sin(t*1.5)*20}px)`});
  const beach=1-p(t,7.1,7.4);
  ['sky','sun','sea','sand','tag','band'].forEach(id=>S(id,{opacity:beach}));
  const tg=eo(p(t,0.1,0.5)); S('tag',{opacity:tg*beach,transform:`translateY(${(1-tg)*-40}px)`});
  const em=(id,a)=>{const x=pop(id,t,a,.35,.4); S(id,{opacity:(x>0?1:0)*beach})}; em('e1',1.84); em('e2',2.48); em('e3',3.84);
  const ph=p(t,5.2,5.4)*(1-p(t,6.4,6.9)); const drop=eio(p(t,6.0,6.9));
  S('ph',{opacity:ph*beach,transform:`translateY(${drop*500}px) scale(${1-drop*.5})`});
  S('s2',{opacity:p(t,7.15,7.45)*(1-p(t,14.1,14.4))});
  slideUp('d1',t,7.6,.4,40); slideUp('d2',t,10.45,.4,40); pop('hc',t,12.95,.3,.5);
  S('s3',{opacity:p(t,14.15,14.45)*(1-p(t,18.0,18.3))});
  const k=eo(p(t,14.85,15.25)); S('k1',{opacity:k,transform:`translateY(${(1-k)*-80}px)`});
  pop('ow',t,16.6,.3,.5);
  const e=eo(p(t,18.2,18.65)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>22.5?1+0.03*Math.sin((t-22.5)*5):1})`});
  S('disc',{opacity:(t>7.3&&t<18.1)?1:0});
}
"""
    sfx = [("whoosh", 0.1, .25), ("click", 1.84, .2), ("click", 2.48, .2), ("click", 3.84, .2), ("whoosh", 6.0, .25),
           ("whoosh", 7.15, .3), ("ping", 7.6, .3), ("ping", 10.45, .35), ("click", 12.95, .22), ("whoosh", 14.15, .3),
           ("ping", 14.9, .35), ("click", 16.6, .22), ("whoosh", 18.2, .3), ("chime", 18.8, .45)]
    return body, script, 25.6, sfx, "/home/claude/l5/audio/new/gus_music.mp3", 0.0, 0.24


def main():
    r = sys.argv[1]
    st = sys.argv[2] if len(sys.argv) > 2 else "all"
    body, script, dur, sfx, music, ms, mv = {"r1": r1, "r2": r2}[r]()
    caps = reels7.layout(r, reels7.words(r))
    os.makedirs(OUT, exist_ok=True)
    page = html(body, CAPJS + "setCaps(" + json.dumps(caps) + ");" + script, CSS)
    steps = ["audio", "render", "encode"] if st == "all" else [st]
    if "audio" in steps:
        mix(OUT + f"l9_{r}_audio.wav", dur, [(reels7.A + f"{r}_voz.mp3", 0.0)], music, music_start=ms, music_vol=mv, sfx=sfx)
    if "render" in steps:
        only = [int(float(x) * FPS) for x in sys.argv[3:]] or None
        print(render(f"l9_{r}", page, dur, outdir=OUT, only=only))
    if "encode" in steps:
        encode(f"l9_{r}", OUT + f"l9_{r}_frames", OUT + f"l9_{r}_audio.wav", OUT + f"l9_{r}.mp4")
        print(OUT + f"l9_{r}.mp4")


if __name__ == "__main__":
    main()
