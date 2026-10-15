import sys
from reel_lib import *

LOGO = f"file://{ROOT}/logo_on_dark.png"

body = f"""
<div id="bg" class="abs" style="inset:0"></div>
<div id="stars" class="abs" style="inset:0"></div>
<div id="sun" class="abs" style="width:220px;height:220px;border-radius:50%;left:430px;top:1300px;background:radial-gradient(circle,#ffd36b,#ff9f43 60%,transparent 70%);opacity:0"></div>
<div id="moon" class="abs" style="width:150px;height:150px;border-radius:50%;left:880px;top:150px;box-shadow:-34px 14px 0 0 #e8eef7;opacity:0"></div>

<!-- relógio -->
<div id="clockwrap" class="abs" style="left:0;right:0;top:330px;text-align:center">
  <div id="clocklbl" style="font-size:34px;font-weight:700;letter-spacing:4px;color:#8fa3bd">TERÇA</div>
  <div id="clock" class="h" style="font-size:260px;font-style:normal;letter-spacing:-4px;font-variant-numeric:tabular-nums">17:59</div>
</div>

<!-- loja -->
<div id="shop" class="abs" style="left:190px;top:620px;width:700px;height:480px;opacity:0">
  <div style="height:90px;background:#0E8DFE;border-radius:18px 18px 0 0;display:flex;align-items:center;justify-content:center;font-weight:900;font-style:italic;font-size:46px;letter-spacing:2px">SUA LOJA</div>
  <div style="position:relative;height:390px;background:#13243a;border:8px solid #1d3150;border-top:0;overflow:hidden">
    <div style="position:absolute;left:60px;top:60px;width:250px;height:330px;background:#ffcf6b;opacity:.9"></div>
    <div style="position:absolute;right:60px;top:60px;width:250px;height:330px;background:#ffcf6b;opacity:.9"></div>
    <div id="shutter" style="position:absolute;left:0;right:0;top:0;height:0;background:repeating-linear-gradient(#5a6b82 0 22px,#46566c 22px 30px);box-shadow:0 6px 0 #2b394c"></div>
  </div>
</div>

<!-- notebook -->
<div id="lap" class="abs" style="left:150px;top:600px;width:780px;opacity:0">
  <div style="height:470px;background:#1d2b3f;border-radius:26px;padding:22px">
    <div id="lapscr" style="height:100%;border-radius:12px;background:linear-gradient(135deg,#0E8DFE,#0a5bb0);position:relative;overflow:hidden">
      <div id="lapline" style="position:absolute;left:0;right:0;top:50%;height:4px;background:#fff;opacity:0"></div>
    </div>
  </div>
  <div style="height:34px;margin:0 -50px;background:#2a3b52;border-radius:0 0 30px 30px"></div>
</div>

<!-- celular -->
<div id="ph" class="phone" style="left:260px;top:170px;opacity:0">
  <div class="chathead"><div class="av">M</div><div><div style="font-weight:800;font-size:32px">Marina</div><div style="font-size:22px;color:#8fa3bd">cliente</div></div></div>
  <div id="chat" style="position:absolute;inset:120px 0 0 0;background:#0b1522">
    <div id="b1" class="bub in" style="top:40px">Oi! Quanto fica a revisão completa do meu carro?<span class="meta">14:10</span></div>
    <div id="b2" class="bub out" style="top:230px">Fica R$ 480, com peças. Quer que eu já reserve um horário?<span class="meta">14:12 ✓✓</span></div>
    <div id="seen" class="abs" style="left:0;right:0;top:470px;text-align:center;font-size:24px;color:#8fa3bd;opacity:0">Visualizada às 14:13 · sem resposta</div>
    <div id="ghost" class="abs" style="left:0;right:0;top:540px;text-align:center;font-size:120px;opacity:0">👻</div>
    <div id="b3" class="bub out" style="top:470px;opacity:0">Oi, Marina! Conseguiu ver o orçamento da revisão? Se quiser, deixo um horário reservado 🙂<span class="meta">09:00 ✓✓</span></div>
    <div id="sentby" class="abs" style="right:24px;top:715px;font-size:22px;color:#7fc0ff;font-weight:700;opacity:0">☁️ enviado pelo Lomax</div>
  </div>
</div>
<div id="lcard" class="abs card" style="left:150px;top:880px;width:780px;opacity:0;display:flex;align-items:center;gap:22px">
  <div style="font-size:60px">☁️</div>
  <div><div style="font-weight:800;font-size:34px">Retorno automático agendado</div><div style="font-size:26px;color:#4a5a70;margin-top:4px">Marina · Revisão · R$ 480</div></div>
</div>

<!-- nuvem -->
<div id="cloudsc" class="abs" style="left:0;right:0;top:250px;height:900px;opacity:0">
  <div id="cloud" class="abs" style="left:290px;top:40px;width:500px;height:280px">
    <svg viewBox="0 0 500 280" width="500" height="280"><path d="M120 250h270a90 90 0 0 0 10-179A130 130 0 0 0 150 60 95 95 0 0 0 120 250z" fill="#0E8DFE"/></svg>
    <div class="abs" style="left:0;right:0;top:120px;text-align:center"><img src="{LOGO}" style="height:52px;filter:brightness(10)"></div>
  </div>
  <div id="ring" class="abs" style="left:440px;top:90px;width:200px;height:200px;border-radius:50%;border:6px solid #0E8DFE;opacity:0"></div>
  <div id="t1" class="abs h" style="left:0;right:0;top:380px;text-align:center;font-size:96px">Roda <span class="blue">na nuvem.</span></div>
  <div id="x1" class="abs" style="left:150px;top:560px;width:780px;display:flex;align-items:center;gap:26px;font-size:50px;font-weight:800;opacity:0">
    <div style="width:84px;height:84px;border-radius:20px;background:#ff4d5e;display:flex;align-items:center;justify-content:center;font-size:52px">✕</div>Sem extensão</div>
  <div id="x2" class="abs" style="left:150px;top:690px;width:780px;display:flex;align-items:center;gap:26px;font-size:50px;font-weight:800;opacity:0">
    <div style="width:84px;height:84px;border-radius:20px;background:#ff4d5e;display:flex;align-items:center;justify-content:center;font-size:52px">✕</div>Sem computador ligado</div>
</div>

<!-- kanban no notebook -->
<div id="kan" class="abs" style="left:90px;top:330px;width:900px;opacity:0">
  <div style="height:640px;background:#1d2b3f;border-radius:26px;padding:22px">
    <div style="height:100%;border-radius:14px;background:#0b1522;position:relative;overflow:hidden;padding:24px">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:22px"><img src="{LOGO}" style="height:34px"><div class="chip" style="background:#16253a;color:#8fa3bd">Quarta · 09:12</div></div>
      <div class="col" style="left:24px;top:92px;height:480px;width:400px"><div class="colh">Sem resposta</div></div>
      <div class="col" style="left:452px;top:92px;height:480px;width:400px"><div class="colh">Em atendimento</div></div>
      <div class="abs card" style="left:44px;top:390px;width:360px;opacity:.55"><div style="font-weight:800;font-size:28px">João</div><div style="font-size:22px;color:#4a5a70">Troca de óleo · R$ 220</div></div>
      <div class="abs card" style="left:472px;top:390px;width:360px;opacity:.55"><div style="font-weight:800;font-size:28px">Paula</div><div style="font-size:22px;color:#4a5a70">Alinhamento · R$ 150</div></div>
      <div id="kc" class="abs card" style="left:44px;top:160px;width:360px">
        <div style="font-weight:800;font-size:30px">Marina</div>
        <div style="font-size:24px;color:#4a5a70;margin-top:4px">Revisão completa · R$ 480</div>
        <div id="kmsg" style="margin-top:14px;background:#e8f3ff;border-radius:14px;padding:12px 14px;font-size:24px;font-weight:600;opacity:0">💬 "Vi sim! Pode ser sábado?"</div>
      </div>
    </div>
  </div>
  <div style="height:34px;margin:0 -50px;background:#2a3b52;border-radius:0 0 30px 30px"></div>
</div>

<!-- final -->
<div id="end" class="abs" style="left:0;right:0;top:330px;text-align:center;opacity:0">
  <img id="endlogo" src="{LOGO}" style="height:118px">
  <div class="h" style="font-size:84px;margin-top:70px">Desligou o computador?<br><span class="blue">O Lomax continua.</span></div>
  <div id="cta" style="display:inline-block;margin-top:70px;background:#0E8DFE;border-radius:999px;padding:30px 56px;font-weight:800;font-size:46px">Teste 30 dias grátis · sem cartão</div>
  <div style="margin-top:34px;font-size:40px;font-weight:700;color:#cfe3ff">🔗 Link na bio</div>
</div>
<div class="disc" id="disc">Imagem ilustrativa, com dados fictícios.</div>
"""

caps = [
 (0.59,1.28,"Seis da tarde."),(1.52,2.64,"Loja fechada."),(2.80,4.24,"Computador desligado."),
 (4.48,7.12,"Mas aquele cliente que pediu orçamento e sumiu..."),(7.16,8.40,"não foi esquecido."),
 (8.63,11.12,"No horário marcado, o retorno sai sozinho."),(11.24,13.20,"Direto do Lomax, que roda na nuvem."),
 (13.28,15.44,"Sem extensão, sem computador ligado."),(15.56,17.92,"Você chega no dia seguinte, abre o sistema..."),
 (17.96,19.20,"e ele já respondeu."),(19.27,20.56,"Lomax CRM."),(20.68,22.72,"Teste 30 dias grátis, sem cartão."),(22.80,23.60,"Link na bio."),
]

script = "buildCaps(" + json.dumps(caps) + ");" + r"""
// estrelas
(function(){let h='';for(let i=0;i<60;i++){const x=(i*397)%1080,y=(i*211)%1100+60,s=(i%3)+2;h+=`<div style="position:absolute;left:${x}px;top:${y}px;width:${s}px;height:${s}px;border-radius:50%;background:#fff;opacity:${.25+(i%5)/10}"></div>`}$('stars').innerHTML=h})();
function render(t){
  // céu: noite (0-10) -> manhã (10-19)
  const day=eio(p(t,9.0,10.6));
  const top=`rgb(${lerp(5,24,day)},${lerp(14,58,day)},${lerp(28,102,day)})`, bot=`rgb(${lerp(10,52,day)},${lerp(25,110,day)},${lerp(44,170,day)})`;
  S('bg',{background:`linear-gradient(${top},${bot})`});
  S('stars',{opacity:(1-day)*(t<19.3?1:0)*clamp(p(t,0,1)+0.4)});
  S('moon',{opacity:(1-day)*fade('moon',t,0.2,null)*(t<11?1:0)});
  const sunx=p(t,9.2,10.8); S('sun',{opacity:sunx*(t<11.2?1:0),top:lerp(1300,700,eo(sunx))+'px'});

  // relógio
  const cw=$('clockwrap');
  let cOp = t<4.3 ? 1-p(t,4.0,4.3) : (t>=8.5 && t<10.4 ? p(t,8.5,8.8)*(1-p(t,10.1,10.4)) : 0);
  S(cw,{opacity:cOp});
  if(t<8.5){ S('clock',{text: t<0.6?'17:59':'18:00'}); S('clocklbl',{text:'TERÇA'}); S('clock',{color:t<0.6?'#fff':'#fff',transform:`scale(${t>=0.6&&t<0.9?1.06:1})`}); }
  else { // time-lapse 18:00 -> 09:00
    const x=eio(p(t,8.7,9.9)); const mins=18*60+x*(15*60); const hh=Math.floor(mins/60)%24, mm=Math.floor(mins%60);
    S('clock',{text:String(hh).padStart(2,'0')+':'+String(mm).padStart(2,'0'),transform:'scale(1)'}); S('clocklbl',{text: x<0.5?'TERÇA · NOITE':'QUARTA · MANHÃ'}); }

  // loja (1.3 - 2.9)
  S('shop',{opacity:p(t,1.2,1.5)*(1-p(t,2.7,2.95))});
  S('shutter',{height:lerp(0,390,eio(p(t,1.6,2.4)))+'px'});
  // notebook (2.75 - 4.35)
  S('lap',{opacity:p(t,2.75,3.0)*(1-p(t,4.1,4.4))});
  const off=p(t,3.0,3.45);
  S('lapscr',{background: off<1?`linear-gradient(135deg,rgba(14,141,254,${1-off}),rgba(10,91,176,${1-off})),#05080d`:'#05080d', transform:`scaleY(${off<0.6?1:lerp(1,1,off)})`});
  S('lapline',{opacity: off>0.3&&off<1? Math.sin(off*Math.PI):0});

  // celular (4.35 - 8.5) e volta (10.1 - 11.3)
  let phOp=0, phY=170;
  if(t>=4.3&&t<8.6){const x=eo(p(t,4.3,4.75)); phOp=x*(1-p(t,8.3,8.6)); phY=lerp(400,170,x);}
  if(t>=10.0&&t<11.4){const x=eo(p(t,10.0,10.3)); phOp=x*(1-p(t,11.1,11.4)); phY=lerp(300,170,x);}
  S('ph',{opacity:phOp,transform:`translateY(${phY-170}px)`});
  slideUp('b1',t,4.5,.35,40); slideUp('b2',t,5.0,.35,40);
  const sumiu=p(t,6.2,6.6);
  S('seen',{opacity: t<9?sumiu:0}); S('ghost',{opacity: t<9? sumiu*(0.9):0, transform:`translateY(${Math.sin(t*4)*8}px)`});
  S('chat',{filter: t<9?`saturate(${1-sumiu*0.7})`:'none'});
  if(t>=10){ S('b1',{opacity:.35}); S('b2',{opacity:.35}); slideUp('b3',t,10.1,.4,50); fade('sentby',t,10.5,null);}
  else { S('b3',{opacity:0}); S('sentby',{opacity:0}); }
  // card de retorno agendado (7.15 - 8.5)
  const lc=eo(p(t,7.15,7.5)); S('lcard',{opacity:lc*(1-p(t,8.3,8.55)),transform:`translateY(${(1-lc)*60}px) scale(${lerp(.9,1,lc)})`,boxShadow:`0 0 ${40+20*Math.sin(t*6)}px rgba(14,141,254,.6)`});

  // nuvem (11.25 - 15.5)
  S('cloudsc',{opacity:p(t,11.25,11.5)*(1-p(t,15.3,15.55))});
  pop('cloud',t,11.3,.45,.5);
  const r=(t*1.2)%1; S('ring',{opacity:(t>11.6&&t<15.5)?(1-r)*.8:0,transform:`scale(${1+r*1.6})`});
  slideUp('t1',t,11.9,.4,40); slideUp('x1',t,13.3,.35,40); slideUp('x2',t,14.2,.35,40);

  // kanban (15.5 - 19.3)
  const k=eo(p(t,15.5,15.95)); S('kan',{opacity:k*(1-p(t,19.1,19.35)),transform:`translateY(${(1-k)*80}px)`});
  const mv=eio(p(t,18.0,18.6)); S('kc',{left:lerp(44,472,mv)+'px',boxShadow: mv>0&&mv<1?'0 30px 60px rgba(0,0,0,.5)':'0 18px 40px rgba(0,0,0,.35)'});
  slideUp('kmsg',t,17.95,.3,20);

  // final
  const e=eo(p(t,19.3,19.8)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>20.6?1+0.03*Math.sin((t-20.6)*5):1})`});
  S('disc',{opacity: (t>4.4&&t<19.2)?1:0});
}
"""

if __name__ == "__main__":
    only = None
    if len(sys.argv) > 1:
        only = [int(float(x) * FPS) for x in sys.argv[1:]]
    fdir = render("l5_r1", html(body, script), 24.8, only=only)
    print(fdir)
