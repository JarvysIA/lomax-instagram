"""Lote 13 (14/11): lançamento do agente de IA do Lomax (liberado pelo Luiz em 14/11 20h12).
Só o que o Luiz confirmou: disponível para todos; responde e manda orçamento; atende de madrugada; entende áudio.
NÃO agenda nem move card (ainda). Preço: R$ 69,90/mês com 3.000 respostas + recarga de 1.000 por R$ 19,90.
Print real da Star (14/11 20h06) com nome e foto do cliente borrados (autorizado pelo Luiz)."""
import sys, os
F = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for d in ("lote5", "lote7", "lote8", "lote9", "lote10", "lote11"):
    sys.path.insert(0, os.path.join(F, d))
from base import *
from c17 import css, dark, lm, cover
from c7 import cta
import stories as st
from c9 import single

PRINT = f"file://{F}/lote5/print_ia.png"
css2 = css + """
.phone{position:absolute;left:96px;top:300px;width:452px;border-radius:38px;overflow:hidden;border:10px solid #22344d;box-shadow:0 30px 70px rgba(0,0,0,.45)}
.phone img{display:block;width:100%}
.side{position:absolute;left:600px;right:80px;top:330px}
.side .st2{margin-bottom:40px}
.side .k{font-size:24px;font-weight:800;letter-spacing:2px;color:#7fc0ff}
.side p{font-size:34px;line-height:1.28;font-weight:600;margin-top:6px}
"""
N = 5
S = [cover("l13_c1_1", "20h06 de sábado.", "Ninguém da equipe", "digitou nada.", "E o orçamento saiu na hora. Arrasta. 👉", size=96)]
S.append(("l13_c1_2", page(f"""<div class="s dark"><div class="count">2/{N}</div>
<div class="h" style="position:absolute;top:150px;left:96px;right:96px;font-size:60px">Conversa real, <span class="blue">desta noite:</span></div>
<div class="phone"><img src="{PRINT}"></div>
<div class="side">
<div class="st2"><div class="k">20H02</div><p>O cliente pede o orçamento.</p></div>
<div class="st2"><div class="k">20H06</div><p>O <b>agente de IA</b> responde sozinho.</p></div>
<div class="st2"><div class="k">NO MODELO DA LOJA</div><p>Serviço, preço por marca e forma de pagamento.</p></div>
</div>
<div class="note" style="bottom:170px">Print real da oficina onde o Lomax nasceu. Dados do cliente borrados.</div>{logo()}</div>""", css2)))
S.append(dark("l13_c1_3", 3, N, '<div class="h" style="font-size:62px;margin-bottom:50px">O agente de IA <span class="blue">faz sozinho:</span></div>' + lm([
    "Responde o cliente <b>na hora</b>, até de madrugada e no fim de semana.",
    "Manda o <b>orçamento no modelo da sua empresa</b>.",
    "<b>Entende áudio</b>: o cliente fala, ele entende.",
    "Se apresenta como <b>assistente virtual</b>.",
    "E a equipe vê <b>cada conversa</b> no Lomax."]), top=250))
S.append(dark("l13_c1_4", 4, N, '<div class="h" style="font-size:62px">E quanto custa?</div><div class="price" style="margin-top:50px">R$ 69,90</div>'
    '<div class="b" style="font-size:42px;margin-top:20px;line-height:1.45">por mês, com <b>3.000 respostas</b>.<br>Acabou? <b>+1.000 por R$ 19,90</b>.<br><br>'
    'Com o Lomax (R$ 99,90 com 2 usuários):<br><b class="blue" style="font-size:56px">R$ 169,80 por mês.</b></div>', top=280))
S.append(("l13_c1_5", page(cta("Cliente chamou às 22h?", "Agora alguém responde.",
    "O agente de IA do Lomax atende enquanto a sua equipe descansa. De manhã, é só ver o que ele já resolveu."), css)))

# Stories 1080x1920
ST = []
ST.append(st.faq("ls_46_atende_sozinho", "O WhatsApp atende sozinho?", "<span style='font-size:150px'>Agora atende.</span>",
  "O agente de IA do Lomax responde o cliente e manda o orçamento, até de madrugada. Entende áudio também."))
ST.append(st.faq("ls_47_preco_ia", "Quanto custa<br>o agente de IA?", "R$ 69,90",
  "por mês, com 3.000 respostas. Acabou? Mais 1.000 por R$ 19,90.", theme="light"))
ST.append(("ls_48_print", st.page(st.headline("Sábado, 20h06.", "Respondeu sozinho.", top=220, size=104) + f"""
<div style='position:absolute;left:310px;width:460px;top:600px;border-radius:44px;overflow:hidden;border:12px solid #0A192C;box-shadow:0 30px 70px rgba(10,25,44,.3)'><img src='{PRINT}' style='display:block;width:100%'></div>
<div class='note' style='bottom:380px'>Print real da oficina onde o Lomax nasceu. Cliente borrado.</div>""" + st.logo().replace("bottom:290px", "bottom:250px"))))

# Conexão pelo celular com código (liberada pelo Luiz em 14/11 20h16): sem computador para ler QR Code.
S.append(single("l13_s1_celular", "Sem computador?", "Conecta", "pelo celular.",
    "Agora o seu WhatsApp entra no Lomax com um <b>código</b>, direto no celular. Sem QR Code, sem computador.", dark=True, size=104))
ST.append(st.faq("ls_49_celular", "Preciso de computador<br>pra conectar?", "Não.",
  "Agora o WhatsApp conecta ao Lomax pelo celular, com um código. Sem QR Code e sem computador.", theme="light"))

# Checagem de 15/11 (ideia de Datacrazy "23 pessoas pediram preço depois do expediente" e WeSales "23h40"): post único com o agente de IA.
S.append(single("l13_s2_21h40", "Pediu preço", "às 21h40?", "Já tem resposta.",
    "O agente de IA do Lomax responde na hora, com o orçamento no modelo da sua empresa. Entende até áudio. De manhã, a sua equipe só continua a conversa.", dark=False, size=110))

if __name__ == "__main__":
    out = "/home/claude/l5/out13"
    render_pngs(S, out)
    render_pngs(ST, out, w=st.W, h=st.H)
    print(len(S), len(ST))
