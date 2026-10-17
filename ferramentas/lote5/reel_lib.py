"""Mini motor de Reels: HTML com render(t), captura quadro a quadro e monta com áudio."""
import os, json, subprocess, shutil
from base import font_faces, ROOT

W, H, FPS = 1080, 1920, 30

CSS = font_faces() + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#0A192C}
body{font-family:'Barlow',sans-serif;color:#fff;-webkit-font-smoothing:antialiased}
#stage{position:absolute;inset:0;overflow:hidden}
.abs{position:absolute}
.h{font-weight:900;font-style:italic;letter-spacing:-1.5px;line-height:1}
.blue{color:#0E8DFE}
#cap{position:absolute;left:70px;right:70px;top:1250px;text-align:center;font-weight:800;font-size:60px;line-height:1.18;letter-spacing:-.5px;text-shadow:0 4px 18px rgba(0,0,0,.55)}
#cap span{display:inline-block;margin:0 7px;transition:none;opacity:.35}
#cap span.on{opacity:1}
#cap span.now{color:#fff;background:#0E8DFE;border-radius:12px;padding:0 10px;margin:0 2px;text-shadow:none}
.disc{position:absolute;left:0;right:0;top:1500px;text-align:center;font-size:22px;color:rgba(255,255,255,.45)}
.phone{position:absolute;width:560px;height:1060px;border-radius:64px;background:#0d1117;border:10px solid #1f2a3a;box-shadow:0 40px 90px rgba(0,0,0,.55);overflow:hidden}
.chathead{height:120px;background:#16253a;display:flex;align-items:center;gap:18px;padding:30px 28px 0}
.av{width:62px;height:62px;border-radius:50%;background:#0E8DFE;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px;flex:none}
.bub{position:absolute;max-width:420px;padding:18px 22px;border-radius:24px;font-size:30px;line-height:1.25;font-weight:500}
.in{background:#1e2c40;border-top-left-radius:6px;left:24px}
.out{background:#0E8DFE;border-top-right-radius:6px;right:24px}
.meta{display:block;font-size:20px;opacity:.7;margin-top:6px;text-align:right}
.card{background:#fff;color:#0A192C;border-radius:22px;padding:22px 24px;box-shadow:0 18px 40px rgba(0,0,0,.35)}
.col{position:absolute;top:0;width:300px;border-radius:24px;background:#122238;padding:18px}
.colh{font-weight:800;font-size:26px;letter-spacing:1px;text-transform:uppercase;color:#8fa3bd;margin-bottom:16px}
.chip{display:inline-block;padding:8px 16px;border-radius:999px;font-weight:700;font-size:22px}
"""

JS = r"""
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const lerp=(a,b,x)=>a+(b-a)*x;
const p=(t,a,b)=>clamp((t-a)/(b-a));
const eo=x=>1-Math.pow(1-x,3);
const ei=x=>x*x*x;
const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const back=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
const $=id=>document.getElementById(id);
function S(id,o){const e=typeof id==='string'?$(id):id; if(!e)return; for(const k in o){ if(k==='text'){e.textContent=o[k]} else if(k==='html'){e.innerHTML=o[k]} else e.style[k]=o[k];}}
function pop(id,t,t0,d=.35,from=.6){const x=p(t,t0,t0+d);S(id,{opacity:x>0?1:0,transform:`scale(${lerp(from,1,back(x))})`});return x}
function fade(id,t,a,b,d=.3){let o=p(t,a,a+d); if(b!=null) o=Math.min(o,1-p(t,b,b+d)); S(id,{opacity:o}); return o}
function slideUp(id,t,t0,d=.45,dist=80){const x=eo(p(t,t0,t0+d));S(id,{opacity:x,transform:`translateY(${(1-x)*dist}px)`});return x}
// legendas palavra a palavra
let CAP=[];
function buildCaps(list){CAP=list.map(([a,b,txt])=>{const w=txt.split(' ');const n=w.length;const ws=w.map((s,i)=>[a+(b-a)*i/n,s]);return {a,b,ws}})}
let lastCap=-1;
function caps(t){const c=$('cap'); let idx=-1; for(let i=0;i<CAP.length;i++){ if(t>=CAP[i].a-0.05 && t<(CAP[i+1]?Math.min(CAP[i+1].a-0.05,CAP[i].b+0.6):CAP[i].b+0.8)) idx=i;}
 if(idx<0){c.innerHTML='';lastCap=-1;return}
 const ph=CAP[idx]; if(idx!==lastCap){c.innerHTML=ph.ws.map(w=>`<span>${w[1]}</span>`).join(' ');lastCap=idx}
 const sp=c.querySelectorAll('span'); let cur=-1; ph.ws.forEach((w,i)=>{if(t>=w[0])cur=i});
 sp.forEach((s,i)=>{s.className=i<cur?'on':(i===cur?'on now':'')});
 const x=eo(p(t,ph.a-0.05,ph.a+0.15)); c.style.transform=`translateY(${(1-x)*20}px)`; c.style.opacity=x;}
"""

def html(body, script, extra_css=""):
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra_css}</style></head>
<body><div id="stage">{body}</div><div id="cap"></div><script>{JS}
{script}
</script></body></html>"""

def render(name, page_html, duration, outdir="/home/claude/l5/reels", fps=FPS, only=None, expr="render({t:.4f}); caps({t:.4f})"):
    from playwright.sync_api import sync_playwright
    fdir = os.path.join(outdir, name + "_frames")
    shutil.rmtree(fdir, ignore_errors=True); os.makedirs(fdir)
    path = os.path.join(outdir, name + ".html"); open(path, "w").write(page_html)
    n = int(duration * fps)
    frames = only if only is not None else range(n)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto("file://" + path); pg.wait_for_timeout(400); pg.evaluate("document.fonts.ready")
        for i in frames:
            t = i / fps
            pg.evaluate(expr.format(t=t))
            pg.screenshot(path=os.path.join(fdir, f"f{i:05d}.jpg"), type="jpeg", quality=88)
        b.close()
    return fdir

def encode(name, fdir, audio, out, fps=FPS):
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-framerate", str(fps), "-i", os.path.join(fdir, "f%05d.jpg"),
           "-i", audio, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "20", "-preset", "medium",
           "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
