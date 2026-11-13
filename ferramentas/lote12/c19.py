"""Lote 12 (13/11): 5 carrosséis (l12_c2 a c6) + 12 posts únicos. O l12_c1 está em c18.py.
Lições da semana de 30/10 a 05/11: "esquecer cliente" e quiz/FAQ funcionam. Série "Reclamações" continua.
Só recursos confirmados; sem IA, sem citar concorrente, sem Black Friday."""
from base import *
from c9 import single
from c17 import css, dark, lm, cover, cta, qs, evs, q, NOTE_Q

S = []
# C2 — Teste rápido (quiz)
S.append(cover("l12_c2_1", "Teste rápido:", "o seu atendimento", "passa ou não passa?", "5 perguntas, sim ou não. Arrasta. 👉", size=90))
S.append(dark("l12_c2_2", 2, 4, '<div class="h" style="font-size:62px;margin-bottom:46px">Responde <span class="blue">sim ou não:</span></div>' + qs(
    ["Você sabe agora quem está esperando resposta?", "Todo orçamento enviado recebe um retorno?", "O cliente sabe com quem está falando?",
     "Se um atendente faltar, outro assume a conversa?", "Quem chega pelo anúncio é atendido no mesmo dia?"], 1, 42), top=230))
S.append(dark("l12_c2_3", 3, 4, '<div class="h" style="font-size:66px;margin-bottom:56px">Quantos <span class="blue">"sim"?</span></div>'
    '<div class="ev2"><div class="t">5</div><p>Passou. Seu atendimento está organizado.</p></div>'
    '<div class="ev2" style="border-color:#ffd166"><div class="t" style="color:#ffd166">3 A 4</div><p>Quase. Tem cliente escapando pelas beiradas.</p></div>'
    '<div class="ev2" style="border-color:#ff6b78"><div class="t" style="color:#ff6b78">0 A 2</div><p>Não passou. O WhatsApp está trabalhando contra você.</p></div>', top=300))
S.append(("l12_c2_4", page(cta("Não passou?", "Dá pra arrumar.", "O Lomax mostra quem está esperando, chama de volta quem sumiu e põe o nome de quem atendeu em cada mensagem. Testa 30 dias grátis."), css)))

# C3 — Sexta, 17h48 (história de cliente esquecido)
S.append(cover("l12_c3_1", "Sexta, 17h48:", "“me manda", "o orçamento?”", "O que aconteceu com esse cliente. 👉", dark=True, size=96))
S.append(dark("l12_c3_2", 2, 4, '<div class="h" style="font-size:62px;margin-bottom:46px"><span style="color:#ff6b78">Sem sistema:</span></div>' + evs([
    ("SEXTA, 17H48", "O pedido chega no celular de quem já estava saindo."),
    ("SEGUNDA, 9H", "A conversa desceu na lista. Ninguém lembra."),
    ("TERÇA, 15H", "O cliente fechou com quem respondeu primeiro.")]), top=260))
S.append(dark("l12_c3_3", 3, 4, '<div class="h" style="font-size:62px;margin-bottom:46px"><span class="blue">Com o Lomax:</span></div>' + evs([
    ("SEXTA, 17H48", "A conversa nova cai no funil, já com um responsável."),
    ("SEGUNDA, 9H", "A equipe abre o computador e vê quem está esperando."),
    ("SEM RESPOSTA?", "O retorno automático chama de volta, em horário comercial.")]), top=260))
S.append(("l12_c3_4", page(cta("O cliente não sumiu.", "Ele foi esquecido.", "No Lomax, nenhum orçamento fica sem dono. Testa 30 dias grátis, sem cartão."), css)))

# C4 — Reclamações, parte 2
S.append(cover("l12_c4_1", "Reclamações sobre", "sistema de WhatsApp,", "parte 2.", "E o que o Lomax faz com cada uma. 👉", size=90))
S.append(dark("l12_c4_2", 2, 5, q("O suporte sumiu.", "Aqui o suporte é <b>grátis</b>: WhatsApp e vídeo com hora marcada.")
    + q("Prometeram tudo na venda.", "Aqui você <b>testa 30 dias</b> antes de pagar qualquer coisa."), top=300, note=NOTE_Q))
S.append(dark("l12_c4_3", 3, 5, q("É caro pra quem tem 2 pessoas.", "<b>R$ 99,90 por mês</b> com 2 usuários inclusos.")
    + q("Pago por mensagem e nunca sei quanto vem.", "Aqui <b>não tem cobrança por mensagem</b>. Mensalidade fixa."), top=300, note=NOTE_Q))
S.append(dark("l12_c4_4", 4, 5, q("Pra cancelar foi uma novela.", "Aqui <b>não tem fidelidade</b>. Não quer mais? Não renova.")
    + q("A extensão travava o computador.", "O Lomax <b>roda na nuvem</b>, com o computador desligado."), top=300, note=NOTE_Q))
S.append(("l12_c4_5", page(cta("Leu as reclamações?", "Agora testa o Lomax.", "30 dias grátis, sem cartão e sem compromisso. Se não servir, é só não continuar."), css)))

# C5 — Quem está esperando?
S.append(cover("l12_c5_1", "4 perguntas que", "o seu WhatsApp", "não responde.", "E o funil do Lomax responde. 👉", size=94))
S.append(dark("l12_c5_2", 2, 4, '<div class="h" style="font-size:62px;margin-bottom:46px">Responde rápido:</div>' + qs(
    ["Quem está esperando resposta agora?", "Quem pediu orçamento e não voltou?", "Quem atendeu esse cliente da última vez?", "Em que etapa está cada negociação?"], 1, 46), top=260))
S.append(dark("l12_c5_3", 3, 4, '<div class="h" style="font-size:62px;margin-bottom:46px">No Lomax, <span class="blue">está na tela:</span></div>' + lm([
    "Cada conversa vira um <b>card no funil</b>.", "Cada card tem <b>um responsável</b>.", "Cada mensagem sai com o <b>nome de quem atendeu</b>.",
    "Quem sumiu recebe o <b>retorno automático</b>."]), top=260))
S.append(("l12_c5_4", page(cta("Pergunta respondida", "em 1 olhada.", "O funil do Lomax mostra quem está esperando e quem atende cada cliente. Testa 30 dias grátis."), css)))

# C6 — Gente nova na equipe
S.append(cover("l12_c6_1", "Entrou gente nova", "na equipe?", "Sem passar senha.", "Como fica o WhatsApp no Lomax. 👉", size=94))
S.append(dark("l12_c6_2", 2, 4, '<div class="h" style="font-size:62px;margin-bottom:46px"><span style="color:#ff6b78">Do jeito antigo:</span></div>' + lm([
    "Passa a senha do WhatsApp pra mais um.", "Ninguém sabe quem respondeu o quê.", "Se a pessoa sai, leva o acesso junto."], "bad"), top=280))
S.append(dark("l12_c6_3", 3, 4, '<div class="h" style="font-size:62px;margin-bottom:46px"><span class="blue">No Lomax:</span></div>' + lm([
    "Cada um com <b>o próprio login</b>.", "Você define <b>quem vê o quê</b>.", "Passa a conversa <b>com o histórico junto</b>.",
    "Saiu alguém? <b>O número continua da empresa.</b>"]), top=260))
S.append(("l12_c6_4", page(cta("Equipe cresceu?", "O número é o mesmo.", "2 usuários inclusos e R$ 49,90 por usuário extra. Testa 30 dias grátis com a equipe toda."), css)))

SG = [
 ("l12_s1_esperando", "Quem está esperando", "resposta agora?", "No Lomax, está na tela.", "Cada conversa vira um card no funil, com um responsável. Você vê quem está esperando sem rolar o celular.", True, 84),
 ("l12_s2_promessa", "“Prometeram tudo", "na venda.”", "Aqui você testa antes.", "30 dias grátis, sem cartão, com a sua equipe e o seu número. Se servir, você continua. Se não, é só não continuar.", False, 96),
 ("l12_s3_caro", "“É caro pra quem", "tem 2 pessoas.”", "R$ 99,90 com 2 usuários.", "Mensalidade fixa, sem cobrança por mensagem e sem taxa de implantação. Cresceu? R$ 49,90 por usuário extra.", True, 72),
 ("l12_s4_orcamento", "Orçamento enviado", "não é venda feita.", "É meio caminho.", "No Lomax, quem recebeu o orçamento e não respondeu ganha o retorno automático, com o seu texto, em horário comercial.", False, 90),
 ("l12_s5_dono", "Cada conversa", "com dono.", "Desde a 1ª mensagem.", "Conversa nova já cai com um atendente responsável. Ninguém responde duas vezes e ninguém fica sem resposta.", True, 104),
 ("l12_s6_sexta", "Sexta, 17h48:", "“me manda o orçamento?”", "Segunda já tem dono.", "A conversa cai no funil com um responsável. Se o cliente não voltar, o retorno automático chama de novo.", False, 84),
 ("l12_s7_numero", "O número é", "da empresa.", "Não do funcionário.", "No Lomax, cada um entra com o próprio login. Se alguém sai, o número e as conversas continuam com você.", True, 104),
 ("l12_s8_barra", "Digitou /,", "apareceu.", "Resposta pronta.", "Preço, prazo, endereço e horário viram mensagem rápida. A equipe responde igual e em segundos.", False, 112),
 ("l12_s9_lembrar", "O seu cliente", "não lê mente.", "Ele precisa ser lembrado.", "No Lomax, o horário marcado é confirmado sozinho e quem sumiu recebe o retorno automático.", True, 104),
 ("l12_s10_equipe", "1 número.", "A equipe toda.", "Cada um no seu login.", "Vendas, atendimento e financeiro no mesmo WhatsApp, pelo computador. O cliente salva um contato só.", False, 112),
 ("l12_s11_anuncio", "Pagou anúncio?", "Saiba quem veio dele.", "O card avisa.", "O Lomax marca no card quem chegou pela campanha. Você sabe o que o anúncio trouxe e atende primeiro.", True, 92),
 ("l12_s12_teste", "30 dias.", "Sem cartão.", "Com a sua equipe.", "No seu número, com a configuração feita junto com você por vídeo. Depois, R$ 99,90 por mês com 2 usuários.", False, 112),
]
for name, l1, l2, pill, body, dk, sz in SG:
    S.append(single(name, l1, l2, pill, body, dark=dk, size=sz))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out19")
    print(len(S))
