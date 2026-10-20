from base import *
from c5 import css as css5

N = 4
def cnt(i): return f'<div class="count">{i}/{N}</div>'

css = css5 + """
.num{display:flex;align-items:center;gap:22px;background:#fff;border-radius:22px;padding:22px 28px;margin-bottom:16px;box-shadow:0 10px 30px rgba(10,25,44,.08)}
.num .d{flex:none;width:58px;height:58px;border-radius:50%;background:#25D366;display:flex;align-items:center;justify-content:center;font-size:30px}
.num p{font-size:32px;font-weight:700;color:#0A192C}
.num span{display:block;font-size:24px;font-weight:500;color:#6a788c;margin-top:2px}
.eq{display:inline-block;border-radius:12px;padding:6px 16px;font-size:24px;font-weight:800;margin-right:8px}
"""

s = []
s.append(("l6_c3_1", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:200px;left:96px;right:96px">
<div class="num"><div class="d">📞</div><p>Vendas<span>(21) 9 xxxx-0001</span></p></div>
<div class="num"><div class="d">📞</div><p>Oficina<span>(21) 9 xxxx-0002</span></p></div>
<div class="num"><div class="d">📞</div><p>Financeiro<span>(21) 9 xxxx-0003</span></p></div>
<div class="h" style="font-size:84px;margin-top:56px">Um número pra cada setor?</div>
<div class="h" style="font-size:84px;margin-top:18px"><span class="pl">Seu cliente se perde.</span></div>
</div><div class="note">Números ilustrativos.</div>{logo(False)}<div class="foot">Arraste para o lado</div></div>""", css)))

s.append(("l6_c3_2", page(f"""<div class="s dark">{cnt(2)}
<div style="position:absolute;top:220px;left:96px;right:96px">
<div class="h" style="font-size:66px;margin-bottom:46px">O que acontece <span class="blue">na prática:</span></div>
<div class="hr"><div class="t">01</div><p>Cliente salva três contatos e manda pro errado.</p></div>
<div class="hr"><div class="t">02</div><p>Explica tudo de novo quando passam ele pro setor certo.</p></div>
<div class="hr"><div class="t">03</div><p>Cada chip num celular diferente. Ninguém vê o todo.</p></div>
<div class="hr"><div class="t">04</div><p>O atendente sai e o número vai junto com a conversa.</p></div>
</div>{logo()}</div>""", css)))

s.append(("l6_c3_3", page(f"""<div class="s dark">{cnt(3)}
<div style="position:absolute;top:200px;left:96px;right:96px">
<div class="h" style="font-size:72px">Um número.</div>
<div class="h blue" style="font-size:72px;margin-bottom:28px">Todas as equipes.</div>
<div style="margin-bottom:44px"><span class="eq" style="background:#0E8DFE">Vendas</span><span class="eq" style="background:#f59e0b;color:#0A192C">Oficina</span><span class="eq" style="background:#22c55e;color:#0A192C">Financeiro</span></div>
<div class="ok"><div class="i">👥</div><p><b>Equipes no mesmo número:</b> o cliente salva um contato só.</p></div>
<div class="ok"><div class="i">🔁</div><p><b>Transferência:</b> a conversa passa pra equipe certa com o histórico junto. Ninguém repete nada.</p></div>
<div class="ok"><div class="i">🔒</div><p><b>Quem vê o quê:</b> perfis de admin, gerente e atendente.</p></div>
</div>{logo()}</div>""", css)))

s.append(("l6_c3_4", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:260px;left:96px;right:96px">
<div class="h" style="font-size:84px">Um WhatsApp só</div>
<div class="h" style="font-size:84px;margin-top:18px"><span class="pl">pra empresa toda.</span></div>
<div class="b" style="font-size:38px;margin-top:44px;line-height:1.4">Feito no Rio, no balcão de uma oficina de verdade. A equipe toda atende pelo computador, no mesmo número.</div>
<div style="margin-top:40px"><span class="chip">💬 Suporte em tudo pelo WhatsApp</span><span class="chip">🎥 Ajuda por vídeo com hora marcada</span></div>
<div class="cta" style="margin-top:30px">
<div style="font-size:44px;font-weight:800">Teste 30 dias grátis</div>
<div style="font-size:32px;margin-top:10px;opacity:.92">Sem cartão. Link na bio.</div>
</div></div>{logo(False)}</div>""", css)))

if __name__ == "__main__":
    render_pngs(s, "/home/claude/l5/out")
    print("ok")
