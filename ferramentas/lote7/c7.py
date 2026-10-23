"""Lote 7 (23/10): 4 carrosséis + 2 posts únicos. Ângulo carioca, só funções que o Lomax já tem."""
from base import *
from c6 import css as css6

css = css6 + """
.bq{display:inline-block;background:#fff;color:#0A192C;border-radius:30px 30px 30px 8px;padding:26px 34px;font-size:58px;font-weight:700;box-shadow:0 14px 34px rgba(0,0,0,.25)}
.bqt{font-size:28px;font-weight:600;color:#8796ab;margin-top:14px}
.ans{margin-top:80px;background:#16253a;border-left:8px solid #0E8DFE;border-radius:20px;padding:34px 38px}
.ans .k{font-size:28px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#0E8DFE;margin-bottom:14px}
.ans p{font-size:44px;line-height:1.32;font-weight:500}
.ans b{font-weight:800}
.cmd{font-family:monospace;background:#0E8DFE;color:#fff;border-radius:10px;padding:2px 12px;font-size:34px}
.ck{display:flex;gap:26px;align-items:flex-start;background:#fff;border-radius:24px;padding:32px 34px;margin-bottom:22px;box-shadow:0 10px 30px rgba(10,25,44,.08)}
.ck .bx{flex:none;width:48px;height:48px;border-radius:12px;border:4px solid #0E8DFE;margin-top:2px}
.ck p{font-size:40px;line-height:1.28;font-weight:600;color:#0A192C}
.res{display:flex;gap:30px;align-items:flex-start;margin-bottom:46px}
.res .n{flex:none;width:170px;border-radius:18px;padding:14px 0;text-align:center;font-weight:900;font-style:italic;font-size:40px}
.res p{font-size:40px;line-height:1.3;font-weight:500}
.tl{position:relative;padding-left:60px}
.tl:before{content:'';position:absolute;left:18px;top:10px;bottom:10px;width:4px;background:#2a3b52}
.st{position:relative;margin-bottom:34px}
.st:before{content:'';position:absolute;left:-52px;top:8px;width:28px;height:28px;border-radius:50%;background:#0E8DFE}
.st.bad:before{background:#ff6b78}
.st .t{font-size:26px;font-weight:800;color:#8796ab;letter-spacing:1px}
.st p{font-size:38px;font-weight:700;margin-top:4px}
.step{font-weight:900;font-style:italic;font-size:200px;line-height:.8;color:#0E8DFE}
"""


def cnt(i, n): return f'<div class="count">{i}/{n}</div>'


def cta(title="Feito por carioca,", pill="pra carioca.", txt="O Lomax nasceu no balcão de um auto center no Rio. A equipe toda atende no mesmo número, pelo computador.", top=230):
    return f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:{top}px;left:96px;right:96px">
<div class="h" style="font-size:84px">{title}</div>
<div class="h" style="font-size:84px;margin-top:18px"><span class="pl">{pill}</span></div>
<div class="b" style="font-size:38px;margin-top:44px;line-height:1.4">{txt}</div>
<div style="margin-top:40px"><span class="chip">💬 Suporte em tudo pelo WhatsApp</span><span class="chip">🎥 Ajuda por vídeo com hora marcada</span></div>
<div class="cta" style="margin-top:30px">
<div style="font-size:44px;font-weight:800">Teste 30 dias grátis</div>
<div style="font-size:32px;margin-top:10px;opacity:.92">Sem cartão. Link na bio.</div>
</div></div>{logo(False)}</div>"""


S = []

# ---------- C1: as 5 mensagens que todo carioca manda ----------
N1 = 7
S.append(("l7_c1_1", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:270px;left:96px;right:96px">
<div class="tag">Atendimento no Rio</div>
<div class="h" style="font-size:92px;margin-top:26px">As 5 mensagens que<br>todo carioca manda</div>
<div class="h" style="font-size:92px;margin-top:22px"><span class="pl">no seu WhatsApp.</span></div>
<div class="b" style="font-size:40px;margin-top:50px">E como responder sem virar refém do celular. 👉</div>
</div>{logo(False)}<div class="foot">Arraste para o lado</div></div>""", css)))

MSGS = [
    ("“Qual é o valor?”", "chega toda hora, de todo mundo",
     "Mensagem rápida", "Digita <span class='cmd'>/preco</span> e a resposta sai pronta. <b>A equipe toda responde igual</b>, em segundos."),
    ("“Tá aberto sábado?”", "enviada às 23h40",
     "Funil por etapas", "A conversa entra em <b>Novo</b>. De manhã, a equipe bate o olho e vê <b>quem está esperando</b>."),
    ("“Vou ver e te falo.”", "e some por três dias",
     "Retorno automático", "Quem pediu orçamento e sumiu recebe <b>retorno automático em horário comercial</b>. Ninguém precisa lembrar."),
    ("“Fala com o Paulo, ele já sabe.”", "mas o Paulo está de folga",
     "Histórico na conversa", "Tudo fica no Lomax. <b>Qualquer um da equipe continua de onde parou</b>, e cada mensagem mostra quem respondeu."),
    ("“Vi o anúncio de vocês.”", "o clique já foi pago",
     "Origem no card", "O card avisa que <b>veio do anúncio</b> e a conversa já cai com um atendente pela <b>distribuição automática</b>."),
]
for i, (m, sub, k, a) in enumerate(MSGS, start=2):
    S.append((f"l7_c1_{i}", page(f"""<div class="s dark">{cnt(i, N1)}
<div style="position:absolute;top:330px;left:96px;right:96px">
<div class="h" style="font-size:220px;color:#16253a;position:absolute;top:-170px;right:0">{i-1}</div>
<div class="bq">{m}</div><div class="bqt">{sub}</div>
<div class="ans"><div class="k">No Lomax · {k}</div><p>{a}</p></div>
</div>{logo()}</div>""", css)))

S.append(("l7_c1_7", page(cta(), css)))

# ---------- C2: checklist ----------
N2 = 5
S.append(("l7_c2_1", page(f"""<div class="s dark">
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="tag">Teste rápido · 8 perguntas</div>
<div class="h" style="font-size:100px;margin-top:26px">Seu WhatsApp<br>passa nesse teste?</div>
<div class="b" style="font-size:42px;margin-top:50px;line-height:1.4">Conta quantas vezes você responde <b style="color:#fff">“sim”</b>. Sem roubar. 😅</div>
</div>{logo()}<div class="foot">Arraste para o lado</div></div>""", css)))

Q1 = ["Você sabe quantos clientes estão esperando resposta agora?",
      "Sabe quem da equipe respondeu o último orçamento?",
      "Se o atendente faltar, outra pessoa continua a conversa?",
      "O cliente fala com um número só, não com um por setor?"]
Q2 = ["Quem pediu orçamento e sumiu recebe um retorno?",
      "Você sabe quais clientes vieram do anúncio?",
      "A resposta de preço é a mesma, não importa quem atende?",
      "Dá pra tirar um domingo sem conferir o celular?"]
for i, qs in ((2, Q1), (3, Q2)):
    items = "".join(f"<div class='ck'><div class='bx'></div><p>{q}</p></div>" for q in qs)
    S.append((f"l7_c2_{i}", page(f"""<div class="s light">{cnt(i, N2)}
<div style="position:absolute;top:200px;left:96px;right:96px"><div class="tag" style="margin-bottom:30px">Parte {i-1} de 2 · marca o que é “sim”</div>{items}</div>{logo(False)}</div>""", css)))

S.append(("l7_c2_4", page(f"""<div class="s dark">{cnt(4, N2)}
<div style="position:absolute;top:290px;left:96px;right:96px">
<div class="h" style="font-size:84px;margin-bottom:80px">E aí, <span class="blue">quantos “sim”?</span></div>
<div class="res"><div class="n" style="background:#ff6b78;color:#0A192C">0 a 3</div><p><b>Plantão total.</b> A empresa depende do seu celular pra funcionar.</p></div>
<div class="res"><div class="n" style="background:#f59e0b;color:#0A192C">4 a 6</div><p><b>No meio do caminho.</b> Funciona, mas cliente ainda escapa pelas frestas.</p></div>
<div class="res"><div class="n" style="background:#22c55e;color:#0A192C">7 a 8</div><p><b>Atendimento redondo.</b> Manda esse post pra quem precisa. 😉</p></div>
</div>{logo()}</div>""", css)))

S.append(("l7_c2_5", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:220px;left:96px;right:96px">
<div class="h" style="font-size:76px">Cada “não” aqui</div>
<div class="h" style="font-size:76px;margin-top:14px"><span class="pl">tem resposta no Lomax.</span></div>
<div class="b" style="font-size:34px;margin-top:40px;line-height:1.45">Funil por etapas · nome de quem respondeu · histórico na conversa · equipes no mesmo número · retorno automático · origem do anúncio · mensagens rápidas.</div>
<div style="margin-top:36px"><span class="chip">💬 Suporte em tudo pelo WhatsApp</span><span class="chip">🎥 Ajuda por vídeo com hora marcada</span></div>
<div class="cta" style="margin-top:26px">
<div style="font-size:44px;font-weight:800">Teste 30 dias grátis</div>
<div style="font-size:32px;margin-top:10px;opacity:.92">Sem cartão. Link na bio.</div>
</div></div>{logo(False)}</div>""", css)))

# ---------- C3: anúncio e vácuo ----------
N3 = 5
S.append(("l7_c3_1", page(f"""<div class="s dark">
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="h" style="font-size:96px">Você paga o anúncio.</div>
<div class="h" style="font-size:96px;margin-top:22px"><span class="pl">E o cliente fica</span></div>
<div class="h" style="font-size:96px;margin-top:22px">no vácuo?</div>
<div class="b" style="font-size:40px;margin-top:50px">O dinheiro some depois do “oi”. Arrasta. 👉</div>
</div>{logo()}<div class="foot">Arraste para o lado</div></div>""", css)))

S.append(("l7_c3_2", page(f"""<div class="s dark">{cnt(2, N3)}
<div style="position:absolute;top:210px;left:96px;right:96px">
<div class="h" style="font-size:64px;margin-bottom:56px">O caminho <span class="blue">do seu dinheiro:</span></div>
<div class="tl">
<div class="st"><div class="t">10:02</div><p>Cliente vê o anúncio e clica.</p></div>
<div class="st"><div class="t">10:03</div><p>“Oi, quanto fica?”</p></div>
<div class="st bad"><div class="t">10:03 → 12:40</div><p>Ninguém viu. Todo mundo achou que outro ia responder.</p></div>
<div class="st bad"><div class="t">12:41</div><p>“Já resolvi, obrigado.”</p></div>
</div></div><div class="note">Exemplo ilustrativo.</div>{logo()}</div>""", css)))

S.append(("l7_c3_3", page(f"""<div class="s dark">{cnt(3, N3)}
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="h" style="font-size:84px">O problema não é<br>o anúncio.</div>
<div class="h blue" style="font-size:84px;margin-top:16px">É o que acontece<br>depois do “oi”.</div>
<div class="b" style="font-size:40px;margin-top:54px;line-height:1.4">Quando a conversa não tem dono, cada um acha que o outro respondeu. E o cliente fecha com quem respondeu primeiro.</div>
</div>{logo()}</div>""", css)))

S.append(("l7_c3_4", page(f"""<div class="s dark">{cnt(4, N3)}
<div style="position:absolute;top:200px;left:96px;right:96px">
<div class="h" style="font-size:72px;margin-bottom:56px">No Lomax, <span class="blue">o “oi” tem dono.</span></div>
<div class="ok"><div class="i">🔀</div><p><b>Distribuição automática:</b> cada conversa nova já cai com um atendente.</p></div>
<div class="ok"><div class="i">📣</div><p><b>Origem no card:</b> você sabe quem veio do anúncio.</p></div>
<div class="ok"><div class="i">📋</div><p><b>Funil por etapas:</b> quem está esperando fica à vista.</p></div>
<div class="ok"><div class="i">⏰</div><p><b>Retorno automático</b> em horário comercial pra quem sumiu.</p></div>
</div>{logo()}</div>""", css)))

S.append(("l7_c3_5", page(cta("Anúncio bom", "merece resposta.", "Feito no Rio, no balcão de uma oficina de verdade, pra quem atende cliente pelo WhatsApp todo dia."), css)))

# ---------- C4: começar com ajuda ----------
N4 = 5
S.append(("l7_c4_1", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:290px;left:96px;right:96px">
<div class="h" style="font-size:96px">Medo de CRM</div>
<div class="h" style="font-size:96px;margin-top:14px">complicado?</div>
<div class="h" style="font-size:96px;margin-top:26px"><span class="pl">A gente começa junto.</span></div>
<div class="b" style="font-size:40px;margin-top:50px">Como é o começo no Lomax, passo a passo. 👉</div>
</div>{logo(False)}<div class="foot">Arraste para o lado</div></div>""", css)))

STEPS = [
    ("1", "Cria a conta.", "São <b>30 dias grátis, sem cartão</b>. Você testa com a sua equipe, no seu número, com os seus clientes."),
    ("2", "Marca uma chamada.", "<b>Ajuda por vídeo com hora marcada:</b> a gente configura junto com você as equipes, as etapas do funil e as mensagens rápidas."),
    ("3", "Dúvida? Chama.", "<b>Suporte em tudo pelo WhatsApp</b>, do cadastro ao primeiro cliente andando no funil. Ninguém fica sozinho."),
]
for i, (n, t, d) in enumerate(STEPS, start=2):
    S.append((f"l7_c4_{i}", page(f"""<div class="s dark">{cnt(i, N4)}
<div style="position:absolute;top:240px;left:96px;right:96px">
<div class="step">{n}</div>
<div class="h" style="font-size:84px;margin-top:40px">{t}</div>
<div class="b" style="font-size:42px;margin-top:40px;line-height:1.4">{d}</div>
</div>{logo()}</div>""", css)))

S.append(("l7_c4_5", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:240px;left:96px;right:96px">
<div class="step">4</div>
<div class="h" style="font-size:80px;margin-top:30px">Gostou? Segue.</div>
<div class="b" style="font-size:38px;margin-top:34px;line-height:1.4"><b>R$ 99,90 por mês</b> com 2 usuários. Usuário extra por R$ 49,90. Pix ou boleto.</div>
<div style="margin-top:36px"><span class="chip">💬 Suporte em tudo pelo WhatsApp</span><span class="chip">🎥 Ajuda por vídeo com hora marcada</span></div>
<div class="cta" style="margin-top:26px">
<div style="font-size:44px;font-weight:800">Teste 30 dias grátis</div>
<div style="font-size:32px;margin-top:10px;opacity:.92">Sem cartão. Link na bio.</div>
</div></div>{logo(False)}</div>""", css)))

# ---------- posts únicos ----------
S.append(("l7_s1_nao_espera", page(f"""<div class="s dark">
<div style="position:absolute;top:290px;left:96px;right:96px">
<div class="tag">Papo reto</div>
<div class="h" style="font-size:110px;margin-top:30px">No Rio, cliente<br><span class="blue">não espera.</span></div>
<div class="b" style="font-size:44px;margin-top:56px;line-height:1.4">Ele manda “oi” pra três lugares ao mesmo tempo e fecha com quem responde primeiro.</div>
<div class="b" style="font-size:34px;margin-top:40px;color:#8fa3bd">Com a equipe toda no mesmo número, quem responde primeiro é você.</div>
</div>{logo()}</div>""", css)))

S.append(("l7_s2_preco", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:250px;left:96px;right:96px">
<div class="tag">Quanto custa</div>
<div class="h" style="font-size:150px;margin-top:30px">R$ 99,90</div>
<div class="h" style="font-size:58px;margin-top:10px">por mês, <span class="pl">pra equipe atender junto.</span></div>
<div style="margin-top:56px">
<div class="ck"><div class="bx" style="background:#0E8DFE"></div><p>2 usuários inclusos · extra por R$ 49,90</p></div>
<div class="ck"><div class="bx" style="background:#0E8DFE"></div><p>Pix ou boleto</p></div>
<div class="ck"><div class="bx" style="background:#0E8DFE"></div><p>30 dias grátis, sem cartão</p></div>
</div></div>{logo(False)}</div>""", css)))

if __name__ == "__main__":
    import sys
    only = sys.argv[1:]
    items = [x for x in S if not only or any(x[0].startswith(o) for o in only)]
    render_pngs(items, "/home/claude/l5/out7")
    print(len(items))
