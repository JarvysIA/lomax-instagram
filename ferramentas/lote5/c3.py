from base import *

N = 6
def cnt(i): return f'<div class="count">{i}/{N}</div>'

css = """
.badge{display:inline-block;background:#0E8DFE;color:#fff;font-weight:800;font-size:28px;letter-spacing:2px;padding:12px 22px;border-radius:12px;text-transform:uppercase}
.num{font-size:200px;font-weight:900;font-style:italic;color:#0E8DFE;letter-spacing:-6px;line-height:.9}
.row{display:flex;gap:28px;margin-top:40px}
.box{flex:1;border-radius:24px;padding:34px 34px;background:#16253a}
.box h4{font-size:26px;letter-spacing:2px;text-transform:uppercase;color:#8796ab;font-weight:800;margin-bottom:14px}
.box p{font-size:36px;line-height:1.25;font-weight:600}
.ok{border:3px solid #0E8DFE}
.li{display:flex;gap:26px;align-items:flex-start;margin-bottom:30px}
.ic{flex:none;width:62px;height:62px;border-radius:16px;background:#0E8DFE;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:34px}
.li p{font-size:37px;line-height:1.28;font-weight:500}
.cta{background:#0E8DFE;color:#fff;border-radius:28px;padding:46px 50px}
"""

s = []
s.append(("l5_c3_1", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:290px;left:96px;right:96px">
<div class="badge">Desde 1º de outubro</div>
<div class="h" style="font-size:100px;margin-top:34px">O WhatsApp<br>começou a cobrar<br><span class="blue">por mensagem?</span></div>
<div class="b" style="font-size:42px;margin-top:40px">O que mudou de verdade, sem pânico. 👉</div>
</div>{logo(False)}<div class="foot">Arraste para o lado</div></div>""", css)))

s.append(("l5_c3_2", page(f"""<div class="s dark">{cnt(2)}
<div style="position:absolute;top:250px;left:96px;right:96px">
<div class="tag">O que mudou</div>
<div class="h" style="font-size:72px;margin-top:22px">Na <span class="blue">API oficial</span> do WhatsApp, responder o cliente passou a ter custo.</div>
<div class="b" style="font-size:38px;margin-top:44px;line-height:1.38">As respostas dentro da janela de 24 horas, as chamadas <b style="color:#fff">mensagens de atendimento</b>, eram grátis. Agora são cobradas depois de uma franquia mensal.</div>
</div>{logo()}</div>""", css)))

s.append(("l5_c3_3", page(f"""<div class="s dark">{cnt(3)}
<div style="position:absolute;top:220px;left:96px;right:96px">
<div class="tag">Os números</div>
<div class="num" style="margin-top:30px">1.000</div>
<div class="h" style="font-size:52px;margin-top:10px">mensagens de atendimento grátis<br>por mês, por número.</div>
<div class="row">
<div class="box"><h4>Passou disso</h4><p>Cada mensagem é cobrada</p></div>
<div class="box"><h4>Estimativa</h4><p>Cerca de R$ 0,04 por mensagem</p></div>
</div>
</div><div class="note">A Meta ainda não publicou o valor final em reais. A estimativa é do mercado e pode mudar.</div>{logo()}</div>""", css)))

s.append(("l5_c3_4", page(f"""<div class="s dark">{cnt(4)}
<div style="position:absolute;top:250px;left:96px;right:96px">
<div class="tag">Quem não foi afetado</div>
<div class="h" style="font-size:74px;margin-top:22px">Usa o app no celular?<br><span class="blue">Continua sem pagar por mensagem.</span></div>
<div class="b" style="font-size:38px;margin-top:44px;line-height:1.38">A cobrança é da plataforma de API, usada por sistemas que conectam pela via oficial. O aplicativo WhatsApp e o WhatsApp Business seguem como antes.</div>
</div>{logo()}</div>""", css)))

s.append(("l5_c3_5", page(f"""<div class="s dark">{cnt(5)}
<div style="position:absolute;top:220px;left:96px;right:96px">
<div class="h" style="font-size:80px">E no Lomax?</div>
<div style="margin-top:50px">
<div class="li"><div class="ic">✓</div><p>Conecta pelo QR Code, como o WhatsApp Web. Não usa a API oficial.</p></div>
<div class="li"><div class="ic">✓</div><p><b>Mensalidade fixa:</b> R$ 99,90 com 2 usuários. A conta não muda com o número de mensagens.</p></div>
<div class="li"><div class="ic">!</div><p>A conexão pelo QR Code tem o risco de bloqueio que toda ferramenta desse tipo tem. Explicamos tudo num post só sobre isso.</p></div>
</div></div>{logo()}</div>""", css)))

s.append(("l5_c3_6", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="h" style="font-size:96px">Atenda à vontade.<br><span class="blue">A mensalidade<br>não muda.</span></div>
<div class="cta" style="margin-top:60px">
<div style="font-size:44px;font-weight:800">Teste o Lomax CRM 30 dias grátis</div>
<div style="font-size:32px;margin-top:10px;opacity:.92">Sem cartão. Link na bio.</div>
</div></div>{logo(False)}</div>""", css)))

if __name__ == "__main__":
    render_pngs(s, "/home/claude/l5/out")
    print("ok")
