from base import *

N = 5
def cnt(i): return f'<div class="count">{i}/{N}</div>'

css = """
.pl{display:inline-block;background:#0E8DFE;color:#fff;padding:2px 26px 8px;border-radius:18px;transform:rotate(-2deg)}
.hr{display:flex;align-items:center;gap:28px;background:#16253a;border-radius:24px;padding:26px 30px;margin-bottom:18px}
.hr .t{flex:none;width:150px;font-weight:900;font-style:italic;font-size:44px;color:#ff6b78}
.hr p{font-size:34px;font-weight:600;line-height:1.25}
.ok{display:flex;gap:24px;align-items:flex-start;margin-bottom:30px}
.ok .i{flex:none;width:64px;height:64px;border-radius:18px;background:#0E8DFE;display:flex;align-items:center;justify-content:center;font-size:34px}
.ok p{font-size:36px;line-height:1.3;font-weight:500}
.ok b{font-weight:800}
.cta{background:#0E8DFE;color:#fff;border-radius:28px;padding:44px 50px}
.chip{display:inline-block;background:#fff;color:#0A192C;border-radius:999px;padding:14px 26px;font-size:28px;font-weight:700;margin:0 12px 14px 0;box-shadow:0 8px 24px rgba(10,25,44,.08)}
"""

s = []
s.append(("l6_c2_1", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:290px;left:96px;right:96px">
<div class="h" style="font-size:94px">Você abriu uma empresa.</div>
<div class="h" style="font-size:94px;margin-top:22px"><span class="pl">Não um plantão</span></div>
<div class="h" style="font-size:94px;margin-top:22px">de WhatsApp.</div>
<div class="b" style="font-size:40px;margin-top:50px">Se o celular não sai da sua mão, arrasta pro lado. 👉</div>
</div>{logo(False)}<div class="foot">Arraste para o lado</div></div>""", css)))

s.append(("l6_c2_2", page(f"""<div class="s dark">{cnt(2)}
<div style="position:absolute;top:220px;left:96px;right:96px">
<div class="h" style="font-size:66px;margin-bottom:46px">Seu dia, do jeito <span class="blue">que tá hoje:</span></div>
<div class="hr"><div class="t">07:10</div><p>Respondendo orçamento antes do café.</p></div>
<div class="hr"><div class="t">12:30</div><p>Almoço com uma mão. A outra no WhatsApp.</p></div>
<div class="hr"><div class="t">19:40</div><p>"Alguém respondeu a cliente de ontem?" Ninguém sabe.</p></div>
<div class="hr"><div class="t">DOM</div><p>Praia, família... e você conferindo mensagem.</p></div>
</div>{logo()}</div>""", css)))

s.append(("l6_c2_3", page(f"""<div class="s dark">{cnt(3)}
<div style="position:absolute;top:260px;left:96px;right:96px">
<div class="h" style="font-size:80px">O problema não é<br>o WhatsApp.</div>
<div class="h blue" style="font-size:80px;margin-top:16px">É tudo depender de você.</div>
<div class="b" style="font-size:40px;margin-top:54px;line-height:1.4">Quando só o dono sabe quem respondeu, quem tá esperando e quem precisa de retorno, a empresa para quando o dono para.</div>
</div>{logo()}</div>""", css)))

s.append(("l6_c2_4", page(f"""<div class="s dark">{cnt(4)}
<div style="position:absolute;top:200px;left:96px;right:96px">
<div class="h" style="font-size:72px;margin-bottom:56px">No Lomax, <span class="blue">a equipe segura.</span></div>
<div class="ok"><div class="i">👥</div><p><b>A equipe toda no mesmo número</b>, atendendo pelo computador. Seu celular sai do centro.</p></div>
<div class="ok"><div class="i">🔀</div><p><b>Distribuição automática:</b> cada conversa nova já cai com um atendente.</p></div>
<div class="ok"><div class="i">📋</div><p><b>Funil por etapas:</b> você bate o olho e vê quem tá esperando, sem perguntar pra ninguém.</p></div>
<div class="ok"><div class="i">⏰</div><p><b>Retornos automáticos</b> em horário comercial, pra quem pediu orçamento e sumiu.</p></div>
</div>{logo()}</div>""", css)))

s.append(("l6_c2_5", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:250px;left:96px;right:96px">
<div class="h" style="font-size:80px">Feito no Rio,</div>
<div class="h" style="font-size:80px;margin-top:10px">numa oficina</div>
<div class="h" style="font-size:80px;margin-top:18px"><span class="pl">de verdade.</span></div>
<div class="b" style="font-size:38px;margin-top:44px;line-height:1.4">O Lomax nasceu no balcão de um auto center carioca, pra resolver exatamente esse plantão.</div>
<div style="margin-top:40px"><span class="chip">💬 Suporte em tudo pelo WhatsApp</span><span class="chip">🎥 Ajuda por vídeo com hora marcada</span></div>
<div class="cta" style="margin-top:30px">
<div style="font-size:44px;font-weight:800">Teste 30 dias grátis</div>
<div style="font-size:32px;margin-top:10px;opacity:.92">Sem cartão. Link na bio.</div>
</div></div>{logo(False)}</div>""", css)))

if __name__ == "__main__":
    render_pngs(s, "/home/claude/l5/out")
    print("ok")
