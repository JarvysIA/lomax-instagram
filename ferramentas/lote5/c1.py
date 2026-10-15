from base import *

N = 6
def cnt(i): return f'<div class="count">{i}/{N}</div>'

css = """
.big{font-size:104px}
.rec{background:#fff;color:#0A192C;border-radius:18px;padding:48px 52px;position:relative;
     box-shadow:0 30px 60px rgba(0,0,0,.35);font-variant-numeric:tabular-nums}
.rl{display:flex;justify-content:space-between;font-size:44px;padding:26px 0;border-bottom:2px dashed #cfd8e3}
.rl:last-child{border:0}
.rl b{font-weight:800}
.dots{display:grid;grid-template-columns:repeat(5,1fr);gap:26px;margin-top:56px}
.dot{height:118px;border-radius:22px;background:#0E8DFE;display:flex;align-items:center;justify-content:center;font-size:54px}
.dot.off{background:transparent;border:3px dashed #3d4f68;opacity:.9}
.price{display:flex;align-items:center;gap:36px;margin-top:40px}
.p1{white-space:nowrap;font-size:96px;font-weight:900;font-style:italic;color:#56657a;text-decoration:line-through;text-decoration-thickness:8px}
.p2{white-space:nowrap;font-size:170px;font-weight:900;font-style:italic;color:#0E8DFE;letter-spacing:-4px}
.arrow{font-size:90px;color:#fff;font-weight:900}
.li{display:flex;gap:28px;align-items:flex-start;margin-bottom:34px}
.ic{flex:none;width:68px;height:68px;border-radius:18px;background:#0E8DFE;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-style:italic;font-size:36px}
.li p{font-size:38px;line-height:1.28;font-weight:500}
.cta{background:#0E8DFE;color:#fff;border-radius:28px;padding:46px 50px}
"""

s = []
# 1 capa
s.append(("l5_c1_1", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:330px;left:96px;right:96px">
<div class="h big">O lead que<br>ninguém respondeu<br><span class="blue">custou o dobro.</span></div>
<div class="b" style="font-size:42px;margin-top:44px;line-height:1.35">Parece exagero. Faz a conta comigo. 👉</div>
</div>{logo(False)}<div class="foot">Arraste para o lado</div></div>""", css)))
# 2 nota do anúncio
s.append(("l5_c1_2", page(f"""<div class="s dark">{cnt(2)}
<div style="position:absolute;top:250px;left:96px;right:96px">
<div class="h" style="font-size:78px">Você coloca R$ 400<br>em anúncio.</div>
<div class="rec" style="margin-top:64px">
<div class="tag" style="color:#6a788c;margin-bottom:10px">Resumo do mês</div>
<div class="rl"><span>Investimento</span><b>R$ 400</b></div>
<div class="rl"><span>Pessoas que chamaram</span><b>20</b></div>
<div class="rl"><span>Custo por contato</span><b style="color:#0E8DFE">R$ 20</b></div>
</div></div>
<div class="note">Exemplo com números redondos.</div>{logo()}</div>""", css)))
# 3 metade esquecida
dots = "".join('<div class="dot">✓</div>' for _ in range(10)) + "".join('<div class="dot off"></div>' for _ in range(10))
s.append(("l5_c1_3", page(f"""<div class="s dark">{cnt(3)}
<div style="position:absolute;top:230px;left:96px;right:96px">
<div class="h" style="font-size:78px">Mas na correria,<br><span class="blue">só 10 recebem resposta.</span></div>
<div class="dots">{dots}</div>
<div class="b" style="font-size:36px;margin-top:44px;line-height:1.35">Os outros 10 ficaram no meio das conversas. Nem você sabe quem eram.</div>
</div>{logo()}</div>""", css)))
# 4 preço real
s.append(("l5_c1_4", page(f"""<div class="s dark">{cnt(4)}
<div style="position:absolute;top:270px;left:96px;right:96px">
<div class="b" style="font-size:40px">O custo de cada cliente atendido</div>
<div class="price"><span class="p1">R$ 20</span><span class="arrow">→</span><span class="p2">R$ 40</span></div>
<div class="h" style="font-size:66px;margin-top:40px">Lead sem resposta não é lead.<br><span class="blue">É verba jogada fora.</span></div>
</div>{logo()}</div>""", css)))
# 5 solução
s.append(("l5_c1_5", page(f"""<div class="s dark">{cnt(5)}
<div style="position:absolute;top:210px;left:96px;right:96px">
<div class="h" style="font-size:70px">Antes de aumentar a verba,<br><span class="blue">pare de perder quem já chegou.</span></div>
<div style="margin-top:60px">
<div class="li"><div class="ic">1</div><p>Toda conversa nova vira um card em <b>Novo</b>. Ninguém fica no meio da lista.</p></div>
<div class="li"><div class="ic">2</div><p>A equipe vê quem está esperando e há quanto tempo, e responde pelo computador.</p></div>
<div class="li"><div class="ic">3</div><p>Sumiu depois do orçamento? Até <b>5 retornos automáticos</b>, que param quando o cliente responde.</p></div>
<div class="li"><div class="ic">4</div><p>Veio de anúncio do Meta? A origem aparece no card.</p></div>
</div></div>{logo()}</div>""", css)))
# 6 CTA
s.append(("l5_c1_6", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="h" style="font-size:96px">Cada lead<br>atendido.<br><span class="blue">Cada real valendo.</span></div>
<div class="cta" style="margin-top:64px">
<div style="font-size:46px;font-weight:800">Teste o Lomax CRM 30 dias grátis</div>
<div style="font-size:34px;margin-top:12px;opacity:.92">Sem cartão. Depois, R$ 99,90/mês com 2 usuários.</div>
</div>
<div class="b" style="font-size:34px;margin-top:36px">Link na bio. 🔗</div>
</div>{logo(False)}</div>""", css)))

if __name__ == "__main__":
    render_pngs(s, "/home/claude/l5/out")
    print("ok")
