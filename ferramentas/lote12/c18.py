"""l12_c1 (checagem de 07/11; ideia recriada do Columba/@ativocode 06/11: "10 coisas que o seu WhatsApp não faz sozinho").
Só recursos do Lomax já usados em posts confirmados; nada de IA, nada de citar concorrente."""
from base import *
from c17 import css, dark, cover, cta

def nl(items, start):
    return "".join(f'<div class="lm"><div class="i" style="background:#16253a;color:#7fc0ff;font-size:34px">{start+i:02d}</div><p>{t}</p></div>' for i, t in enumerate(items))

N = 4
S = [cover("l12_c1_1", "10 coisas que", "o seu WhatsApp", "não faz sozinho.", "E o Lomax faz. Arrasta. 👉", size=96)]
S.append(dark("l12_c1_2", 2, N, '<div class="h" style="font-size:62px;margin-bottom:46px">As 5 primeiras:</div>' + nl([
    "A <b>equipe toda</b> atende no mesmo número, pelo computador.",
    "Cada mensagem sai com o <b>nome de quem atendeu</b>.",
    "Conversa nova já cai com <b>um responsável</b>.",
    "Passa pra outra equipe <b>com o histórico junto</b>.",
    "Cada equipe vê <b>só o funil dela</b>, se você quiser."], 1), top=230))
S.append(dark("l12_c1_3", 3, N, '<div class="h" style="font-size:62px;margin-bottom:46px">E mais 5:</div>' + nl([
    "Preço e prazo viram <b>mensagem rápida</b>: digitou /, aparece.",
    "Quem sumiu recebe o <b>retorno automático</b>.",
    "O horário marcado é <b>confirmado sozinho</b>.",
    "O card mostra quem <b>veio do anúncio</b>.",
    "Tudo isso <b>com o computador desligado</b>."], 6), top=230))
S.append(("l12_c1_4", page(cta("O WhatsApp é o mesmo.", "O jeito de atender, não.", "Testa 30 dias grátis, sem cartão. Se servir, R$ 99,90 por mês com 2 usuários."), css)))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out18")
    print(len(S))
