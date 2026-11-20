"""Lote 14 (20/11): feed e stories com TELAS REAIS das gravações do Code (empresas de teste, dados fictícios).
Carrosséis l14_c1 (um dia no Lomax) e l14_c2 (o que o agente de IA faz e o que ainda não faz), posts únicos l14_s1..s9, stories ls_51..ls_57."""
import sys, os
F = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(F, "lote5"))
from base import render_pngs, page, BLUE, NAVY, ROOT
from PIL import Image
FR = "/home/claude/l14/fr/"; CR = "/home/claude/l14/crops/"; os.makedirs(CR, exist_ok=True)
NOTE = "Tela real do Lomax · empresa de teste, dados fictícios"

def crop(name, src, y0, y1, x0=0, x1=1170):
    p = f"{CR}{name}.png"; Image.open(FR + src + ".png").crop((x0, y0, x1, y1)).save(p); return p

CSS = f"""
.s{{padding:0}}
.hd{{position:absolute;left:80px;right:80px;top:84px;text-align:center}}
.k{{display:inline-block;font-weight:800;font-size:30px;letter-spacing:2px;color:{BLUE};margin-bottom:18px;text-transform:uppercase}}
.h1{{font-weight:900;font-style:italic;font-size:80px;letter-spacing:-2px;line-height:1.02;color:#fff}}
.pl{{display:inline-block;background:{BLUE};border-radius:20px;padding:0 24px 10px;transform:rotate(-1.5deg);margin-top:8px}}
.shot{{position:absolute;left:50%;transform:translateX(-50%);border-radius:30px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.45);border:6px solid #1d3352;background:#fff}}
.shot img{{display:block;width:100%}}
.lab{{position:absolute;left:0;right:0;text-align:center;font-weight:800;font-size:30px;color:#c9d6e8}}
.lg{{position:absolute;left:80px;bottom:46px;height:44px}}
.nt{{position:absolute;right:80px;bottom:52px;font-size:20px;color:#7d8fa8}}
.cn{{position:absolute;right:80px;top:40px;font-size:24px;font-weight:600;color:#7d8fa8}}
.big{{font-weight:900;font-style:italic;letter-spacing:-2px;line-height:1.02}}
.ls{{font-size:38px;line-height:1.4;color:#d7e0ec}}
.li{{display:flex;gap:22px;align-items:flex-start;margin-top:44px;font-size:46px;line-height:1.3;color:#fff;text-align:left}}
.li b{{color:{BLUE}}}
.ic{{flex:none;width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:34px}}
"""
def frame(inner, n=None, N=None, note=True):
    c = f"<div class=cn>{n}/{N}</div>" if n else ""
    return page(f"<div class='s dark'>{inner}{c}<img class=lg src='file://{ROOT}/logo_on_dark.png'>" + (f"<div class=nt>{NOTE}</div>" if note else "") + "</div>", CSS)

def head(a, b, k=""):
    kk = f"<div class=k>{k}</div><br>" if k else ""
    return f"<div class=hd>{kk}<div class=h1>{a}<br><span class=pl>{b}</span></div></div>"

def shot(path, top, maxw=900, maxh=None, srcw=None, srch=None):
    im = Image.open(path); w, h = im.size
    if maxh is None: maxh = 1250 - top
    s = min(maxw / w, maxh / h); W = int(w * s)
    return f"<div class=shot style='top:{top}px;width:{W}px'><img src='file://{path}'></div>"

def post(name, a, b, img, k="", n=None, N=None, top=None):
    t = top or (370 if k else 320)
    return (name, frame(head(a, b, k) + shot(img, t), n, N))

def stack(name, a, b, imgs, labels):
    # dois prints um embaixo do outro, com rótulo
    top = 320; inner = head(a, b); y = top; avail = 1250 - top - 50 * len(imgs)
    sizes = [Image.open(p).size for p in imgs]; tot = sum(h for w, h in sizes)
    s = min(760 / 1170, avail / tot)
    for p, l, (w, h) in zip(imgs, labels, sizes):
        inner += f"<div class=lab style='top:{y}px'>{l}</div>"; y += 46
        inner += f"<div class=shot style='top:{y}px;width:{int(w*s)}px;border-radius:22px'><img src='file://{p}'></div>"; y += int(h * s) + 16
    return (name, frame(inner))

# ---------- recortes ----------
C = dict(
 madr=crop("madr", "madr", 430, 2225), audio=crop("audio", "audio", 860, 2215), ficha=crop("ficha", "ficha", 140, 1960),
 anuncio_ia=crop("anuncio_ia", "anuncio_ia", 380, 2100), rodizio=crop("rodizio", "rodizio", 120, 1800),
 retorno=crop("retorno", "retorno", 120, 2000), jul=crop("jul", "jul", 640, 1130), carlos=crop("carlos", "carlos", 640, 1560),
 barra=crop("barra", "barra", 330, 2532), conf=crop("conf", "conf", 300, 2240), transf=crop("transf", "transf", 120, 2040),
 loja=crop("loja", "loja", 380, 1850), clinica=crop("clinica", "clinica", 380, 1720), audio_longo=crop("audio_longo", "audio_longo", 330, 2190),
 codigo=crop("codigo", "codigo", 100, 1300))

FEED = []
# ---------- carrossel 1: um dia no Lomax ----------
N = 8
FEED += [
 ("l14_c1_1", frame("""<div class=hd style='top:250px'><div class=k>GRAVAÇÕES REAIS DO SISTEMA</div><br>
 <div class=big style='font-size:120px;color:#fff'>Um dia<br>no Lomax.</div><br><span class='h1'><span class=pl>Hora a hora.</span></span>
 <div class=ls style='margin-top:70px'>O que o sistema faz sozinho, da madrugada à noite.<br>Arrasta. 👉</div></div>""", 1, N)),
 post("l14_c1_2", "3 mensagens.", "1 resposta da IA.", C["madr"], "03h10 · oficina fechada", 2, N),
 post("l14_c1_3", "3 clientes,", "3 atendentes.", C["rodizio"], "11h27 · rodízio automático", 3, N),
 post("l14_c1_4", "Pediu orçamento e sumiu?", "O retorno saiu sozinho.", C["retorno"], "11h31 · retorno automático", 4, N),
 post("l14_c1_5", "Mandou áudio?", "Transcrito e respondido.", C["audio"], "16h00 · áudio", 5, N),
 post("l14_c1_6", "Respondeu 1.", "Confirmado.", C["conf"], "17h48 · confirmação na véspera", 6, N),
 post("l14_c1_7", "Lead do anúncio.", "Respondido na hora.", C["anuncio_ia"], "23h00 · anúncio", 7, N),
 ("l14_c1_8", frame("""<div class=hd style='top:300px'><div class=big style='font-size:100px;color:#fff'>Tudo isso<br>com a equipe<br><span class=pl style='font-size:100px'>dormindo.</span></div>
 <div class=ls style='margin-top:70px'>Teste 30 dias grátis, sem cartão,<br>com o agente de IA incluso.</div>
 <div style='margin-top:60px'><span style='display:inline-block;background:#0E8DFE;color:#fff;border-radius:999px;padding:24px 56px;font-size:44px;font-weight:800'>Link na bio</span></div></div>""", 8, N, note=False)),
]
# ---------- carrossel 2: o que o agente faz e o que ainda não faz ----------
N = 7
FEED += [
 ("l14_c2_1", frame("""<div class=hd style='top:250px'><div class=k>AGENTE DE IA DO LOMAX</div><br>
 <div class=big style='font-size:104px;color:#fff'>O que ele faz.</div><br><span class='h1' style='font-size:92px'><span class=pl>E o que ainda não faz.</span></span>
 <div class=ls style='margin-top:70px'>Sem promessa. Com tela real.<br>Arrasta. 👉</div></div>""", 1, N, note=False)),
 post("l14_c2_2", "Responde sozinho,", "com a sua tabela.", C["clinica"], "faz", 2, N),
 post("l14_c2_3", "Manda o orçamento", "no seu modelo.", C["loja"], "faz", 3, N),
 post("l14_c2_4", "Entende áudio.", "E responde.", C["audio"], "faz", 4, N),
 post("l14_c2_5", "3 mensagens seguidas?", "Uma resposta só.", C["madr"], "faz", 5, N),
 ("l14_c2_6", frame("""<div class=hd style='top:170px'><div class=k>O QUE ELE AINDA NÃO FAZ</div></div>
 <div style='position:absolute;left:110px;right:110px;top:300px'>
 <div class=li><div class=ic style='background:#2a3c57;color:#fff'>✕</div><div>Não marca horário na agenda.</div></div>
 <div class=li><div class=ic style='background:#2a3c57;color:#fff'>✕</div><div>Não move o card no funil.</div></div>
 <div class=li><div class=ic style='background:#0E8DFE;color:#fff'>?</div><div>Quando não sabe a resposta, <b>não inventa</b>: não manda nada e a conversa fica para a sua equipe.</div></div>
 <div class=li><div class=ic style='background:#0E8DFE;color:#fff'>⏻</div><div>Você escolhe quando ele atende: <b>só fora do horário</b> ou o dia todo.</div></div>
 </div>""", 6, N, note=False)),
 ("l14_c2_7", frame("""<div class=hd style='top:250px'><div class=k>QUANTO CUSTA</div><br>
 <div class=big style='font-size:150px;color:#0E8DFE'>R$ 69,90</div><div class=ls style='font-size:44px;color:#fff;font-weight:700'>por mês, com 3.000 respostas</div>
 <div class=ls style='margin-top:30px'>Acabou? Recarga de 1.000 respostas por R$ 19,90.<br>Com o CRM (2 usuários): R$ 169,80 por mês.</div>
 <div class=ls style='margin-top:50px;color:#fff;font-weight:700'>No teste de 30 dias grátis, ele vem incluso.</div>
 <div style='margin-top:50px'><span style='display:inline-block;background:#0E8DFE;color:#fff;border-radius:999px;padding:24px 56px;font-size:44px;font-weight:800'>Link na bio</span></div></div>""", 7, N, note=False)),
]
# ---------- posts únicos ----------
FEED += [
 post("l14_s1_madrugada", "3 mensagens às 03h10.", "1 resposta da IA.", C["madr"]),
 post("l14_s2_audio", "Mandou áudio?", "Já tem resposta.", C["audio"]),
 post("l14_s3_ficha", "Veio do anúncio?", "Tá escrito no card.", C["ficha"]),
 post("l14_s4_rodizio", "3 leads. 3 atendentes.", "Zero discussão.", C["rodizio"]),
 post("l14_s5_retorno", "O cliente sumiu.", "O retorno não.", C["retorno"]),
 stack("l14_s6_perfis", "A atendente vê o dela.", "O dono vê tudo.", [C["jul"], C["carlos"]], ["No celular da Juliana (atendente)", "No celular do Carlos (dono)"]),
 post("l14_s7_confirmacao", "Respondeu 1?", "Confirmado. Sozinho.", C["conf"]),
 post("l14_s8_transferencia", "Passou a conversa?", "O histórico foi junto.", C["transf"]),
 post("l14_s9_audio_longo", "Áudio de 1 minuto?", "Lê em vez de ouvir.", C["audio_longo"]),
]

# ---------- stories ----------
SCSS = CSS + """
html,body{width:1080px;height:1920px}.s{height:1920px}
.q{font-weight:900;font-style:italic;font-size:92px;letter-spacing:-2px;line-height:1.02;color:#fff;text-align:center}
.ans{display:inline-block;font-weight:900;font-style:italic;font-size:170px;letter-spacing:-5px;color:#0E8DFE;line-height:1}
.ld{font-size:42px;line-height:1.35;text-align:center;color:#d7e0ec}
.tg{display:inline-block;background:#0E8DFE;color:#fff;font-size:28px;letter-spacing:3px;padding:12px 26px;border-radius:14px;font-weight:800}
.lgS{position:absolute;left:0;right:0;bottom:260px;text-align:center}.lgS img{height:58px}
.ntS{position:absolute;left:0;right:0;bottom:220px;text-align:center;font-size:21px;color:#7d8fa8}
"""
def story(name, q, a, txt, img=None, imgh=420):
    sh = ""
    if img:
        im = Image.open(img); w, h = im.size; s = min(760 / w, imgh / h)
        sh = f"<div class=shot style='top:1080px;width:{int(w*s)}px'><img src='file://{img}'></div>"
    top_ans = 640 if img else 820; top_txt = 860 if img else 1090
    body = f"""<div style='position:absolute;left:84px;right:84px;top:250px;text-align:center'><span class=tg>DÚVIDA FREQUENTE</span><div class=q style='margin-top:46px'>{q}</div></div>
    <div style='position:absolute;left:0;right:0;top:{top_ans}px;text-align:center'><span class=ans style='font-size:{170 if len(a)<=9 else 128}px'>{a}</span></div>
    <div class=ld style='position:absolute;left:110px;right:110px;top:{top_txt}px'>{txt}</div>{sh}
    <div class=lgS><img src='file://{ROOT}/logo_on_dark.png'></div>""" + (f"<div class=ntS>{NOTE}</div>" if img else "")
    return (name, f"<!doctype html><html><head><meta charset='utf-8'><style>{page('', SCSS).split('<style>')[1].split('</style>')[0]}</style></head><body><div class='s dark'>{body}</div></body></html>")

ST = [
 story("ls_51_tabela", "A IA inventa preço?", "Não.", "Ela responde com a tabela e o modelo de orçamento da sua empresa.", crop("st_clinica", "clinica", 600, 1720)),
 story("ls_52_audio", "Entende áudio?", "Entende.", "O áudio vira texto na conversa e o agente responde.", crop("st_audio", "audio", 860, 2215)),
 story("ls_53_nao_sabe", "E quando ela não sabe?", "Fica com você.", "Ela não inventa e não manda nada: a conversa fica para a sua equipe responder."),
 story("ls_54_horario", "Só de madrugada?", "Você escolhe.", "O agente atende só fora do horário ou o dia todo. Quem decide é você."),
 story("ls_55_tres", "Cliente mandou 3 mensagens seguidas?", "1 resposta.", "O agente junta tudo e responde uma vez só.", crop("st_madr", "madr", 430, 2225)),
 story("ls_56_recarga", "Acabaram as 3.000 respostas?", "R$ 19,90", "Recarga de mais 1.000 respostas do agente de IA."),
 story("ls_57_teste", "O teste grátis inclui a IA?", "Inclui.", "30 dias grátis, sem cartão, com o agente de IA incluso."),
]

if __name__ == "__main__":
    out = "/home/claude/lomax-instagram/2026-11/lote14"
    render_pngs(FEED, out); render_pngs(ST, "/home/claude/lomax-instagram/2026-11/stories7", w=1080, h=1920)
    print(len(FEED), len(ST))
