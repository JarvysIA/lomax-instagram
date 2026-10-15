import sys
from reel_lib import *

LOGO = f"file://{ROOT}/logo_on_dark.png"

def chip(i, emoji, txt, top):
    return f'<div id="ch{i}" class="abs" style="left:170px;top:{top}px;width:740px;display:flex;align-items:center;gap:24px;background:#16253a;border-radius:26px;padding:26px 30px;font-size:44px;font-weight:800;opacity:0"><span style="font-size:58px">{emoji}</span>{txt}</div>'

body = f"""
<div id="bg" class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C)"></div>
<div id="red" class="abs" style="inset:0;background:radial-gradient(circle at 50% 40%,rgba(255,77,94,.35),transparent 60%);opacity:0"></div>

<!-- tela bloqueada -->
<div id="lock" class="phone" style="left:260px;top:170px;background:linear-gradient(160deg,#1b2d47,#0b1522)">
  <div style="text-align:center;margin-top:110px;font-size:30px;font-weight:600;color:#c9d6e8">Sexta-feira, 17 de outubro</div>
  <div class="h" style="text-align:center;font-size:150px;font-style:normal;margin-top:8px">17:48</div>
  <div id="notif" style="position:absolute;left:22px;right:22px;top:430px;background:rgba(255,255,255,.92);color:#0A192C;border-radius:30px;padding:24px 26px;opacity:0">
    <div style="display:flex;align-items:center;gap:14px"><div class="av" style="width:52px;height:52px;font-size:24px;color:#fff">R</div>
    <div style="font-weight:800;font-size:28px">Rafael · Atendente</div><div style="margin-left:auto;font-size:22px;color:#6a788c">agora</div></div>
    <div style="font-size:29px;margin-top:12px;line-height:1.3">Chefe, hoje é meu último dia. Obrigado por tudo 🫡</div>
  </div>
</div>

<!-- o que vai embora -->
<div id="gone" class="abs" style="inset:0;opacity:0">
  <div id="gtitle" class="abs h" style="left:0;right:0;top:240px;text-align:center;font-size:76px">E com ele vão embora...</div>
  {chip(1,'💬','as conversas',420)}
  {chip(2,'📄','os orçamentos',560)}
  {chip(3,'🤝','os clientes quase fechando',700)}
  <div id="rph" class="abs" style="left:400px;top:880px;width:280px;height:300px;border-radius:40px;background:#0d1117;border:8px solid #1f2a3a;display:flex;align-items:center;justify-content:center;flex-direction:column;opacity:0">
    <div style="font-size:70px">📱</div><div style="font-size:26px;font-weight:800;margin-top:10px;text-align:center">celular<br>do Rafael</div></div>
  <div id="door" class="abs" style="left:880px;top:880px;font-size:150px;opacity:0">🚪</div>
</div>

<!-- Lomax -->
<div id="lom" class="abs" style="inset:0;opacity:0">
  <div id="ltitle" class="abs h" style="left:0;right:0;top:220px;text-align:center;font-size:84px">No Lomax, o atendimento<br><span class="blue">é da empresa.</span></div>
  <div id="board" class="abs" style="left:70px;top:470px;width:940px;height:660px;background:#1d2b3f;border-radius:30px;padding:22px">
    <div style="height:100%;background:#0b1522;border-radius:16px;position:relative;padding:22px">
      <div style="display:flex;align-items:center;justify-content:space-between"><img src="{LOGO}" style="height:34px"><div class="chip" style="background:#16253a;color:#8fa3bd">🛡️ dados da empresa</div></div>
      <div class="col" style="left:22px;top:84px;height:530px;width:280px"><div class="colh">Novo</div></div>
      <div class="col" style="left:318px;top:84px;height:530px;width:280px"><div class="colh">Em atendimento</div></div>
      <div class="col" style="left:614px;top:84px;height:530px;width:280px"><div class="colh">Agendado</div></div>
      <div id="k1" class="abs card" style="left:38px;top:150px;width:248px"><b style="font-size:26px">Carla</b><div style="font-size:21px;color:#4a5a70">💬 conversa completa</div></div>
      <div id="k2" class="abs card" style="left:334px;top:150px;width:248px"><b style="font-size:26px">Diego</b><div style="font-size:21px;color:#4a5a70">📄 orçamento R$ 1.250</div></div>
      <div id="k3" class="abs card" style="left:334px;top:290px;width:248px"><b style="font-size:26px">Fábio</b><div style="font-size:21px;color:#4a5a70">🕓 histórico de 3 meses</div></div>
      <div id="k4" class="abs card" style="left:630px;top:150px;width:248px"><b style="font-size:26px">Helena</b><div style="font-size:21px;color:#4a5a70">📅 sábado, 9h</div></div>
      <div id="lockico" class="abs" style="left:0;right:0;top:470px;text-align:center;font-size:30px;font-weight:800;color:#7fc0ff;opacity:0">🔒 Tudo fica no sistema</div>
    </div>
  </div>
</div>

<!-- usuários -->
<div id="users" class="abs" style="left:110px;top:300px;width:860px;opacity:0">
  <div class="h" style="font-size:74px;text-align:center;margin-bottom:50px">Troca o usuário.<br><span class="blue">A vaga é a mesma.</span></div>
  <div style="background:#122238;border-radius:30px;padding:30px">
    <div style="display:flex;justify-content:space-between;font-weight:800;font-size:28px;color:#8fa3bd;margin-bottom:20px"><span>USUÁRIOS</span><span>2 de 2 vagas</span></div>
    <div style="display:flex;align-items:center;gap:20px;background:#16253a;border-radius:20px;padding:22px;margin-bottom:16px"><div class="av">L</div><div style="font-size:34px;font-weight:700">Luiz</div><div class="chip" style="margin-left:auto;background:#0E8DFE">Admin</div></div>
    <div style="position:relative;height:106px">
      <div id="uR" class="abs" style="inset:0;display:flex;align-items:center;gap:20px;background:#16253a;border-radius:20px;padding:22px"><div class="av" style="background:#6a788c">R</div><div id="rname" style="font-size:34px;font-weight:700">Rafael</div><div class="chip" style="margin-left:auto;background:#2a3b52">Atendente</div></div>
      <div id="uB" class="abs" style="inset:0;display:flex;align-items:center;gap:20px;background:#16253a;border-radius:20px;padding:22px;opacity:0;border:3px solid #0E8DFE"><div class="av" style="background:#22c55e">B</div><div style="font-size:34px;font-weight:700">Bruno</div><div class="chip" style="margin-left:auto;background:#2a3b52">Atendente</div></div>
    </div>
  </div>
  <div id="zero" style="text-align:center;margin-top:40px;opacity:0"><span class="chip" style="background:#22c55e;font-size:38px;padding:16px 34px">R$ 0 a mais</span></div>
</div>

<!-- Bruno vê tudo -->
<div id="hist" class="abs" style="left:150px;top:300px;width:780px;opacity:0">
  <div class="card" style="padding:30px">
    <div style="display:flex;align-items:center;gap:16px"><div class="av" style="background:#22c55e;color:#fff">B</div><div style="font-weight:800;font-size:32px">Bruno abriu: Diego</div></div>
    <div id="hl1" style="margin-top:22px;font-size:27px;padding:14px 18px;background:#eef4fb;border-radius:14px;opacity:0">💬 12/10 · Pediu orçamento de freios</div>
    <div id="hl2" style="margin-top:12px;font-size:27px;padding:14px 18px;background:#eef4fb;border-radius:14px;opacity:0">📄 13/10 · Orçamento enviado: R$ 1.250</div>
    <div id="hl3" style="margin-top:12px;font-size:27px;padding:14px 18px;background:#eef4fb;border-radius:14px;opacity:0">🔁 15/10 · Retorno automático enviado</div>
    <div id="hl4" style="margin-top:12px;font-size:27px;padding:14px 18px;background:#e3f7ea;border-radius:14px;opacity:0">✅ Agora: "Pode marcar pra segunda?"</div>
  </div>
</div>

<!-- final -->
<div id="end" class="abs" style="left:0;right:0;top:300px;text-align:center;opacity:0">
  <img src="{LOGO}" style="height:118px">
  <div class="h" style="font-size:80px;margin-top:70px">O atendimento é da empresa.<br><span class="blue">Não do celular de ninguém.</span></div>
  <div id="cta" style="display:inline-block;margin-top:70px;background:#0E8DFE;border-radius:999px;padding:30px 56px;font-weight:800;font-size:46px">Teste 30 dias grátis · sem cartão</div>
  <div style="margin-top:34px;font-size:40px;font-weight:700;color:#cfe3ff">🔗 Link na bio</div>
</div>
<div class="disc" id="disc">Imagem ilustrativa, com dados fictícios.</div>
"""

caps = [
 (0.16,1.24,"Sexta-feira."),(1.52,3.84,"Seu melhor atendente pede as contas."),(4.08,5.88,"E com ele vão embora as conversas,"),
 (5.92,6.96,"os orçamentos,"),(7.04,9.44,"os clientes que estavam quase fechando."),(9.48,11.12,"Tudo no celular dele."),
 (11.19,13.60,"No Lomax, o atendimento é da empresa."),(13.64,17.60,"As conversas, o histórico e cada card do funil ficam no sistema."),
 (17.72,21.04,"Você troca o usuário na mesma vaga, sem pagar nada a mais."),(21.07,22.96,"E quem chega já encontra tudo."),
 (23.03,24.32,"Lomax CRM."),(24.44,26.56,"Teste 30 dias grátis, sem cartão."),(26.64,27.36,"Link na bio."),
]

script = "buildCaps(" + json.dumps(caps) + ");" + r"""
function render(t){
  // S1 tela bloqueada
  const l=1-p(t,3.8,4.15); S('lock',{opacity:l,transform:`scale(${lerp(1,1.06,eo(p(t,1.5,3.8)))})`});
  const n=eo(p(t,1.5,1.85)); S('notif',{opacity:n,transform:`translateY(${(1-n)*-60}px)`});
  S('red',{opacity: t<11.2 ? clamp(p(t,1.6,2.2)*(0.6+0.4*Math.sin(t*5))) * (1-p(t,10.8,11.2)) : 0});
  // S2 o que vai embora
  S('gone',{opacity:p(t,4.0,4.3)*(1-p(t,10.9,11.2))});
  slideUp('gtitle',t,4.05,.35,30);
  const T=[5.15,5.95,7.1];
  const suck=eio(p(t,9.5,10.1)), exit=eio(p(t,10.3,10.9));
  [1,2,3].forEach((k,i)=>{const x=eo(p(t,T[i],T[i]+.35));
    const sx=lerp(0,0,suck), sy=lerp(0,880-(420+140*i)+60,suck), sc=lerp(1,.15,suck);
    S('ch'+k,{opacity:x*(1-suck*0.95),transform:`translate(${(1-x)*-60 + exit*620}px,${sy}px) scale(${sc})`});});
  const ph=eo(p(t,9.3,9.6)); S('rph',{opacity:ph,transform:`translateX(${exit*620}px) rotate(${exit*12}deg)`});
  S('door',{opacity:p(t,9.9,10.2)*(1-p(t,10.8,11.0))});
  // S3 Lomax
  S('lom',{opacity:p(t,11.15,11.4)*(1-p(t,17.5,17.75))});
  slideUp('ltitle',t,11.2,.4,30);
  const b=eo(p(t,11.6,12.0)); S('board',{opacity:b,transform:`translateY(${(1-b)*60}px)`});
  const glow=(id,t0)=>{const g=p(t,t0,t0+.25)*(1-p(t,t0+.9,t0+1.3)); S(id,{boxShadow:`0 0 ${50*g}px rgba(14,141,254,${.9*g}), 0 18px 40px rgba(0,0,0,.35)`,transform:`scale(${1+.06*g})`});};
  glow('k1',13.75); glow('k2',14.0); glow('k3',14.6); glow('k4',15.4);
  fade('lockico',t,16.5,null);
  // S4 usuários
  S('users',{opacity:p(t,17.7,17.95)*(1-p(t,20.9,21.15))});
  const sw=eio(p(t,18.5,19.0)); S('uR',{opacity:1-sw,transform:`translateX(${-sw*60}px)`}); S('uB',{opacity:sw,transform:`translateX(${(1-sw)*60}px)`});
  pop('zero',t,19.7,.35,.5);
  // S5 histórico
  S('hist',{opacity:p(t,21.05,21.3)*(1-p(t,22.9,23.1))});
  slideUp('hl1',t,21.3,.25,20); slideUp('hl2',t,21.6,.25,20); slideUp('hl3',t,21.9,.25,20); slideUp('hl4',t,22.2,.25,20);
  // final
  const e=eo(p(t,23.05,23.5)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>24.4?1+0.03*Math.sin((t-24.4)*5):1})`});
  S('disc',{opacity:(t<23)?1:0});
}
"""

if __name__ == "__main__":
    only = None
    if len(sys.argv) > 1:
        only = [int(float(x) * FPS) for x in sys.argv[1:]]
    fdir = render("l5_r3", html(body, script), 28.4, only=only)
    print(fdir)
