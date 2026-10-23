"""Reels do lote 7 (23/10). Legendas com o tempo real de cada palavra da narração.
Uso: python3 reels7.py r1|r2 [render|audio|encode|all] [t1 t2 ... só esses quadros]
"""
import sys, json, re
sys.path.insert(0, "/home/claude/l5")
import reel_lib
from reel_lib import html, render, encode, FPS, ROOT
from mix import mix

A = "/home/claude/l7/audio/"
OUT = "/home/claude/l7/reels/"
LOGO = f"file://{ROOT}/logo_on_dark.png"


def words(r):
    out, inside = [], False
    for x in json.load(open(A + f"{r}_words.json"))["words"]:
        if x["type"] != "word":
            continue
        t = x["text"]
        if t.startswith("["):
            inside = True
        if not inside:
            out.append((x["start"], x["end"], t))
        if t.endswith("]"):
            inside = False
    return out


def phrases(ws, maxw=7):
    def strong(t): return bool(re.search(r'[.?!…]["”]?$', t))
    res, cur = [], []
    for i, w in enumerate(ws):
        cur.append(w)
        t = w[2]
        # palavras até o próximo ponto final
        rest = 0
        for x in ws[i + 1:]:
            rest += 1
            if strong(x[2]):
                break
        if strong(t) or (t.endswith((',', ':')) and len(cur) >= 3 and rest > 2) or (len(cur) >= maxw and rest > 2):
            res.append(cur); cur = []
    if cur:
        res.append(cur)
    q = lambda t: (('“' + t[1:]) if t.startswith('"') else t).replace('"', '”')
    return [dict(a=p[0][0], b=p[-1][1], ws=[[round(s, 3), q(t)] for s, e, t in p]) for p in res]


CAPJS = r"""
function setCaps(list){CAP=list}
"""

EXTRA_CSS = """
.mon{position:absolute;background:#1d2b3f;border-radius:30px;padding:22px}
.scr{height:100%;background:#0b1522;border-radius:16px;position:relative;padding:22px;overflow:hidden}
.pin{display:inline-flex;align-items:center;gap:14px;background:#fff;color:#0A192C;border-radius:999px;padding:16px 30px;font-weight:800;font-size:38px;box-shadow:0 18px 40px rgba(0,0,0,.35)}
.pill{display:inline-block;background:#0E8DFE;color:#fff;padding:0 26px 8px;border-radius:18px;transform:rotate(-2deg)}
.tagA{display:inline-block;background:#e3f0ff;color:#0b6fd0;border-radius:10px;padding:4px 12px;font-size:20px;font-weight:800}
.redchip{display:inline-block;background:#ff4d5e;color:#fff;border-radius:999px;padding:12px 26px;font-weight:800;font-size:34px}
"""


# ------------------------------------------------------------------ R1
def r1():
    body = f"""
<div id="bg" class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C)"></div>
<div id="dawn" class="abs" style="inset:0;background:linear-gradient(180deg,#ff9a5a 0%,#f2685a 30%,#3b2d5a 62%,#0A192C 85%)"></div>
<svg id="mnt" class="abs" style="left:0;top:640px" width="1080" height="560" viewBox="0 0 1080 560">
 <path d="M0 560 L0 380 L120 300 L210 340 L300 180 Q330 120 360 190 L430 330 L520 260 L600 330 L700 120 Q735 40 770 120 L820 230 L900 200 L1080 320 L1080 560 Z" fill="#0d1a2c"/>
 <path d="M0 560 L0 450 L180 420 L340 460 L520 410 L700 450 L880 420 L1080 460 L1080 560 Z" fill="#081322"/>
</svg>
<div id="sun" class="abs" style="left:430px;top:560px;width:220px;height:220px;border-radius:50%;background:radial-gradient(#ffe29a,#ffb35a);box-shadow:0 0 120px #ffb35a"></div>
<div id="t1" class="abs h" style="left:0;right:0;top:250px;text-align:center;font-size:118px">Rio de Janeiro</div>
<div id="t2" class="abs" style="left:0;right:0;top:400px;text-align:center"><span class="pin">🕗 Segunda · 08:00</span></div>

<div id="ph" class="phone" style="left:260px;top:120px;opacity:0">
  <div class="chathead"><div class="av" style="background:#25D366">💬</div><div><div style="font-weight:800;font-size:30px">WhatsApp da oficina</div><div style="font-size:22px;color:#8fa3bd">1 celular</div></div>
  <div id="badge" style="margin-left:auto;background:#ff4d5e;border-radius:999px;padding:6px 16px;font-weight:800;font-size:26px">0</div></div>
  <div id="list" style="padding:16px 18px"></div>
</div>
<div id="q1" class="abs bub in" style="left:120px;top:560px;font-size:44px;font-weight:700;max-width:none;opacity:0;background:#fff;color:#0A192C">“Qual é o valor?”</div>
<div id="q2" class="abs bub in" style="left:420px;top:720px;font-size:44px;font-weight:700;max-width:none;opacity:0;background:#fff;color:#0A192C">“Tá aberto sábado?”</div>
<div id="q3" class="abs bub in" style="left:200px;top:880px;font-size:44px;font-weight:700;max-width:none;opacity:0;background:#fff;color:#0A192C">“Aceita Pix?”</div>

<div id="bal" class="abs" style="inset:0;opacity:0">
  <div class="abs h" style="left:0;right:0;top:250px;text-align:center;font-size:84px">Nasceu no balcão</div>
  <div class="abs h blue" style="left:0;right:0;top:350px;text-align:center;font-size:84px">de um auto center.</div>
  <div id="wrench" class="abs" style="left:0;right:0;top:520px;text-align:center;font-size:190px">🔧</div>
  <div id="loc" class="abs" style="left:0;right:0;top:780px;text-align:center"><span class="pin">📍 Jacarepaguá · RJ</span></div>
  <div id="lg" class="abs" style="left:0;right:0;top:960px;text-align:center"><img src="{LOGO}" style="height:110px"></div>
</div>

<div id="team" class="abs" style="inset:0;opacity:0">
  <div class="abs h" style="left:0;right:0;top:200px;text-align:center;font-size:80px">A equipe toda,<br><span class="blue">no mesmo número.</span></div>
  <div class="mon" style="left:150px;top:470px;width:780px;height:470px"><div class="scr">
     <div style="display:flex;align-items:center;justify-content:space-between"><img src="{LOGO}" style="height:30px"><span id="num" class="chip" style="background:#16253a;color:#9fd0ff">📞 1 número</span></div>
     <div id="a1" class="abs" style="left:60px;top:150px;text-align:center"><div class="av" style="width:120px;height:120px;font-size:52px;margin:auto">A</div><div style="font-size:28px;font-weight:700;margin-top:10px">Ana</div></div>
     <div id="a2" class="abs" style="left:300px;top:150px;text-align:center"><div class="av" style="width:120px;height:120px;font-size:52px;margin:auto;background:#22c55e">P</div><div style="font-size:28px;font-weight:700;margin-top:10px">Paulo</div></div>
     <div id="a3" class="abs" style="left:540px;top:150px;text-align:center"><div class="av" style="width:120px;height:120px;font-size:52px;margin:auto;background:#f59e0b">C</div><div style="font-size:28px;font-weight:700;margin-top:10px">Carla</div></div>
  </div></div>
  <div style="position:absolute;left:470px;top:940px;width:140px;height:60px;background:#1d2b3f"></div>
  <div style="position:absolute;left:380px;top:995px;width:320px;height:20px;border-radius:10px;background:#1d2b3f"></div>
  <div id="pc" class="abs" style="left:0;right:0;top:1060px;text-align:center"><span class="pin">💻 pelo computador</span></div>
</div>

<div id="fun" class="abs" style="inset:0;opacity:0">
  <div class="abs h" style="left:0;right:0;top:200px;text-align:center;font-size:80px">Cada conversa<br><span class="blue">já tem dono.</span></div>
  <div class="mon" style="left:60px;top:450px;width:960px;height:690px"><div class="scr">
    <div class="col" style="left:22px;top:22px;height:620px;width:290px"><div class="colh">Novo</div></div>
    <div id="cw" class="col" style="left:328px;top:22px;height:620px;width:290px"><div class="colh">Esperando</div></div>
    <div class="col" style="left:634px;top:22px;height:620px;width:280px"><div class="colh">Fechado</div></div>
    <div id="k1" class="abs card" style="left:38px;top:100px;width:258px"><b style="font-size:27px">Rafael</b><div style="font-size:21px;color:#4a5a70">Qual é o valor?</div><div id="as1" style="margin-top:10px;opacity:0"><span class="tagA">👤 Paulo</span></div></div>
    <div id="k2" class="abs card" style="left:344px;top:100px;width:258px"><b style="font-size:27px">Juliana</b><div style="font-size:21px;color:#4a5a70">⏳ esperando resposta</div></div>
    <div id="k3" class="abs card" style="left:344px;top:240px;width:258px"><b style="font-size:27px">Bruno</b><div style="font-size:21px;color:#4a5a70">⏳ esperando resposta</div></div>
    <div id="k4" class="abs card" style="left:650px;top:100px;width:248px"><b style="font-size:27px">Helena</b><div style="font-size:21px;color:#4a5a70">✅ agendado</div></div>
  </div></div>
</div>

<div id="end" class="abs" style="left:0;right:0;top:240px;text-align:center;opacity:0">
  <img src="{LOGO}" style="height:118px">
  <div class="h" style="font-size:96px;margin-top:80px">Feito por carioca,</div>
  <div class="h" style="font-size:96px;margin-top:20px"><span class="pill">pra carioca.</span></div>
  <div id="cta" style="display:inline-block;margin-top:80px;background:#0E8DFE;border-radius:999px;padding:30px 56px;font-weight:800;font-size:46px">Teste 30 dias grátis · sem cartão</div>
  <div style="margin-top:34px;font-size:40px;font-weight:700;color:#cfe3ff">🔗 Link na bio</div>
</div>
<div class="disc" id="disc">Cena ilustrativa, com dados fictícios.</div>
"""
    msgs = ["Orçamento de freio?", "Bom dia!!", "Tem horário hoje?", "Quanto fica o óleo?", "Me liga?", "Oi", "Ainda tá aí?", "E aí, conseguiu ver?"]
    script = r"""
const MS=%s;
(function(){const l=$('list');MS.forEach((m,i)=>{const d=document.createElement('div');d.id='m'+i;d.style.cssText='display:flex;align-items:center;gap:16px;padding:16px 8px;border-bottom:1px solid #1f2a3a;opacity:0';
 d.innerHTML=`<div class="av" style="width:56px;height:56px;font-size:24px;background:#2a3b52">${'RJBMDLKS'[i]}</div><div style="flex:1"><div style="font-weight:700;font-size:26px">Cliente ${i+1}</div><div style="font-size:23px;color:#8fa3bd">${m}</div></div><div style="background:#25D366;color:#0A192C;border-radius:999px;width:36px;height:36px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:20px">${1+i%%3}</div>`;l.appendChild(d)})})();
function render(t){
  // S1 amanhecer
  const s1=1-p(t,2.6,2.95);
  S('dawn',{opacity:s1}); S('mnt',{opacity:s1}); S('sun',{opacity:s1,transform:`translateY(${(1-eo(p(t,0,2.4)))*140}px)`});
  slideUp('t1',t,0.1,.45,40); S('t1',{opacity:p(t,0.1,0.5)*s1});
  const t2=pop('t2',t,0.9,.35,.6); S('t2',{opacity:Math.min(t2>0?1:0,s1)});
  // S2 celular lotado
  const ph=p(t,2.75,3.05)*(1-p(t,10.95,11.25)); S('ph',{opacity:ph,transform:`translateX(${t>8.6&&t<10.9?Math.sin(t*60)*6*p(t,8.6,8.8):0}px)`});
  const n=Math.floor(clamp((t-2.9)/0.18,0,8));
  for(let i=0;i<8;i++){S('m'+i,{opacity:t>2.9+i*0.18?1:0})}
  const cnt=t<2.9?0:Math.min(47,Math.floor(3+(t-2.9)*5.5)); S('badge',{text:String(cnt)});
  [['q1',5.1],['q2',6.15],['q3',7.25]].forEach(([id,a])=>{const x=pop(id,t,a,.3,.5); S(id,{opacity:(x>0?1:0)*(1-p(t,10.9,11.2))});});
  // S3 balcão
  S('bal',{opacity:p(t,11.2,11.5)*(1-p(t,16.3,16.55))});
  pop('wrench',t,11.6,.4,.4); S('wrench',{transform:`rotate(${Math.sin(t*3)*12}deg) scale(${lerp(.4,1,back(p(t,11.6,12.0)))})`});
  pop('loc',t,13.3,.35,.6); pop('lg',t,14.8,.4,.6);
  // S4 equipe
  S('team',{opacity:p(t,16.45,16.75)*(1-p(t,19.85,20.1))});
  pop('a1',t,16.95,.3,.4); pop('a2',t,17.3,.3,.4); pop('a3',t,17.6,.3,.4); pop('num',t,18.1,.3,.6); pop('pc',t,19.05,.35,.6);
  // S5 funil
  S('fun',{opacity:p(t,19.95,20.25)*(1-p(t,24.2,24.45))});
  const k=eo(p(t,20.2,20.6)); S('k1',{opacity:k,transform:`translateY(${(1-k)*-80}px)`});
  pop('as1',t,21.55,.3,.5);
  const g=p(t,22.5,22.8)*(1-p(t,23.9,24.2));
  S('cw',{boxShadow:`0 0 ${60*g}px rgba(255,180,60,${.9*g})`,background:g>0?`rgba(${18+60*g},${34+20*g},${56},1)`:'#122238'});
  S('k2',{transform:`scale(${1+.05*g})`}); S('k3',{transform:`scale(${1+.05*g})`});
  // final
  const e=eo(p(t,24.3,24.75)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>28.1?1+0.03*Math.sin((t-28.1)*5):1})`});
  S('disc',{opacity:(t>2.8&&t<24.3)?1:0});
}
""" % json.dumps(msgs)
    sfx = [("whoosh", 2.75, .28), ("ping", 3.1, .3), ("ping", 3.6, .3), ("ping", 4.2, .3), ("ping", 5.12, .35), ("ping", 6.16, .35),
           ("ping", 7.28, .35), ("ping", 8.5, .3), ("ping", 8.7, .3), ("ping", 8.9, .3), ("whoosh", 11.2, .3), ("click", 13.3, .28),
           ("chime", 14.84, .3), ("whoosh", 16.45, .28), ("click", 16.95, .25), ("click", 17.3, .25), ("click", 17.6, .25),
           ("whoosh", 19.95, .28), ("click", 20.3, .25), ("ping", 21.55, .3), ("whoosh", 24.3, .3), ("chime", 25.7, .45)]
    return body, script, 31.6, sfx, "/home/claude/l5/audio/new/mus1.mp3", 0.0, 0.26


# ------------------------------------------------------------------ R2
def r2():
    body = f"""
<div id="bg" class="abs" style="inset:0;background:linear-gradient(#081322,#0A192C)"></div>
<div id="red" class="abs" style="inset:0;background:radial-gradient(circle at 50% 40%,rgba(255,77,94,.35),transparent 60%);opacity:0"></div>

<div id="ad" class="abs" style="left:190px;top:170px;width:700px;opacity:0">
  <div class="card" style="padding:0;overflow:hidden;border-radius:30px">
    <div style="display:flex;align-items:center;gap:16px;padding:22px 26px"><div class="av" style="background:#f59e0b;color:#0A192C">SE</div><div><div style="font-weight:800;font-size:28px">Sua Empresa</div><div style="font-size:22px;color:#6a788c">Patrocinado</div></div></div>
    <div style="height:520px;background:linear-gradient(135deg,#0E8DFE,#0a5bb0);display:flex;align-items:center;justify-content:center;color:#fff;font-weight:900;font-style:italic;font-size:80px;text-align:center;line-height:1">PROMO<br>DA SEMANA</div>
    <div id="btn" style="margin:22px 26px;background:#0E8DFE;color:#fff;border-radius:16px;padding:20px;text-align:center;font-weight:800;font-size:30px">Enviar mensagem</div>
  </div>
</div>
<div id="coin" class="abs" style="left:800px;top:120px;font-size:120px;opacity:0">💸</div>
<div id="tap" class="abs" style="left:520px;top:880px;font-size:120px;opacity:0">👆</div>

<div id="ph" class="phone" style="left:260px;top:120px;opacity:0">
  <div class="chathead"><div class="av">R</div><div><div style="font-weight:800;font-size:30px">Rafael</div><div style="font-size:22px;color:#8fa3bd">veio do anúncio</div></div></div>
  <div id="b1" class="bub in" style="top:170px;opacity:0">Oi, quanto fica?<span class="meta">10:03</span></div>
  <div id="clock" class="abs" style="left:0;right:0;top:420px;text-align:center;opacity:0"><div style="font-size:120px">🕑</div><div id="ctime" class="h" style="font-size:110px;font-style:normal">10:03</div></div>
  <div id="nores" class="abs" style="left:0;right:0;top:760px;text-align:center;opacity:0"><span class="redchip">Sem resposta</span></div>
</div>

<div id="team" class="abs" style="inset:0;opacity:0">
  <div class="abs h" style="left:0;right:0;top:230px;text-align:center;font-size:76px">“Achei que alguém<br>já tinha respondido.”</div>
  <div id="u1" class="abs" style="left:110px;top:560px;text-align:center"><div class="av" style="width:150px;height:150px;font-size:64px;margin:auto">A</div><div style="font-size:60px;margin-top:10px">🤷</div></div>
  <div id="u2" class="abs" style="left:465px;top:560px;text-align:center"><div class="av" style="width:150px;height:150px;font-size:64px;margin:auto;background:#22c55e">P</div><div style="font-size:60px;margin-top:10px">🤷‍♂️</div></div>
  <div id="u3" class="abs" style="left:820px;top:560px;text-align:center"><div class="av" style="width:150px;height:150px;font-size:64px;margin:auto;background:#f59e0b">C</div><div style="font-size:60px;margin-top:10px">🤷‍♀️</div></div>
  <div id="bye" class="abs bub in" style="left:220px;top:900px;font-size:46px;font-weight:700;max-width:none;opacity:0;background:#fff;color:#0A192C">“Já resolvi, obrigado.” 👋</div>
</div>

<div id="prob" class="abs" style="left:80px;right:80px;top:330px;text-align:center;opacity:0">
  <div id="p1" class="h" style="font-size:96px">O problema não<br>é o anúncio.</div>
  <div id="p2" class="h blue" style="font-size:96px;margin-top:60px">É o que acontece<br>depois do “oi”.</div>
</div>

<div id="lom" class="abs" style="inset:0;opacity:0">
  <div class="abs" style="left:0;right:0;top:190px;text-align:center"><img src="{LOGO}" style="height:80px"></div>
  <div class="mon" style="left:60px;top:330px;width:960px;height:800px"><div class="scr">
    <div class="col" style="left:22px;top:22px;height:730px;width:430px"><div class="colh">Novo</div></div>
    <div class="col" style="left:470px;top:22px;height:730px;width:430px"><div class="colh">Em atendimento</div></div>
    <div id="c1" class="abs card" style="left:40px;top:100px;width:394px"><div style="display:flex;justify-content:space-between;align-items:center"><b style="font-size:30px">Rafael</b><span id="ad1" class="tagA">📣 Anúncio</span></div><div style="font-size:24px;color:#4a5a70;margin-top:6px">Oi, quanto fica?</div><div id="as1" style="margin-top:12px;opacity:0"><span class="tagA" style="background:#e1f6e9;color:#1f8a4c">👤 Paulo · agora</span></div></div>
    <div id="c2" class="abs card" style="left:488px;top:330px;width:394px;opacity:0"><b style="font-size:30px">Juliana</b><div style="font-size:24px;color:#4a5a70;margin-top:6px">pediu orçamento e sumiu</div><div id="rt" style="margin-top:12px;opacity:0"><span class="tagA">⏰ retorno automático enviado</span></div><div id="hc" style="margin-top:10px;opacity:0"><span class="tagA" style="background:#fff3d1;color:#9a6500">🕘 terça · 09:00</span></div></div>
  </div></div>
</div>

<div id="end" class="abs" style="left:0;right:0;top:260px;text-align:center;opacity:0">
  <img src="{LOGO}" style="height:118px">
  <div class="h" style="font-size:96px;margin-top:80px">Anúncio bom</div>
  <div class="h" style="font-size:96px;margin-top:20px"><span class="pill">merece resposta.</span></div>
  <div id="cta" style="display:inline-block;margin-top:80px;background:#0E8DFE;border-radius:999px;padding:30px 56px;font-weight:800;font-size:46px">Teste 30 dias grátis · sem cartão</div>
  <div style="margin-top:34px;font-size:40px;font-weight:700;color:#cfe3ff">🔗 Link na bio</div>
</div>
<div class="disc" id="disc">Cena ilustrativa, com dados fictícios.</div>
"""
    script = r"""
function render(t){
  // S1 anúncio
  const a=eo(p(t,0.05,0.45)); S('ad',{opacity:a*(1-p(t,3.1,3.35)),transform:`translateY(${(1-a)*60}px) scale(${t>2.1&&t<2.4?.98:1})`});
  const c=p(t,0.5,1.4); S('coin',{opacity:c>0&&c<1?1:0,transform:`translate(${-c*120}px,${c*500}px) rotate(${c*90}deg)`});
  const tp=p(t,1.9,2.15)*(1-p(t,2.7,2.95)); S('tap',{opacity:tp,transform:`translateY(${(1-p(t,1.9,2.2))*40}px)`});
  S('btn',{background:(t>2.15&&t<2.6)?'#0a5bb0':'#0E8DFE'});
  // S2 celular
  S('ph',{opacity:p(t,3.15,3.4)*(1-p(t,8.95,9.2))});
  slideUp('b1',t,3.36,.3,30);
  S('clock',{opacity:p(t,5.4,5.7)});
  const k=p(t,5.6,7.4); const m=Math.round(3+k*157); const hh=10+Math.floor(m/60), mm=m%60;
  S('ctime',{text:`${hh}:${String(mm).padStart(2,'0')}`});
  pop('nores',t,7.7,.3,.5);
  S('red',{opacity:(t>7.6&&t<13.6)?.7+.3*Math.sin(t*5):0});
  // S3 equipe
  S('team',{opacity:p(t,9.05,9.3)*(1-p(t,13.55,13.8))});
  pop('u1',t,9.3,.3,.4); pop('u2',t,9.7,.3,.4); pop('u3',t,10.1,.3,.4);
  const by=pop('bye',t,12.3,.3,.6); S('bye',{opacity:by>0?1:0});
  // S4 problema
  S('prob',{opacity:p(t,13.75,14.0)*(1-p(t,17.65,17.9))});
  slideUp('p1',t,13.8,.4,40); slideUp('p2',t,15.75,.4,40);
  // S5 Lomax
  S('lom',{opacity:p(t,17.85,18.1)*(1-p(t,27.3,27.55))});
  const e1=eo(p(t,19.2,19.6)), mv=eio(p(t,20.9,21.4));
  S('c1',{opacity:e1,transform:`translate(${mv*448}px,${(1-e1)*-80}px)`});
  pop('as1',t,20.95,.3,.5);
  const g=p(t,22.2,22.45)*(1-p(t,23.6,23.9)); S('ad1',{transform:`scale(${1+.35*g})`,boxShadow:`0 0 ${30*g}px rgba(14,141,254,${g})`});
  slideUp('c2',t,23.9,.35,40); pop('rt',t,25.2,.3,.5); pop('hc',t,26.3,.3,.5);
  // final
  const e=eo(p(t,27.45,27.9)); S('end',{opacity:e,transform:`translateY(${(1-e)*50}px)`});
  S('cta',{transform:`scale(${t>30.9?1+0.03*Math.sin((t-30.9)*5):1})`});
  S('disc',{opacity:(t>3.1&&t<27.4)?1:0});
}
"""
    sfx = [("whoosh", 0.05, .28), ("click", 2.16, .3), ("ping", 3.36, .38), ("whoosh", 5.4, .25), ("off", 7.7, .4),
           ("whoosh", 9.05, .28), ("click", 9.3, .22), ("click", 9.7, .22), ("click", 10.1, .22), ("ping", 12.3, .35),
           ("whoosh", 13.75, .3), ("whoosh", 15.75, .25), ("whoosh", 17.85, .3), ("ping", 19.3, .35), ("whoosh", 20.9, .25),
           ("click", 22.3, .25), ("ping", 25.2, .35), ("click", 26.3, .22), ("whoosh", 27.45, .3), ("chime", 28.8, .45)]
    return body, script, 34.0, sfx, "/home/claude/l5/audio/new/gus_music.mp3", 0.0, 0.24


LAYOUT = {
    "r1": ["Rio de Janeiro,", "segunda-feira, oito da manhã.", "O WhatsApp da oficina já tá lotado.", "Qual é o valor?",
           "Tá aberto sábado?", "Aceita Pix?", "E só tem um celular", "pra responder tudo.", "Foi assim, no balcão",
           "de um auto center em Jacarepaguá,", "que nasceu o Lomax CRM.", "Agora a equipe toda atende",
           "no mesmo número, pelo computador.", "Cada conversa nova", "já cai com um atendente,", "e o funil mostra quem tá esperando.",
           "Lomax CRM.", "Feito por carioca,", "pra carioca.", "Teste trinta dias grátis.", "Link na bio."],
}


def layout(r, ws):
    if r not in LAYOUT:
        return phrases(ws)
    q = lambda t: (('“' + t[1:]) if t.startswith('"') else t).replace('"', '”')
    res, i = [], 0
    for txt in LAYOUT[r]:
        n = len(txt.split()); p = ws[i:i + n]; i += n
        res.append(dict(a=p[0][0], b=p[-1][1], ws=[[round(s, 3), q(t)] for s, e, t in p]))
    assert i == len(ws), (i, len(ws))
    return res


def main():
    r = sys.argv[1]
    st = sys.argv[2] if len(sys.argv) > 2 else "all"
    body, script, dur, sfx, music, ms, mv = {"r1": r1, "r2": r2}[r]()
    caps = layout(r, words(r))
    for c in caps:
        print(f"  {c['a']:.2f}-{c['b']:.2f}  {' '.join(w[1] for w in c['ws'])}")
    import os; os.makedirs(OUT, exist_ok=True)
    full = "setCaps(" + json.dumps(caps) + ");" + script
    page = html(body, CAPJS + full, EXTRA_CSS)
    steps = ["audio", "render", "encode"] if st == "all" else [st]
    if "audio" in steps:
        mix(OUT + f"l7_{r}_audio.wav", dur, [(A + f"{r}_voz.mp3", 0.0)], music, music_start=ms, music_vol=mv, sfx=sfx)
    if "render" in steps:
        only = [int(float(x) * FPS) for x in sys.argv[3:]] or None
        print(render(f"l7_{r}", page, dur, outdir=OUT, only=only))
    if "encode" in steps:
        encode(f"l7_{r}", OUT + f"l7_{r}_frames", OUT + f"l7_{r}_audio.wav", OUT + f"l7_{r}.mp4")
        print(OUT + f"l7_{r}.mp4")


if __name__ == "__main__":
    main()
