import sys
from reel_lib import *

LOGO = f"file://{ROOT}/logo_on_dark.png"
A0 = 0.3    # início da voz da cliente
B0 = 20.4   # início da voz do narrador (depois do "volta a fita")
DUR = 43.8

extra_css = """
.sepia{filter:sepia(.55) saturate(.7) brightness(.92)}
.colB{position:absolute;top:96px;width:205px;height:560px;border-radius:18px;background:#122238;padding:12px}
.colB .colh{font-size:19px;margin-bottom:10px}
.kc{position:absolute;width:190px;background:#fff;color:#0A192C;border-radius:16px;padding:14px 14px;box-shadow:0 14px 30px rgba(0,0,0,.35)}
.scan{position:absolute;inset:0;background:repeating-linear-gradient(rgba(255,255,255,.06) 0 2px,transparent 2px 6px);mix-blend-mode:screen}
"""

body = f"""
<div id="bgA" class="abs" style="inset:0;background:linear-gradient(#1a1712,#0f0d0a)"></div>
<div id="bgB" class="abs" style="inset:0;background:linear-gradient(#081322,#0b1d36);opacity:0"></div>

<!-- PARTE A: ponto de vista da cliente -->
<div id="A" class="abs sepia" style="inset:0">
  <div id="hook" class="abs" style="left:0;right:0;top:420px;text-align:center">
    <div class="h" style="font-size:150px;color:#ffd36b">POV:</div>
    <div class="h" style="font-size:92px;margin-top:20px">eu sou a cliente<br>que você esqueceu</div>
  </div>
  <div id="phA" class="phone" style="left:260px;top:170px;opacity:0">
    <div class="chathead"><div class="av" style="background:#8a6d3b">O</div><div><div id="chatname" style="font-weight:800;font-size:30px">Sua empresa</div><div style="font-size:22px;color:#8fa3bd">online há pouco</div></div></div>
    <div id="chatA" style="position:absolute;inset:120px 0 0 0;background:#0b1522">
      <div id="a1" class="bub out" style="top:40px;background:#2f8f5b">Oi! Quanto fica a troca das pastilhas de freio?<span class="meta">Ter 10:02 <b id="ticks" style="color:#cfd6df">✓✓</b></span></div>
      <div id="cri" class="abs" style="left:0;right:0;top:330px;text-align:center;font-size:110px;opacity:0">🦗</div>
      <div id="clockA" class="abs h" style="left:0;right:0;top:500px;text-align:center;font-size:120px;font-style:normal;opacity:0">10:02</div>
    </div>
    <div id="chatC" style="position:absolute;inset:120px 0 0 0;background:#0b1522;opacity:0">
      <div id="c1" class="bub out" style="top:40px;background:#2f8f5b">Oi! Quanto fica a troca das pastilhas de freio?<span class="meta">14:15 ✓✓</span></div>
      <div id="c2" class="bub in" style="top:220px">Oi! Fica R$ 280 com mão de obra. Consigo amanhã às 9h, pode ser? 😊<span class="meta">14:17</span></div>
      <div id="c2b" class="abs chip" style="left:24px;top:445px;background:#22c55e;opacity:0">respondeu em 2 min</div>
      <div id="c3" class="bub out" style="top:520px;background:#2f8f5b;opacity:0">Fechado! 👍<span class="meta">14:18 ✓✓</span></div>
    </div>
  </div>
  <!-- lado da empresa: lista enterrada -->
  <div id="inbox" class="phone" style="left:260px;top:170px;opacity:0">
    <div class="chathead" style="justify-content:space-between"><div style="font-weight:800;font-size:32px">Conversas</div><div class="chip" style="background:#ff4d5e">47 não lidas</div></div>
    <div id="rows" style="position:absolute;inset:120px 0 0 0;background:#0b1522;overflow:hidden"></div>
  </div>
  <div id="lost" class="abs" style="left:0;right:0;top:860px;text-align:center;opacity:0"><span style="display:inline-block;border:8px solid #ff4d5e;color:#ff4d5e;border-radius:20px;padding:14px 34px;font-weight:900;font-style:italic;font-size:76px;transform:rotate(-6deg);background:rgba(15,13,10,.75)">−R$ 280</span></div>
</div>

<!-- VOLTA A FITA -->
<div id="R" class="abs" style="inset:0;opacity:0">
  <div class="scan"></div>
  <div id="rw" class="abs h" style="left:0;right:0;top:640px;text-align:center;font-size:120px">◀◀ VOLTA<br>A FITA</div>
  <div id="rwclock" class="abs" style="left:0;right:0;top:960px;text-align:center;font-size:70px;font-weight:800;font-variant-numeric:tabular-nums;color:#ffd36b">14:18</div>
</div>

<!-- PARTE B: com o Lomax -->
<div id="B" class="abs" style="inset:0;opacity:0">
  <div id="btitle" class="abs" style="left:0;right:0;top:250px;text-align:center">
    <div style="font-size:38px;font-weight:800;letter-spacing:4px;color:#8fa3bd">TERÇA · 10:02</div>
    <div class="h" style="font-size:96px;margin-top:14px">A mesma terça,<br><span class="blue">agora com o Lomax.</span></div>
  </div>
  <div id="desk" class="abs" style="left:60px;top:250px;width:960px;opacity:0">
    <div style="height:760px;background:#1d2b3f;border-radius:28px;padding:20px">
      <div style="height:100%;background:#0b1522;border-radius:16px;position:relative;padding:20px">
        <div style="display:flex;align-items:center;justify-content:space-between"><img src="{LOGO}" style="height:32px">
          <div id="team" style="display:flex;gap:10px;opacity:0"><div class="av" style="width:48px;height:48px;font-size:22px">P</div><div class="av" style="width:48px;height:48px;font-size:22px;background:#22c55e">C</div><div class="av" style="width:48px;height:48px;font-size:22px;background:#f59e0b">V</div><div class="chip" style="background:#16253a;color:#8fa3bd;align-self:center">👀 todos veem</div></div></div>
        <div class="colB" style="left:20px"><div class="colh">Novo</div></div>
        <div class="colB" style="left:243px"><div class="colh">Em atendimento</div></div>
        <div class="colB" style="left:466px"><div class="colh">Sem resposta</div></div>
        <div class="colB" style="left:689px"><div class="colh">Agendado</div></div>
        <div id="kA" class="kc" style="left:28px;top:150px;opacity:0"><b style="font-size:24px">Ana</b><div style="font-size:18px;color:#4a5a70">Pastilhas de freio</div>
          <div id="timer" class="chip" style="margin-top:10px;background:#fff1d6;color:#9a5b00;font-size:18px;padding:6px 12px">⏱ esperando 0:00</div></div>
      </div>
    </div>
  </div>
  <div id="rep" class="abs bub out" style="left:auto;right:90px;top:760px;max-width:640px;font-size:30px;opacity:0"><b>Pedro:</b> Oi, Ana! A troca das pastilhas fica R$ 280, com mão de obra. Quer agendar? 😊<span class="meta">10:04 ✓✓</span></div>
  <div id="ghostB" class="abs" style="left:620px;top:700px;font-size:90px;opacity:0">👻</div>
  <div id="auto" class="abs bub out" style="left:auto;right:90px;top:760px;max-width:640px;font-size:30px;opacity:0">Oi, Ana! Conseguiu ver o orçamento? Tenho horário amanhã às 9h 🙂<span class="meta">☁️ retorno automático · 1 de 5</span></div>
  <div id="ansB" class="abs bub in" style="left:90px;top:940px;max-width:620px;font-size:30px;opacity:0">Vi sim! Pode ser amanhã às 9h? 🙌<span class="meta">11:20</span></div>
  <div id="paused" class="abs chip" style="right:90px;top:1080px;background:#22c55e;font-size:24px;opacity:0">✓ retornos pausados: ela respondeu</div>

  <div id="end" class="abs" style="left:0;right:0;top:300px;text-align:center;opacity:0">
    <img src="{LOGO}" style="height:118px">
    <div class="h" style="font-size:80px;margin-top:70px">Cliente esquecido<br><span class="blue">é venda pro concorrente.</span></div>
    <div id="cta" style="display:inline-block;margin-top:70px;background:#0E8DFE;border-radius:999px;padding:30px 56px;font-weight:800;font-size:46px">Teste 30 dias grátis · sem cartão</div>
    <div style="margin-top:34px;font-size:40px;font-weight:700;color:#cfe3ff">🔗 Link na bio</div>
  </div>
</div>
<div class="disc" id="disc">Imagem ilustrativa, com dados fictícios.</div>
"""

capsA = [(0.24,0.80,"Oi."),(1.12,4.40,"Eu sou aquela cliente que te pediu um orçamento na terça."),(4.72,6.52,"Mandei mensagem às dez da manhã."),
 (6.64,8.00,"Você visualizou..."),(8.24,8.82,"e nada."),(9.12,9.88,"Esperei."),(10.08,11.76,"À tarde, chamei outra empresa."),
 (11.84,13.60,"Me responderam em dois minutos."),(13.76,14.92,"Fechei com eles."),(16.56,18.48,"E você nem ficou sabendo que me perdeu.")]
capsB = [(0.27,1.04,"Volta a fita."),(1.28,3.92,"A mesma terça, agora com o Lomax."),(3.96,6.99,"A mensagem dela chega e vira um card em Novo."),
 (7.01,9.97,"A equipe toda vê há quanto tempo ela está esperando,"),(10.03,12.40,"e qualquer um responde pelo computador."),
 (12.44,14.43,"Mandou o orçamento e ela sumiu?"),(14.45,16.05,"O retorno sai sozinho."),(16.11,17.68,"E para quando ela responde."),
 (17.75,19.04,"Lomax CRM."),(19.16,21.36,"Teste 30 dias grátis, sem cartão."),(21.44,22.16,"Link na bio.")]
caps = [(a+A0,b+A0,s) for a,b,s in capsA] + [(a+B0,b+B0,s) for a,b,s in capsB]

script = f"const A0={A0},B0={B0};buildCaps(" + json.dumps(caps) + ");" + r"""
(function(){let h='';const names=['Fornecedor peças','Grupo da família','Carlos','Boleto Internet','Mãe','Promoções','Juliana','Ana','Grupo futebol','Marcos','Banco','Pedro'];
 names.forEach((n,i)=>{const isAna=n==='Ana';h+=`<div style="display:flex;align-items:center;gap:16px;padding:18px 22px;border-bottom:1px solid #16253a;${isAna?'opacity:.45':''}"><div class="av" style="width:56px;height:56px;font-size:24px;background:${isAna?'#8a6d3b':'#2a3b52'}">${n[0]}</div><div style="flex:1"><div style="font-weight:700;font-size:26px">${n}</div><div style="font-size:21px;color:#8fa3bd">${isAna?'Oi! Quanto fica a troca das pastilhas...':'...'}</div></div><div class="chip" style="background:#22c55e;font-size:18px;padding:4px 10px">${(i*7)%9+1}</div></div>`});$('rows').innerHTML=h})();
function hm(m){m=Math.round(m);return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0')}
function render(t){
  const a=t-A0, b=t-B0;
  // fundos
  S('bgB',{opacity:p(t,18.9,20.4)});
  // ---------- parte A
  S('A',{opacity:1-p(t,18.8,19.1)});
  S('hook',{opacity:(1-p(t,3.0,3.3)),transform:`scale(${lerp(1.08,1,eo(p(t,0,0.6)))})`});
  const phA=eo(p(t,3.1,3.5)); S('phA',{opacity:phA*(1-p(t,16.4,16.7)),transform:`translateY(${(1-phA)*80}px)`});
  slideUp('a1',t,A0+4.72,.3,30);
  S('ticks',{color: a>=6.9?'#53bdeb':'#cfd6df'});
  S('cri',{opacity:(a>8.2&&a<10.0)?p(a,8.2,8.5):0,transform:`translateY(${Math.sin(t*9)*6}px)`});
  const ck=p(a,8.3,10.0); S('clockA',{opacity:(a>8.2&&a<10.05)?p(a,8.2,8.4):0,text:hm(10*60+2+ck*(4*60+13))});
  // troca para a outra empresa
  const sw=p(a,10.05,10.3); S('chatA',{opacity:1-sw}); S('chatC',{opacity:sw}); S('chatname',{text: sw>0.5?'Outra empresa':'Sua empresa'});
  slideUp('c1',t,A0+10.15,.3,30); slideUp('c2',t,A0+11.9,.3,30); pop('c2b',t,A0+12.5,.3,.6); slideUp('c3',t,A0+13.8,.3,30);
  // lado da empresa: lista
  const ib=eo(p(a,16.3,16.6)); S('inbox',{opacity:ib,transform:`translateY(${(1-ib)*60}px)`});
  pop('lost',t,A0+17.6,.35,1.6);
  // ---------- volta a fita
  const r=p(t,18.85,19.0)*(1-p(t,20.3,20.5)); S('R',{opacity:r});
  S('rw',{transform:`translateX(${Math.sin(t*90)*10}px)`}); S('rwclock',{text:hm(lerp(14*60+18,10*60+2,eio(p(t,18.9,20.2))))});
  // ---------- parte B
  S('B',{opacity:p(t,20.35,20.6)});
  S('btitle',{opacity:p(b,0.1,0.4)*(1-p(b,3.8,4.0))});
  const dk=eo(p(b,3.9,4.3)); S('desk',{opacity:dk*(1-p(b,17.6,17.9)),transform:`translateY(${(1-dk)*60}px)`});
  // card da Ana: Novo -> Em atendimento (10.6) -> Sem resposta (12.5) -> Agendado (16.4)
  pop('kA',t,B0+5.9,.4,.4);
  const m1=eio(p(b,10.6,11.0)), m2=eio(p(b,12.6,13.1)), m3=eio(p(b,16.3,16.8));
  S('kA',{left:(28+223*m1+223*m2+223*m3)+'px'});
  const wait=clamp(b-6.2,0,4.6)*26; S('timer',{text:'⏱ esperando '+hm(wait/60*60/60).replace(/^00:/,'0:'), display: m1>0.5?'none':'inline-block'});
  S('timer',{text:'⏱ esperando 0:'+String(Math.floor(clamp((b-6.2)*9,0,59))).padStart(2,'0')});
  S('kA',{boxShadow: (b>7&&b<10)?`0 0 ${30+15*Math.sin(t*8)}px rgba(255,180,60,.8)`:'0 14px 30px rgba(0,0,0,.35)'});
  fade('team',t,B0+7.1,null);
  const rp=eo(p(b,10.4,10.75)); S('rep',{opacity:rp*(1-p(b,12.4,12.7)),transform:`translateY(${(1-rp)*40}px)`});
  S('ghostB',{opacity:p(b,12.9,13.2)*(1-p(b,14.3,14.5)),transform:`translateY(${Math.sin(t*4)*8}px)`});
  const au=eo(p(b,14.5,14.85)); S('auto',{opacity:au*(1-p(b,17.6,17.9)),transform:`translateY(${(1-au)*40}px)`});
  slideUp('ansB',t,B0+16.15,.3,30); S('ansB',{opacity: b>17.6?1-p(b,17.6,17.9):undefined});
  pop('paused',t,B0+16.6,.3,.6); if(b>17.6) S('paused',{opacity:1-p(b,17.6,17.9)});
  const e=eo(p(b,17.8,18.3)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${b>19.2?1+0.03*Math.sin((b-19.2)*5):1})`});
  S('disc',{opacity:(t>3.1&&b<17.7&&!(t>18.8&&t<24.3))?1:0});
}
"""

if __name__ == "__main__":
    only = None
    if len(sys.argv) > 1:
        only = [int(float(x) * FPS) for x in sys.argv[1:]]
    fdir = render("l5_r2", html(body, script, extra_css), DUR, only=only)
    print(fdir)
