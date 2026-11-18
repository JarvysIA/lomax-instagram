import sys, os
sys.path.insert(0,'/home/claude/lomax-instagram/ferramentas/lote5')
from base import font_faces, ROOT
from playwright.sync_api import sync_playwright
CSS=font_faces()+"""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:transparent;font-family:Barlow}
.t{position:absolute;left:70px;right:70px;top:110px;text-align:center;color:#fff;font-weight:900;font-style:italic;font-size:96px;line-height:1.02;letter-spacing:-2px}
.p{display:inline-block;background:#0E8DFE;border-radius:22px;padding:2px 26px 12px;transform:rotate(-1.5deg);margin-top:10px}
.end{position:absolute;inset:0;background:#0A192C;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center}
.end .a{font-weight:900;font-style:italic;font-size:96px;line-height:1.02;letter-spacing:-2px}
.end .b{font-size:46px;margin-top:40px;color:#c9d6e8;line-height:1.35}
.end .c{margin-top:60px;background:#0E8DFE;border-radius:999px;padding:26px 60px;font-size:50px;font-weight:800}
.end img{height:70px;margin-top:90px}
"""
def h(body): return f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>"
def title(a,b): return h(f"<div class=t>{a}<br><span class=p>{b}</span></div>")
def end(a,b,c,d): return h(f"<div class=end><div class=a>{a}<br><span style='color:#0E8DFE'>{b}</span></div><div class=b>{c}</div><div class=c>{d}</div><img src='file://{ROOT}/logo_on_dark.png'></div>")
def render(items,out):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
        for n,html in items:
            fp=os.path.abspath(f'{out}/{n}.html'); open(fp,'w').write(html); pg.goto('file://'+fp); pg.wait_for_timeout(400); pg.evaluate("document.fonts.ready")
            pg.screenshot(path=f"{out}/{n}.png",omit_background=True)
        b.close()
if __name__=="__main__":
    render([("t1",title("22h10.","A oficina fechou.")),("t2",title("O cliente pediu","orçamento.")),("t3",title("A IA respondeu","sozinha.")),
            ("end",end("Atende até","de madrugada.","Agente de IA do Lomax<br>30 dias grátis, com tudo incluso","Link na bio"))],"ov1")
