"""l10_c1 (checagem de 30/10): "Fim de ano chegando: seu WhatsApp aguenta o movimento?"
Ideia recriada de WhaScale (29/10), Datacrazy (29/10) e WaSeller (28/10): preparar o WhatsApp antes do pico de fim de ano.
Só recursos que existem: mensagens rápidas (/), conversa nova cai com um atendente, retorno automático em horário comercial."""
from base import *
from c9 import css, cnt, cover
from c7 import cta

N = 4
S = []
S.append(cover("l10_c1_1", "Fim de ano chegando.", "Seu WhatsApp", "aguenta o movimento?", "3 coisas pra arrumar ainda em novembro. 👉", size=86))

S.append(("l10_c1_2", page(f"""<div class="s dark">{cnt(2,N)}
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="h" style="font-size:68px;margin-bottom:46px">Em dezembro, <span style="color:#ff6b78">sem organização:</span></div>
<div class="biglist">
<div class="mv"><div class="bd" style="background:#2a3b52;width:80px">😩</div><p>O mesmo <b>“quanto custa?”</b> respondido 30 vezes por dia.</p></div>
<div class="mv"><div class="bd" style="background:#2a3b52;width:80px">🤷</div><p>Ninguém sabe <b>quem já respondeu</b> qual cliente.</p></div>
<div class="mv"><div class="bd" style="background:#2a3b52;width:80px">👻</div><p>Quem pediu orçamento <b>some</b> e ninguém chama de volta.</p></div>
</div></div>{logo()}</div>""", css)))

S.append(("l10_c1_3", page(f"""<div class="s dark">{cnt(3,N)}
<div style="position:absolute;top:250px;left:96px;right:96px">
<div class="h" style="font-size:66px;margin-bottom:50px">Arruma agora, <span class="blue">colhe em dezembro:</span></div>
<div class="part"><div class="n">1</div><p><b>Respostas prontas.</b> Preço, prazo e horário viram mensagem rápida: digitou <b>/</b>, aparece.</p></div>
<div class="part"><div class="n">2</div><p><b>Cada conversa com dono.</b> Conversa nova já cai com um atendente, e cada mensagem sai com o nome de quem respondeu.</p></div>
<div class="part"><div class="n">3</div><p><b>Retorno automático.</b> Quem sumiu recebe o retorno sozinho, em horário comercial.</p></div>
</div>{logo()}</div>""", css)))

S.append(("l10_c1_4", page(cta("Começa em novembro.", "Pronto em dezembro.", "O teste do Lomax dura 30 dias: dá tempo de organizar a equipe antes do movimento de fim de ano."), css)))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out10")
    print(len(S))
