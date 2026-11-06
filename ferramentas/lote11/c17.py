"""Lote 11 (06/11): 6 carrosséis + 12 posts únicos. Série "Reclamações" (ideia do @alvim_ai, aprovada pelo Luiz em 04/11)
e confirmações do Luiz de 03 e 04/11: sem fidelidade, sem cartão, sem taxa de implantação, suporte grátis, cancela não renovando,
visibilidade por funil e equipe. Nada de citar concorrente. Fechamento: link na bio."""
from base import *
from c9 import css as css9, cnt, cover, single
from c7 import cta

css = css9 + """
.q{background:#16253a;border-radius:26px;padding:38px 40px;margin-bottom:40px;position:relative}
.q .t{font-size:46px;font-weight:700;font-style:italic;line-height:1.25;color:#fff}
.q .r{margin-top:18px;font-size:38px;color:#9fd0ff;font-weight:600;line-height:1.3}
.q .r b{color:#fff}
.lm{display:flex;gap:22px;align-items:center;margin-bottom:34px}
.lm .i{flex:none;width:68px;height:68px;border-radius:18px;background:#123a2a;color:#4fe08f;font-size:40px;font-weight:900;display:flex;align-items:center;justify-content:center}
.lm p{font-size:41px;font-weight:600;line-height:1.25}
.price{font-size:150px;font-weight:900;font-style:italic;color:#0E8DFE;line-height:1}
.ev2{border-left:6px solid #0E8DFE;padding:4px 0 4px 30px;margin-bottom:34px}
.ev2 .t{font-size:26px;font-weight:800;color:#7fc0ff;letter-spacing:2px}
.ev2 p{font-size:37px;line-height:1.3;margin-top:6px}
.bad .i{background:#3a1820;color:#ff6b78}
"""
NOTE_Q = '<div class="note">Frases resumidas de avaliações públicas de clientes de sistemas de atendimento.</div>'
S = []

def dark(name, n, N, inner, top=220, note=""):
    return (name, page(f"""<div class="s dark">{cnt(n,N)}<div style="position:absolute;top:{top}px;left:96px;right:96px">{inner}</div>{note}{logo()}</div>""", css))

def lm(items, cls=""):
    return "".join(f'<div class="lm {cls}"><div class="i">{"✕" if cls else "✓"}</div><p>{t}</p></div>' for t in items)

# C1 — A letra miúda do Lomax
S.append(cover("l11_c1_1", "A letra miúda", "do Lomax.", "Cabe numa tela só.", "Arrasta e lê tudo, sem asterisco. 👉", size=104))
S.append(dark("l11_c1_2", 2, 4, '<div class="h" style="font-size:66px;margin-bottom:50px">Tudo o que <span class="blue">você precisa saber:</span></div>' + lm([
    "<b>Sem fidelidade.</b> Paga mês a mês.", "<b>Cancelar?</b> É só não renovar.", "<b>Sem cartão</b>, nem pra testar.",
    "<b>Sem taxa</b> de implantação.", "<b>Suporte grátis</b> no WhatsApp e por vídeo.", "<b>Sem cobrança</b> por mensagem."]), top=250))
S.append(dark("l11_c1_3", 3, 4, '<div class="h" style="font-size:62px">E o preço?</div><div class="price" style="margin-top:50px">R$ 99,90</div>'
    '<div class="b" style="font-size:42px;margin-top:20px;line-height:1.4">por mês, com <b>2 usuários</b>.<br>Usuário extra: <b>R$ 49,90</b>.<br>Pix ou boleto.</div>', top=300))
S.append(("l11_c1_4", page(cta("Leu tudo?", "Foi só isso mesmo.", "30 dias pra testar com a sua equipe, no seu número. Se servir, você continua. Se não servir, é só não renovar."), css)))

# C2 — 6 perguntas antes de contratar
S.append(cover("l11_c2_1", "Antes de contratar", "um CRM de WhatsApp,", "faz essas 6 perguntas.", "Salva pra usar na próxima reunião de venda. 📌", size=84))
def qs(items, start, fs=44):
    return "".join(f'<div class="part" style="margin-bottom:44px"><div class="n">{start+i}</div><p style="font-size:{fs}px"><b>{t}</b></p></div>' for i, t in enumerate(items))
S.append(dark("l11_c2_2", 2, 5, '<div class="h" style="font-size:64px;margin-bottom:50px">Pergunta <span class="blue">antes de assinar:</span></div>' + qs(
    ["Tem fidelidade ou multa pra cancelar?", "Tem taxa de implantação?", "Cobra por mensagem enviada?"], 1, 50), top=380))
S.append(dark("l11_c2_3", 3, 5, '<div class="h" style="font-size:64px;margin-bottom:50px">E também:</div>' + qs(
    ["Precisa deixar o computador ligado?", "O suporte é pago?", "Quanto custa cada usuário a mais?"], 4, 50), top=380))
def ans(rows):
    return "".join(f'<div class="lm"><div class="i">✓</div><p>{q} <b class="blue">{a}</b></p></div>' for q, a in rows)
S.append(dark("l11_c2_4", 4, 5, '<div class="h" style="font-size:64px;margin-bottom:46px">No Lomax, <span class="blue">as respostas:</span></div>' + ans([
    ("Fidelidade?", "Não."), ("Taxa de implantação?", "Não."), ("Cobra por mensagem?", "Não."), ("Computador ligado?", "Não precisa."),
    ("Suporte pago?", "Não."), ("Usuário extra?", "R$ 49,90.")]), top=210))
S.append(("l11_c2_5", page(cta("Respostas curtas.", "Sem letra miúda.", "R$ 99,90 por mês com 2 usuários, Pix ou boleto. Testa 30 dias antes, sem cartão."), css)))

# C3 — As reclamações que mais aparecem
S.append(cover("l11_c3_1", "As reclamações que", "mais aparecem sobre", "sistema de WhatsApp.", "E o que a gente fez com cada uma. 👉", size=84))
def q(t, r): return f'<div class="q"><div class="t">“{t}”</div><div class="r">→ {r}</div></div>'
S.append(dark("l11_c3_2", 2, 5, q("Quero cancelar e estão me enrolando.", "No Lomax <b>não tem fidelidade</b>. É só não renovar.")
    + q("O suporte sumiu.", "Aqui é <b>pelo WhatsApp e por vídeo</b>, e é grátis."), top=330, note=NOTE_Q))
S.append(dark("l11_c3_3", 3, 5, q("A cobrança veio maior que o combinado.", "<b>Mensalidade fixa</b>, sem cobrança por mensagem.")
    + q("A extensão derrubou o meu WhatsApp Web.", "O Lomax <b>roda na nuvem</b>, com o computador desligado."), top=330, note=NOTE_Q))
S.append(dark("l11_c3_4", 4, 5, q("Três meses e a implantação não terminou.", "Aqui é <b>uma chamada de vídeo</b>, sem taxa de implantação.")
    + q("Caro demais pra quem tem 2 pessoas.", "<b>R$ 99,90</b> com 2 usuários inclusos."), top=330, note=NOTE_Q))
S.append(("l11_c3_5", page(cta("Ouvimos as", "reclamações.", "E montamos o Lomax pra não repetir nenhuma. Testa 30 dias, sem cartão e sem compromisso."), css)))

# C4 — 5 sinais
S.append(cover("l11_c4_1", "5 sinais de que", "o seu WhatsApp", "esquece clientes.", "Conta quantos acontecem aí. 👇", size=96))
S.append(dark("l11_c4_2", 2, 4, '<div class="h" style="font-size:64px;margin-bottom:46px">Marca os que <span class="blue">acontecem aí:</span></div>' + qs(
    ["Cliente pede orçamento e ninguém chama de volta.", "Ninguém sabe quem respondeu cada cliente.", "O cliente pergunta a mesma coisa duas vezes.",
     "Tem furo na agenda toda semana.", "Quem vem do anúncio espera até o fim do dia."], 1, 42), top=240))
S.append(dark("l11_c4_3", 3, 4, '<div class="h" style="font-size:66px;margin-bottom:56px">Quantos <span class="blue">você marcou?</span></div>'
    '<div class="ev2"><div class="t">0 A 1</div><p>Tá no caminho. Só não deixa crescer.</p></div>'
    '<div class="ev2" style="border-color:#ffd166"><div class="t" style="color:#ffd166">2 A 3</div><p>Atenção: tem cliente indo embora sem você ver.</p></div>'
    '<div class="ev2" style="border-color:#ff6b78"><div class="t" style="color:#ff6b78">4 A 5</div><p>Você está perdendo venda toda semana.</p></div>', top=300))
S.append(dark("l11_c4_4", 4, 4, '<div class="h" style="font-size:62px;margin-bottom:46px">No Lomax, <span class="blue">cada sinal tem resposta:</span></div>' + lm([
    "<b>Retorno automático</b> pra quem sumiu.", "<b>Nome de quem atendeu</b> em cada mensagem.", "<b>Histórico</b> da conversa sempre junto.",
    "<b>Confirmação</b> do horário no dia anterior.", "<b>Card marca</b> quem veio do anúncio."]), top=230))

# C5 — 1 cliente, do orçamento ao horário
S.append(cover("l11_c5_1", "Um cliente sumido.", "O que acontece", "no Lomax?", "Do orçamento até o horário marcado. 👉", dark=True, size=96))
def evs(rows):
    return "".join(f'<div class="ev2"><div class="t">{t}</div><p>{p}</p></div>' for t, p in rows)
S.append(dark("l11_c5_2", 2, 3, '<div class="h" style="font-size:62px;margin-bottom:46px">Passo a passo:</div>' + evs([
    ("1 · ORÇAMENTO", "Rafael pede o preço, recebe e some."), ("2 · RETORNO", "O Lomax chama de novo, em horário comercial, com o seu texto."),
    ("3 · SEM RESPOSTA?", "Novo retorno, até 5 vezes."), ("4 · RESPONDEU", "Os retornos param e a conversa volta pra equipe."),
    ("5 · MARCOU", "A confirmação do horário sai no dia anterior.")]), top=200, note='<div class="note">Exemplo com nome fictício.</div>'))
S.append(("l11_c5_3", page(cta("Ninguém precisou", "lembrar de nada.", "O Lomax roda na nuvem, com o seu texto, em horário comercial. Testa 30 dias grátis."), css)))

# C6 — Duas segundas-feiras
S.append(cover("l11_c6_1", "O mesmo WhatsApp.", "Duas segundas-feiras.", "Qual é a sua?", "Arrasta. 👉", size=92))
S.append(dark("l11_c6_2", 2, 4, '<div class="h" style="font-size:64px;margin-bottom:46px"><span style="color:#ff6b78">Segunda sem sistema:</span></div>' + lm([
    "Celular do dono lotado desde as 7h.", "Ninguém sabe quem já respondeu.", "Orçamento de sexta esquecido.", "Cliente do anúncio esperando."], "bad"), top=340))
S.append(dark("l11_c6_3", 3, 4, '<div class="h" style="font-size:64px;margin-bottom:46px"><span class="blue">Segunda com Lomax:</span></div>' + lm([
    "Conversa nova já cai com um atendente.", "Cada mensagem com o nome de quem respondeu.", "Quem sumiu na sexta já recebeu retorno.", "O card mostra quem veio do anúncio."]), top=340))
S.append(("l11_c6_4", page(cta("Escolhe a", "segunda que você quer.", "A equipe toda no mesmo número, pelo computador. Testa 30 dias sem cartão."), css)))

# Posts únicos
SG = [
 ("l11_s1_cancelar", "“Quero cancelar e", "estão me enrolando.”", "Aqui é só não renovar.", "No Lomax não tem fidelidade nem multa. Você paga mês a mês pra usar. Não quer mais? Não renova. Pronto.", True, 84),
 ("l11_s2_suporte", "“O suporte sumiu.”", "", "Aqui ele é grátis.", "Suporte em tudo pelo WhatsApp e ajuda por vídeo com hora marcada. Durante o teste e depois, sem pagar nada a mais.", False, 100),
 ("l11_s3_implantacao", "“Três meses e a", "implantação não terminou.”", "Aqui é uma chamada.", "Você marca um horário, a gente conecta o seu número e monta as equipes e o funil junto com você. Sem taxa de implantação.", True, 80),
 ("l11_s4_taxa", "Taxa de", "implantação:", "R$ 0.", "Configuração junto com você, por vídeo, sem cobrar nada. Você só paga a mensalidade, mês a mês.", False, 110),
 ("l11_s5_surpresa", "“A cobrança veio", "maior que o combinado.”", "Aqui é R$ 99,90. Ponto.", "Mensalidade fixa com 2 usuários. Sem cobrança por mensagem, sem taxa de implantação e sem suporte pago.", True, 80),
 ("l11_s6_extensao", "“A extensão derrubou", "o meu WhatsApp Web.”", "Aqui roda na nuvem.", "O Lomax não depende do seu computador ligado. Retorno e confirmação de horário saem sozinhos, com tudo desligado.", False, 80),
 ("l11_s7_sumiu", "O cliente que sumiu", "não disse não.", "Ele só não foi chamado.", "No Lomax, quem pediu orçamento e sumiu recebe o retorno automático, em horário comercial. Para sozinho quando ele responde.", True, 78),
 ("l11_s8_custo", "Quanto custa", "um cliente esquecido?", "Mais que R$ 99,90.", "Um só que volta já paga o mês. O Lomax chama de volta quem sumiu e confirma o horário de quem marcou.", False, 92),
 ("l11_s9_sem", "Sem fidelidade. Sem cartão.", "Sem taxa. Sem pegadinha.", "Só o Lomax funcionando.", "R$ 99,90 por mês com 2 usuários, Pix ou boleto. Testa 30 dias antes de pagar qualquer coisa.", True, 72),
 ("l11_s10_extra", "2 usuários inclusos.", "Entrou mais alguém?", "R$ 49,90.", "Por usuário extra, todo mundo no mesmo número. Sem trocar de plano e sem taxa escondida.", False, 92),
 ("l11_s11_22h", "Cliente chamou", "às 22h?", "Amanhã já tem dono.", "A conversa nova cai no funil, com um atendente responsável. De manhã, a equipe já sabe quem responde.", True, 84),
 ("l11_s12_pix", "Pix ou boleto.", "Mês a mês.", "Sem cartão.", "Nem pra testar: são 30 dias grátis sem cadastrar cartão. Depois, R$ 99,90 por mês com 2 usuários.", False, 104),
]
for name, l1, l2, pill, body, dk, sz in SG:
    S.append(single(name, l1, l2, pill, body, dark=dk, size=sz))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out17")
    print(len(S))
