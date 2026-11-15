"""Lote 13b (15/11): tutorial "Conectar o WhatsApp pelo celular, com código".
Prints reais do projeto de testes (empresa fictícia Oficina do Carlos), feitos pelo Code em 15/11 (2026-11/telas-conexao).
CPF fictício borrado mesmo assim. Textos dos botões exatamente como na tela."""
import sys, os
F = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for d in ("lote5", "lote7", "lote8", "lote9", "lote10", "lote11"):
    sys.path.insert(0, os.path.join(F, d))
from base import *
from c17 import css, cover
from c7 import cta
import stories as st

CX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(F), "2026-11/telas-conexao/recortes")
def img(k): return f"file://{CX}/{k}.png"
css2 = css + """
.stp{position:absolute;top:290px;left:96px;right:96px;display:flex;gap:26px;align-items:flex-start}
.stp .n{flex:none;width:84px;height:84px;border-radius:22px;background:#0E8DFE;color:#fff;font-size:50px;font-weight:900;font-style:italic;display:flex;align-items:center;justify-content:center}
.stp .t{font-size:50px;font-weight:800;line-height:1.12;letter-spacing:-.5px}
.stp .t b{color:#0E8DFE}
.ph{position:absolute;left:50%;transform:translateX(-50%);border-radius:40px;overflow:hidden;border:10px solid #0A192C;background:#fff;box-shadow:0 30px 70px rgba(10,25,44,.25)}
.ph img{display:block;width:100%}
.nt{position:absolute;right:96px;bottom:118px;font-size:22px;color:#6a788c;text-align:right}
.cd{position:absolute;left:50%;transform:translateX(-50%);border-radius:28px;overflow:hidden;border:4px solid #d5e2f2;background:#fff;box-shadow:0 24px 60px rgba(10,25,44,.16)}
.cd img{display:block;width:100%}
"""
N = 8
def step(name, n, title, k, w=820, top=520, h=None, phone=False, note="Telas reais do Lomax, com dados fictícios."):
    hh = f"height:{h}px;" if h else ""
    cls = "ph" if phone else "cd"
    return (name, page(f"""<div class="s light">{STRIPES}<div class="count">{n+1}/{N}</div>
<div class="stp"><div class="n">{n}</div><div class="t">{title}</div></div>
<div class="{cls}" style="top:{top}px;width:{w}px;{hh}"><img src="{img(k)}"></div>
<div class="nt">{note}</div>{logo(False)}</div>""", css2))

S = [cover("l13_c3_1", "Sem computador.", "Sem QR Code.", "Só um código.", "Conecta o WhatsApp no Lomax pelo celular. Salva o passo a passo. 📌", size=100)]
S.append(step("l13_c3_2", 1, "Cria a conta <b>pelo celular</b>.<br>São 3 passos.", "s1", w=380, h=600, top=470, phone=True))
S.append(step("l13_c3_3", 2, "Toca em <b>Conectar pelo código</b>.", "t1", top=560))
S.append(step("l13_c3_4", 3, "Digita o número e toca em <b>Gerar código</b>.", "t2", top=520))
S.append(step("l13_c3_5", 4, "O Lomax mostra o <b>código</b>. Deixa a tela aberta.", "t4", w=640, h=560, top=520))
S.append(step("l13_c3_6", 5, "No WhatsApp: <b>Aparelhos conectados</b> › <b>Conectar um aparelho</b> › <b>Conectar com número de telefone</b>. Digita o código.", "t3", w=640, top=620))
S.append(step("l13_c3_7", 6, "Pronto: <b>conectado</b>. E as conversas recentes chegam junto.", "t6", w=760, top=530))
S.append(("l13_c3_8", page(cta("Cadastrou e não conectou?", "Faz agora pelo celular.",
    "Travou em algum passo? A gente ajuda pelo WhatsApp ou por vídeo, sem custo.", top=200), css)))

# Guia rápido 1080x1920: story + imagem para mandar a quem se cadastrou e não conectou
G = st.CSS + """
.gr{position:absolute;left:84px;right:84px;display:flex;gap:28px;align-items:center;background:#fff;border-radius:34px;padding:26px 28px;box-shadow:0 18px 40px rgba(10,25,44,.10)}
.gr .n{flex:none;width:76px;height:76px;border-radius:20px;background:#0E8DFE;color:#fff;font-size:44px;font-weight:900;font-style:italic;display:flex;align-items:center;justify-content:center}
.gr p{flex:1;font-size:33px;line-height:1.22;font-weight:600;color:#0A192C}
.gr p b{color:#0b6fd0}
.gr img{flex:none;width:230px;max-height:170px;object-fit:cover;object-position:top;border-radius:16px;border:3px solid #e6edf6}
"""
rows = [("No Lomax, toca em <b>Conectar pelo código</b>.", "t1"),
        ("Digita o número e toca em <b>Gerar código</b>.", "t2"),
        ("No WhatsApp: <b>Aparelhos conectados</b> › <b>Conectar um aparelho</b> › <b>Conectar com número de telefone</b>.", "t3"),
        ("Digita o código. <b>Pronto: conectado.</b>", "t4")]
tops = [500, 740, 980, 1240]
body = st.headline("Conecta pelo celular", "em 4 toques.", top=230, size=98)
for i, ((t, k), y) in enumerate(zip(rows, tops)):
    body += f"<div class='gr' style='top:{y}px'><div class='n'>{i+1}</div><p>{t}</p><img src='{img(k)}'></div>"
body += "<div class='sub' style='position:absolute;left:84px;right:84px;top:1480px;margin:0;font-size:34px'>Travou? A gente ajuda pelo WhatsApp ou por vídeo.</div>"
css_story = BASE_CSS.replace("width:1080px;height:1350px", "width:1080px;height:1920px")
ST = [("ls_50_guia_celular", f"<!doctype html><html><head><meta charset='utf-8'><style>{css_story}{G}</style></head><body><div class='st light'><div class='dots'></div>{body}{st.logo()}</div></body></html>")]

if __name__ == "__main__":
    out = "/home/claude/l5/out13b"
    render_pngs(S, out)
    render_pngs(ST, out, w=st.W, h=st.H)
    print(len(S), len(ST))
