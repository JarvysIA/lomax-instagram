"""Stories do lote 12 (13/11): 10 stories FAQ, 1 por dia. Só fatos confirmados pelo Luiz."""
from stories import page, logo, headline, faq, W, H
from base import render_pngs

S = []
S.append(faq("ls_36_teste_equipe", "Dá pra testar com a equipe toda?", "Dá.",
  "São 30 dias grátis, no seu número, com a sua equipe atendendo de verdade. Sem cartão."))
S.append(faq("ls_37_desistir", "E se eu desistir no teste?", "Nada.",
  "Não tem cartão cadastrado, então não tem cobrança. É só não continuar.", theme="light"))
S.append(faq("ls_38_dois", "Sou só eu e mais um. Vale?", "Vale.",
  "O plano já vem com 2 usuários: R$ 99,90 por mês. Entrou mais alguém? R$ 49,90 por usuário extra."))
S.append(faq("ls_39_por_dia", "Quanto custa por dia?", "R$ 3,33.",
  "R$ 99,90 por mês com 2 usuários. Menos que um cliente esquecido.", theme="light"))
S.append(faq("ls_40_sumiu", "Cliente sumiu. E aí?", "<span style='font-size:118px'>Retorno automático.</span>",
  "Quem pediu orçamento e não voltou recebe o retorno com o seu texto, em horário comercial. Para sozinho quando ele responde."))
S.append(faq("ls_41_anual", "Tem contrato anual?", "Não.",
  "É mês a mês: paga pra usar. Não quer mais? Não renova. Sem multa.", theme="light"))
S.append(faq("ls_42_configura", "Quem configura?", "<span style='font-size:118px'>A gente, com você.</span>",
  "Numa chamada de vídeo com hora marcada: conecta o número e monta as equipes e o funil. Sem taxa."))
S.append(faq("ls_43_barra", "Respostas de sempre?", "<span style='font-size:118px'>Digitou /, aparece.</span>",
  "Preço, prazo e horário viram mensagem rápida. A equipe responde igual e em segundos.", theme="light"))
S.append(faq("ls_44_22h", "Mensagem às 22h?", "<span style='font-size:118px'>Já tem dono.</span>",
  "A conversa nova cai no funil com um atendente responsável. De manhã, ninguém precisa perguntar de quem é."))
S.append(faq("ls_45_dono", "Seu WhatsApp tem dono?", "<span style='font-size:118px'>Deveria ter.</span>",
  "No Lomax, cada conversa tem um responsável e cada mensagem sai com o nome de quem atendeu.", theme="light"))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out_s12")
    print(len(S))
