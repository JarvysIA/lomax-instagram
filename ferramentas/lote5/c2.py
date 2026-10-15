from base import *

N = 6
def cnt(i): return f'<div class="count">{i}/{N}</div>'

css = """
.li{display:flex;gap:26px;align-items:flex-start;margin-bottom:30px}
.ic{flex:none;width:62px;height:62px;border-radius:16px;background:#0E8DFE;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:34px}
.ic.no{background:#ff4d5e}
.li p{font-size:37px;line-height:1.28;font-weight:500}
.stamp{display:inline-block;border:5px solid #0E8DFE;color:#0E8DFE;border-radius:14px;padding:10px 24px;font-weight:900;font-style:italic;font-size:44px;transform:rotate(-4deg);letter-spacing:1px}
.fine{font-size:24px;color:#6a788c;line-height:1.5;border-top:2px solid #26364d;padding-top:22px}
.qr{width:150px;height:150px;border-radius:18px;background:
 conic-gradient(from 90deg at 30% 30%,#fff 25%,transparent 0) 0 0/50px 50px,#0E8DFE;opacity:.95}
.cta{background:#0E8DFE;color:#fff;border-radius:28px;padding:46px 50px}
"""

s = []
s.append(("l5_c2_1", page(f"""<div class="s dark">{STRIPES}
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="tag" style="margin-bottom:28px">Pergunta que todo mundo faz</div>
<div class="h" style="font-size:98px">Meu número<br>pode ser bloqueado<br><span class="blue">se eu usar o Lomax?</span></div>
<div class="b" style="font-size:42px;margin-top:44px">A resposta honesta, sem letra miúda. 👉</div>
</div>{logo()}<div class="foot">Arraste para o lado</div></div>""", css)))

s.append(("l5_c2_2", page(f"""<div class="s dark">{cnt(2)}
<div style="position:absolute;top:260px;left:96px;right:96px">
<div class="stamp">RESPOSTA CURTA: PODE.</div>
<div class="h" style="font-size:74px;margin-top:56px">Com qualquer ferramenta.<br><span class="blue">E até sem nenhuma.</span></div>
<div class="b" style="font-size:38px;margin-top:44px;line-height:1.38">O próprio WhatsApp bloqueia números pelos critérios dele, principalmente quando recebe <b style="color:#fff">denúncias</b> ou vê <b style="color:#fff">envio em massa para quem não conhece a empresa</b>.</div>
</div>{logo()}</div>""", css)))

s.append(("l5_c2_3", page(f"""<div class="s dark">{cnt(3)}
<div style="position:absolute;top:240px;left:96px;right:96px">
<div class="tag">Como o Lomax conecta</div>
<div class="h" style="font-size:76px;margin-top:22px">Pelo QR Code,<br><span class="blue">como no WhatsApp Web.</span></div>
<div class="card" style="margin-top:50px">
<div class="li"><div class="ic">✓</div><p>Você usa o número que já tem.</p></div>
<div class="li"><div class="ic">✓</div><p>Sem cobrança por mensagem.</p></div>
<div class="li" style="margin:0"><div class="ic no">!</div><p>Não é a API oficial da Meta. Por isso o risco de bloqueio existe, como em toda ferramenta desse tipo.</p></div>
</div></div>{logo()}</div>""", css)))

s.append(("l5_c2_4", page(f"""<div class="s dark">{cnt(4)}
<div style="position:absolute;top:220px;left:96px;right:96px">
<div class="h" style="font-size:74px">O que o Lomax faz<br><span class="blue">para reduzir o risco</span></div>
<div style="margin-top:56px">
<div class="li"><div class="ic">1</div><p>Mensagens automáticas só em <b>horário comercial</b>.</p></div>
<div class="li"><div class="ic">2</div><p>Envios em <b>horários variados</b> e com <b>limites</b>, nada de rajada.</p></div>
<div class="li"><div class="ic">3</div><p>O retorno automático <b>para quando o cliente responde</b>. Ninguém fica insistindo.</p></div>
<div class="li"><div class="ic">4</div><p><b>"Não perturbe"</b> para quem pediu para parar de receber.</p></div>
</div></div>{logo()}</div>""", css)))

s.append(("l5_c2_5", page(f"""<div class="s dark">{cnt(5)}
<div style="position:absolute;top:220px;left:96px;right:96px">
<div class="h" style="font-size:74px">O que<br><span class="blue">depende de você</span></div>
<div style="margin-top:56px">
<div class="li"><div class="ic no">✕</div><p>Comprar lista ou mandar para quem nunca falou com a empresa.</p></div>
<div class="li"><div class="ic no">✕</div><p>Disparar a mesma mensagem para centenas de contatos de uma vez.</p></div>
<div class="li"><div class="ic">✓</div><p>Falar com quem te procurou, com texto natural e o nome do cliente.</p></div>
<div class="li"><div class="ic">✓</div><p>Parar na hora quando alguém pedir.</p></div>
</div></div>{logo()}</div>""", css)))

s.append(("l5_c2_6", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:290px;left:96px;right:96px">
<div class="h" style="font-size:90px">Quem promete<br>risco zero<br><span class="blue">está te enganando.</span></div>
<div class="b" style="font-size:38px;margin-top:36px;line-height:1.35">A gente prefere te contar antes. E te ajudar a usar do jeito certo.</div>
<div class="cta" style="margin-top:50px">
<div style="font-size:44px;font-weight:800">Teste 30 dias grátis, sem cartão</div>
<div style="font-size:32px;margin-top:10px;opacity:.92">Link na bio. Dúvidas? Chama no WhatsApp da Lomax.</div>
</div></div>{logo(False)}</div>""", css)))

if __name__ == "__main__":
    render_pngs(s, "/home/claude/l5/out")
    print("ok")
