"""l10_c2 (pedido do Luiz em 30/10): comparação por TIPO de sistema, sem citar marca.
Extensão do Chrome x plataforma grande x CRM na nuvem (Lomax). Só fatos de categoria e recursos confirmados do Lomax."""
from base import *
from c9 import css as css9, cnt, cover
from c7 import cta

css = css9 + """
.typ{display:inline-block;background:#16253a;color:#7fc0ff;border-radius:999px;padding:12px 28px;font-size:28px;font-weight:800;letter-spacing:1px;margin-bottom:34px}
.pc{display:flex;gap:24px;align-items:flex-start;margin-bottom:44px}
.pc .i{flex:none;width:72px;height:72px;border-radius:20px;display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:900}
.pc p{font-size:41px;line-height:1.3;font-weight:500}
.pc b{font-weight:800}
.g{background:#123a2a;color:#4fe08f}.r{background:#3a1820;color:#ff6b78}.y{background:#3a3214;color:#ffd166}
table.cmp{width:100%;border-collapse:separate;border-spacing:0 14px}
table.cmp th{font-size:28px;font-weight:800;color:#8796ab;text-align:center;padding:0 6px 6px;line-height:1.2}
table.cmp th.lx{color:#0E8DFE}
table.cmp td{background:#16253a;font-size:36px;text-align:center;padding:24px 8px}
table.cmp td.q{text-align:left;font-size:32px;font-weight:700;padding-left:24px;border-radius:18px 0 0 18px;width:40%}
table.cmp td:last-child{border-radius:0 18px 18px 0;background:#0E8DFE22}
"""
N = 6
S = []
S.append(cover("l10_c2_1", "Extensão,", "plataforma grande", "ou CRM na nuvem?", "Qual serve pro seu WhatsApp. Arrasta. 👉", size=88))

def tipo(name, n, tag, title, items, note):
    rows = "".join(f'<div class="pc"><div class="i {c}">{s}</div><p>{t}</p></div>' for c, s, t in items)
    return (name, page(f"""<div class="s dark">{cnt(n,N)}
<div style="position:absolute;top:240px;left:96px;right:96px">
<div class="typ">{tag}</div>
<div class="h" style="font-size:66px;margin-bottom:50px">{title}</div>
{rows}
<div class="b" style="font-size:32px;margin-top:20px;color:#8796ab;line-height:1.4">{note}</div>
</div>{logo()}</div>""", css))

S.append(tipo("l10_c2_2", 2, "TIPO 1", "Extensão do Chrome", [
    ("g", "+", "<b>Simples e rápida</b> de instalar."),
    ("g", "+", "Usa o <b>número que você já tem.</b>"),
    ("r", "−", "Roda <b>dentro do WhatsApp Web aberto.</b> Fechou o computador, parou."),
    ("r", "−", "Lembretes e retornos <b>dependem da máquina ligada.</b>"),
], "Boa pra quem atende sozinho, sentado no computador."))

S.append(tipo("l10_c2_3", 3, "TIPO 2", "Plataforma grande", [
    ("g", "+", "<b>Muitos recursos</b> e vários canais."),
    ("g", "+", "Roda <b>na nuvem.</b>"),
    ("y", "!", "Costuma usar a API oficial da Meta, que <b>cobra por mensagem.</b>"),
    ("y", "!", "Mais recurso, <b>mais coisa pra configurar.</b>"),
], "Boa pra operação grande, com gente dedicada só a isso."))

S.append(tipo("l10_c2_4", 4, "TIPO 3", "CRM na nuvem, <span class=\"blue\">do jeito do Lomax</span>", [
    ("g", "✓", "Roda <b>na nuvem</b>, com o computador desligado."),
    ("g", "✓", "<b>A equipe toda</b> no mesmo número que você já tem."),
    ("g", "✓", "<b>Sem cobrança por mensagem.</b>"),
    ("g", "✓", "Retorno automático, confirmação de horário e funil <b>já prontos.</b>"),
], "Feito pra pequena empresa que atende pelo WhatsApp com mais de uma pessoa."))

ROWS = [("Funciona com o computador desligado", "❌", "✅", "✅"),
        ("Usa o número que você já tem", "✅", "Varia", "✅"),
        ("Sem cobrança por mensagem", "✅", "Varia", "✅"),
        ("Retorno automático na nuvem", "❌", "✅", "✅")]
trs = "".join(f'<tr><td class="q">{q}</td><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for q, a, b, c in ROWS)
S.append(("l10_c2_5", page(f"""<div class="s dark">{cnt(5,N)}
<div style="position:absolute;top:170px;left:80px;right:80px">
<div class="h" style="font-size:64px;margin-bottom:40px">Lado a lado:</div>
<table class="cmp"><tr><th></th><th>Extensão</th><th>Plataforma grande</th><th class="lx">Lomax</th></tr>{trs}</table>
<div class="b" style="font-size:34px;margin-top:40px;line-height:1.42">Não existe sistema certo pra todo mundo. Existe o certo pro tamanho da sua equipe.</div>
</div><div class="note">Comparação entre tipos de sistema. Cada produto tem suas regras: confira antes de contratar.</div>{logo()}</div>""", css)))

S.append(("l10_c2_6", page(cta("Ficou no meio?", "Esse é o Lomax.", "Equipe toda no mesmo número, rodando na nuvem e sem cobrança por mensagem. Testa 30 dias e vê se serve pra você."), css)))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out11")
    print(len(S))
