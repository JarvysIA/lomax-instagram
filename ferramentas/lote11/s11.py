"""Stories do lote 11 (06/11): 10 stories, 1 por dia. Base: série "Reclamações" e as confirmações do Luiz de 03 e 04/11
(sem fidelidade, sem cartão, sem taxa de implantação, suporte grátis, cancela não renovando, visibilidade por equipe)."""
from stories import page, logo, headline, faq, W, H
from base import render_pngs

S = []
S.append(faq("ls_26_fidelidade", "Tem fidelidade?", "Não.",
  "Você paga mês a mês pra usar. Não quer mais? É só não renovar. Sem multa e sem burocracia."))
S.append(faq("ls_27_implantacao", "Tem taxa de implantação?", "Não.",
  "A configuração é feita junto com você, por vídeo com hora marcada, sem cobrar nada a mais."))
S.append(faq("ls_28_suporte_gratis", "O suporte é pago?", "Não.",
  "Suporte em tudo pelo WhatsApp e ajuda por vídeo com hora marcada. Tudo grátis, durante o teste e depois."))
S.append(faq("ls_29_cancelar", "Como eu cancelo?", "Não renova.",
  "A mensalidade é paga mês a mês. Se não pagar a renovação, o plano para. Simples assim.", theme="light"))
S.append(faq("ls_30_pagamento", "Como eu pago?", "<span style='font-size:130px'>Pix ou boleto.</span>",
  "R$ 99,90 por mês com 2 usuários, mês a mês. Sem cartão de crédito, nem pra testar.", theme="light"))
S.append(faq("ls_31_usuario_extra", "E se a equipe crescer?", "R$ 49,90.",
  "É o valor de cada usuário além dos 2 que já vêm no plano. Todo mundo no mesmo número."))
S.append(faq("ls_32_vendedores", "Um vendedor vê os clientes do outro?", "<span style='font-size:112px'>Só se você quiser.</span>",
  "Você escolhe: tudo liberado ou cada equipe vendo só o funil dela. Financeiro só com o financeiro."))
S.append(faq("ls_33_comeco", "Quanto tempo pra começar?", "<span style='font-size:140px'>Uma chamada.</span>",
  "Marca um horário, a gente conecta o seu número e monta as equipes e o funil junto com você.", theme="light"))
S.append(faq("ls_34_negocio", "Serve pro meu negócio?", "<span style='font-size:118px'>Provavelmente.</span>",
  "Oficina, clínica, salão, loja, imobiliária, pet shop: se você atende pelo WhatsApp com mais de uma pessoa, serve. Testa 30 dias."))
S.append(faq("ls_35_cobranca", "Vem cobrança surpresa?", "Não.",
  "Mensalidade fixa. Sem cobrança por mensagem, sem taxa de implantação e sem suporte pago."))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out_s11", w=W, h=H)
    print(len(S))
