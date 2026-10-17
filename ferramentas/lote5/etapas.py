from stories import page as spage, headline, logo as slogo, NOTE, ini, who
from base import page as fpage, STRIPES, logo as flogo, render_pngs

ROWS = [
 ("Novo", "t-blue", "🟦", "Cliente chamou pela 1ª vez", "Oi! Recebemos sua mensagem 😊 Já já um atendente fala com você."),
 ("Sem resposta", "t-red", "🔁", "Sumiu depois do orçamento", "Oi! Conseguiu ver o orçamento? Se quiser, reservo um horário."),
 ("Agendado", "t-grn", "📅", "Dia anterior ao horário", "Confirmando seu horário amanhã às 9h. Podemos contar com você?"),
]

def rows(fs=1.0):
    h = ""
    for i, (et, cls, ic, quando, msg) in enumerate(ROWS):
        top = "" if i == 0 else "border-top:2px solid #eef2f7;"
        h += f"""<div style='display:flex;gap:{int(22*fs)}px;padding:{int(26*fs)}px 0;{top}'>
<div style='flex:none;width:{int(210*fs)}px'><span class='tag {cls}' style='display:inline-block;margin:0;font-size:{int(24*fs)}px'>{et}</span>
<div style='font-size:{int(22*fs)}px;color:#7d8a9c;margin-top:10px;line-height:1.25'>{quando}</div></div>
<div style='flex:1'><div style='background:#eef4fb;border-radius:20px 20px 20px 6px;padding:{int(16*fs)}px {int(20*fs)}px;font-size:{int(26*fs)}px;line-height:1.3'>{msg}</div>
<div style='color:#0E8DFE;font-weight:700;font-size:{int(22*fs)}px;margin-top:10px'>⚡ Enviada automaticamente</div></div></div>"""
    return h

story = spage(headline("Cada etapa do funil", "com a mensagem certa.", size=92, top=290) + f"""
<div class='panel' style='top:680px'><div class='ui'>{rows()}</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1400px'>Você escreve uma vez. O Lomax envia sempre, no momento certo.</div>""" + slogo() + NOTE)

FCSS = """.tag{display:inline-block;font-weight:700;padding:8px 16px;border-radius:12px}.t-blue{background:#e3f0ff;color:#0b6fd0}.t-red{background:#ffe3e6;color:#c22a3c}.t-grn{background:#e1f6e9;color:#1f8a4c}
.pnl{position:absolute;left:96px;right:96px;background:#dfeaf7;border-radius:40px;padding:26px}.ui{background:#fff;border-radius:28px;box-shadow:0 20px 50px rgba(10,25,44,.12);padding:6px 30px;color:#0A192C}
.pill{display:inline-block;background:#0E8DFE;color:#fff;border-radius:22px;padding:2px 26px 12px;transform:rotate(-1.5deg)}"""
feed = fpage(f"""<div class="s light">
<div style="position:absolute;top:120px;left:0;right:0;text-align:center"><div class="h" style="font-size:78px">Cada etapa do funil<br><span class="pill">com a mensagem certa.</span></div></div>
<div class="pnl" style="top:400px"><div class="ui">{rows(0.92)}</div></div>
<div style="position:absolute;left:96px;right:96px;top:1120px;text-align:center;font-size:32px;color:#3f4d60">Você escreve uma vez. O Lomax envia sempre.</div>
{flogo(False).replace('class="logo"','class="logo" style="left:50%;transform:translateX(-50%);bottom:70px"')}
<div style="position:absolute;right:96px;bottom:86px;font-size:20px;color:#7d8a9c"></div></div>""", FCSS)

render_pngs([("ls_15_etapas", story)], "/home/claude/l5/stories", w=1080, h=1920)
render_pngs([("l6_s1_etapas", feed)], "/home/claude/l5/out")
print("ok")
