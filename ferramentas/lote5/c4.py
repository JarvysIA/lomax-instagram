from base import *

N = 5
def cnt(i): return f'<div class="count">{i}/{N}</div>'

css = """
.q{display:flex;gap:26px;align-items:center;background:#16253a;border-radius:24px;padding:28px 30px;margin-bottom:22px}
.qn{flex:none;width:72px;height:72px;border-radius:18px;background:#0E8DFE;display:flex;align-items:center;justify-content:center;font-weight:900;font-style:italic;font-size:40px}
.q p{font-size:44px;font-weight:800}
.strike{position:relative;display:inline-block;color:#8796ab}
.strike:after{content:"";position:absolute;left:-6px;right:-6px;top:52%;height:8px;background:#ff4d5e;transform:rotate(-3deg);border-radius:4px}
.slash{font-family:monospace;font-weight:700;background:#0b1522;border:2px solid #26364d;border-radius:16px;padding:16px 22px;font-size:34px;margin-bottom:14px;display:flex;justify-content:space-between}
.slash span{color:#8fa3bd;font-family:'Barlow';font-weight:500;font-size:28px}
.cta{background:#0E8DFE;color:#fff;border-radius:28px;padding:46px 50px}
"""

s = []
s.append(("l6_c1_1", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="h" style="font-size:96px">Seu cliente não quer<br><span class="strike">"excelência".</span></div>
<div class="h blue" style="font-size:96px;margin-top:18px">Ele quer 4 respostas.</div>
<div class="b" style="font-size:42px;margin-top:44px">E rápido. Arraste para ver. 👉</div>
</div>{logo(False)}<div class="foot">Arraste para o lado</div></div>""", css)))

s.append(("l6_c1_2", page(f"""<div class="s dark">{cnt(2)}
<div style="position:absolute;top:230px;left:96px;right:96px">
<div class="b" style="font-size:38px;line-height:1.35;margin-bottom:40px">"Qualidade", "compromisso", "o melhor atendimento"... seu concorrente diz a mesma coisa. Quem chama no WhatsApp quer saber:</div>
<div class="q"><div class="qn">1</div><p>Quanto custa?</p></div>
<div class="q"><div class="qn">2</div><p>Quanto tempo demora?</p></div>
<div class="q"><div class="qn">3</div><p>Como funciona?</p></div>
<div class="q"><div class="qn">4</div><p>Qual é o próximo passo?</p></div>
</div>{logo()}</div>""", css)))

s.append(("l6_c1_3", page(f"""<div class="s dark">{cnt(3)}
<div style="position:absolute;top:250px;left:96px;right:96px">
<div class="h" style="font-size:78px">Quem responde isso primeiro,<br><span class="blue">leva o cliente.</span></div>
<div class="b" style="font-size:40px;margin-top:50px;line-height:1.38">Enquanto você digita a mesma explicação pela décima vez no dia, o cliente já pediu orçamento em outro lugar.</div>
</div>{logo()}</div>""", css)))

s.append(("l6_c1_4", page(f"""<div class="s dark">{cnt(4)}
<div style="position:absolute;top:210px;left:96px;right:96px">
<div class="h" style="font-size:72px">Deixe as 4 respostas<br><span class="blue">prontas no Lomax.</span></div>
<div class="b" style="font-size:34px;margin:30px 0 34px">Digite "/" e a mensagem aparece. Toda a equipe responde igual e em segundos.</div>
<div class="slash">/preco <span>Valores e formas de pagamento</span></div>
<div class="slash">/prazo <span>Quanto tempo leva</span></div>
<div class="slash">/como <span>Como funciona o serviço</span></div>
<div class="slash">/agendar <span>Próximo passo: marcar horário</span></div>
</div><div class="note">Exemplo de mensagens rápidas. Os atalhos você cria do seu jeito.</div>{logo()}</div>""", css)))

s.append(("l6_c1_5", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="h" style="font-size:92px">Menos frase bonita.<br><span class="blue">Mais resposta rápida.</span></div>
<div class="cta" style="margin-top:64px">
<div style="font-size:44px;font-weight:800">Teste o Lomax CRM 30 dias grátis</div>
<div style="font-size:32px;margin-top:10px;opacity:.92">Sem cartão. Link na bio.</div>
</div></div>{logo(False)}</div>""", css)))

if __name__ == "__main__":
    render_pngs(s, "/home/claude/l5/out")
    print("ok")
