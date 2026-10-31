"""l10_c3 (checagem de 31/10; ideia recriada de @ativocode 30/10: roteiro para aproveitar o teste grátis).
Lomax: 30 dias, sem cartão. Só recursos que existem: chamada de vídeo para configurar, equipes, etapas do funil,
mensagens rápidas, retorno automático, confirmação de horário, card que marca quem veio do anúncio."""
from base import *
from c9 import css, cnt, cover
from c7 import cta

N = 4
S = []
S.append(cover("l10_c3_1", "30 dias grátis", "passam rápido.", "Use todos eles.", "Um roteiro pra chegar no fim do teste sabendo se o Lomax serve pra você. 👉", size=92))

EV = [("SEMANA 1", "Conecte o seu número e marque a chamada de vídeo: a gente monta junto as equipes e as etapas do funil."),
      ("SEMANA 2", "Transforme as perguntas de sempre em mensagens rápidas e ligue o retorno automático."),
      ("SEMANA 3", "Ligue a confirmação de horário e veja no card quem chegou pelo anúncio."),
      ("SEMANA 4", "Deixe a equipe toda atendendo pelo Lomax, no mesmo número, sem voltar pro celular.")]
evs = "".join(f'<div class="ev" style="margin-bottom:24px"><div class="t" style="font-size:26px">{t}</div><p style="font-size:34px">{p}</p></div>' for t, p in EV)
S.append(("l10_c3_2", page(f"""<div class="s dark">{cnt(2,N)}
<div style="position:absolute;top:150px;left:96px;right:96px">
<div class="h" style="font-size:64px;margin-bottom:36px">O roteiro, <span class="blue">semana a semana:</span></div>
<div class="tl2">{evs}</div>
</div>{logo()}</div>""", css)))

S.append(("l10_c3_3", page(f"""<div class="s dark">{cnt(3,N)}
<div style="position:absolute;top:250px;left:96px;right:96px" class="bigok">
<div class="h" style="font-size:68px;margin-bottom:56px">No 30º dia, <span class="blue">olhe 3 coisas:</span></div>
<div class="ok"><div class="i">🔁</div><p>Quantos clientes <b>voltaram a responder</b> depois do retorno automático.</p></div>
<div class="ok"><div class="i">📅</div><p>Quantos horários foram <b>confirmados sem ninguém ligar.</b></p></div>
<div class="ok"><div class="i">🙋</div><p>Se a equipe parou de perguntar <b>“quem respondeu esse cliente?”</b></p></div>
</div>{logo()}</div>""", css)))

S.append(("l10_c3_4", page(cta("Sem cartão.", "Sem pegadinha.", "São 30 dias pra testar com a sua equipe, no seu número. Se servir, R$ 99,90 por mês com 2 usuários. Se não servir, é só não continuar."), css)))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out12")
    print(len(S))
