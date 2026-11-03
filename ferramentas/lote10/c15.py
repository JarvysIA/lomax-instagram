"""l10_c4 (resposta do Luiz em 03/11): visibilidade por funil e equipe. Pode ficar tudo liberado ou cada equipe ver só o funil dela;
em vendas, um vendedor não precisa ver os clientes do outro. Financeiro só o financeiro, marketing só o marketing."""
from base import *
from c9 import css, cnt, cover
from c7 import cta

N = 4
S = []
S.append(cover("l10_c4_1", "O financeiro precisa", "ler a conversa de vendas?", "Não precisa.", "No Lomax, você escolhe quem vê o quê. Arrasta. 👉", size=80))

S.append(("l10_c4_2", page(f"""<div class="s dark">{cnt(2,N)}
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="h" style="font-size:68px;margin-bottom:56px">Dois jeitos, <span class="blue">você decide:</span></div>
<div class="card2" style="margin-bottom:36px"><div style="font-size:30px;font-weight:800;color:#0E8DFE;letter-spacing:1px">TUDO LIBERADO</div>
<div style="font-size:38px;font-weight:600;margin-top:10px;line-height:1.3">Todo mundo vê todas as conversas. Bom pra equipe pequena.</div></div>
<div class="card2"><div style="font-size:30px;font-weight:800;color:#0E8DFE;letter-spacing:1px">POR FUNIL E EQUIPE</div>
<div style="font-size:38px;font-weight:600;margin-top:10px;line-height:1.3">Cada equipe vê só o funil dela. O resto fica fechado.</div></div>
</div>{logo()}</div>""", css)))

def row(ic, t, d):
    return f'<div class="mv"><div class="bd" style="background:#16253a;width:84px;font-style:normal">{ic}</div><p><b>{t}</b><br>{d}</p></div>'
S.append(("l10_c4_3", page(f"""<div class="s dark">{cnt(3,N)}
<div style="position:absolute;top:260px;left:96px;right:96px" class="biglist">
<div class="h" style="font-size:66px;margin-bottom:56px">Mesmo número,<br><span class="blue">cada um no seu:</span></div>
{row("💼","Vendas","Só os vendedores. E um vendedor não precisa ver os clientes do outro.")}
{row("💰","Financeiro","Só o financeiro vê cobrança e pagamento.")}
{row("📣","Marketing","Só o marketing vê as conversas dele.")}
</div>{logo()}</div>""", css)))

S.append(("l10_c4_4", page(cta("Um WhatsApp só.", "Cada equipe no seu.", "O cliente fala com um número. Por dentro, cada conversa fica com quem precisa ver, e mais ninguém."), css)))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out15")
    print(len(S))
