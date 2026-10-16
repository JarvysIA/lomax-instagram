"""Stories 1080x1920 do Lomax (lote S1) + capas de destaque."""
from base import *

W, H = 1080, 1920
LOGO_D = f"file://{ROOT}/logo_on_dark.png"
LOGO_L = f"file://{ROOT}/logo_on_light.png"

CSS = """
.st{position:relative;width:1080px;height:1920px;overflow:hidden;padding:0 84px}
.st.light{background:radial-gradient(circle at 50% 38%,#ffffff 0,#ECF3FB 60%) ,#ECF3FB;color:#0A192C}
.st.dark{background:linear-gradient(#0A192C,#0c2240);color:#fff}
.dots{position:absolute;inset:0;background-image:radial-gradient(rgba(14,141,254,.13) 2px,transparent 2px);background-size:46px 46px;opacity:.55}
.dark .dots{background-image:radial-gradient(rgba(255,255,255,.07) 2px,transparent 2px)}
.t1{font-weight:900;font-style:italic;font-size:118px;letter-spacing:-3px;line-height:1;text-align:center}
.pill{display:inline-block;background:#0E8DFE;color:#fff;border-radius:26px;padding:6px 34px 16px;transform:rotate(-1.5deg);box-shadow:0 18px 40px rgba(14,141,254,.35)}
.head{position:absolute;left:0;right:0;top:300px;text-align:center}
.sub{font-size:40px;font-weight:500;text-align:center;margin-top:44px;color:#3f4d60;line-height:1.3}
.dark .sub{color:#c9d6e8}
.panel{position:absolute;left:84px;right:84px;background:#dfeaf7;border-radius:48px;padding:34px}
.dark .panel{background:#122238}
.ui{background:#fff;border-radius:34px;box-shadow:0 24px 60px rgba(10,25,44,.14);padding:30px 34px;color:#0A192C}
.ui h5{font-size:34px;font-weight:800;margin-bottom:10px}
.row{display:flex;align-items:center;gap:22px;padding:22px 0;border-top:2px solid #eef2f7}
.row:first-of-type{border-top:0}
.ini{flex:none;width:76px;height:76px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px}
.nm{font-weight:800;font-size:31px}
.msg{font-size:25px;color:#5a6a80;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:430px}
.tag{margin-left:auto;flex:none;font-weight:700;font-size:23px;padding:8px 16px;border-radius:12px}
.who{flex:none;width:62px;height:62px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:24px;border:4px solid #fff;box-shadow:0 4px 12px rgba(0,0,0,.15)}
.t-blue{background:#e3f0ff;color:#0b6fd0}.t-yel{background:#fff3d1;color:#9a6500}.t-grn{background:#e1f6e9;color:#1f8a4c}.t-red{background:#ffe3e6;color:#c22a3c}.t-gry{background:#eef1f5;color:#56657a}
.logo{position:absolute;left:0;right:0;bottom:290px;text-align:center}
.logo img{height:58px}
.note{position:absolute;left:0;right:0;bottom:250px;text-align:center;font-size:21px;color:#7d8a9c}
.big{font-weight:900;font-style:italic;letter-spacing:-4px}
.q{font-weight:900;font-style:italic;font-size:92px;letter-spacing:-2px;line-height:1.02;text-align:center}
.ans{display:inline-block;font-weight:900;font-style:italic;font-size:200px;letter-spacing:-6px;color:#0E8DFE;line-height:1}
.lead{font-size:42px;line-height:1.35;text-align:center;font-weight:500}
.chipbig{display:inline-block;background:#0E8DFE;color:#fff;border-radius:999px;padding:24px 48px;font-weight:800;font-size:44px}
"""

def page(body, theme="light"):
    css = BASE_CSS.replace("width:1080px;height:1350px", "width:1080px;height:1920px")
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}{CSS}</style></head><body><div class='st {theme}'><div class='dots'></div>{body}</div></body></html>"

def logo(theme="light"):
    return f"<div class='logo'><img src='{LOGO_L if theme=='light' else LOGO_D}'></div>"

COL = {"G": "#0E8DFE", "P": "#22c55e", "R": "#f59e0b", "C": "#8b5cf6", "V": "#ef4444"}
def who(letter): return f"<div class='who' style='background:{COL[letter]}'>{letter}</div>"
def ini(txt, bg, fg): return f"<div class='ini' style='background:{bg};color:{fg}'>{txt}</div>"

def headline(a, b, top=300, size=118):
    return f"<div class='head' style='top:{top}px'><div class='t1' style='font-size:{size}px'>{a}<br><span class='pill'>{b}</span></div></div>"

NOTE = "<div class='note'>Imagem ilustrativa, com dados fictícios.</div>"

S = []

# S1 Cada cliente com dono
S.append(("ls_01_com_dono", page(headline("Cada cliente", "com dono.") + """
<div class='panel' style='top:720px'><div class='ui'><h5>Em atendimento</h5>
<div class='row'>""" + ini("AL","#e1f6e9","#1f8a4c") + """<div><div class='nm'>Ana Lima</div><div class='msg'>Pode ser sábado às 9h?</div></div><span class='tag t-blue'>Vendas</span>""" + who("G") + """</div>
<div class='row'>""" + ini("JR","#fff3d1","#9a6500") + """<div><div class='nm'>João Reis</div><div class='msg'>Meu carro fica pronto hoje?</div></div><span class='tag t-yel'>Oficina</span>""" + who("P") + """</div>
<div class='row'>""" + ini("CS","#e3f0ff","#0b6fd0") + """<div><div class='nm'>Clara Souza</div><div class='msg'>Manda o Pix, por favor</div></div><span class='tag t-grn'>Financeiro</span>""" + who("R") + """</div>
<div class='row'>""" + ini("MP","#f1e8ff","#6d3fd0") + """<div><div class='nm'>Marcos Pinto</div><div class='msg'>Quanto fica a revisão?</div></div><span class='tag t-blue'>Vendas</span>""" + who("C") + """</div>
</div></div>""" + logo() + NOTE)))

# S2 retorno sozinho
S.append(("ls_02_retorno", page(headline("Sumiu? O retorno", "sai sozinho.", size=104, top=270) + """
<div class='panel' style='top:700px'><div class='ui'>
<div style='display:flex;align-items:center;gap:20px'>""" + ini("MP","#f1e8ff","#6d3fd0") + """<div><div class='nm'>Marcos Pinto</div><div class='msg'>Revisão completa · R$ 480</div></div><span class='tag t-red'>Sem resposta</span></div>
<div style='margin-top:26px;display:grid;grid-template-columns:repeat(5,1fr);gap:12px'>
<div class='tag t-blue' style='text-align:center;margin:0'>1º ✓</div><div class='tag t-blue' style='text-align:center;margin:0'>2º ✓</div><div class='tag t-gry' style='text-align:center;margin:0'>3º</div><div class='tag t-gry' style='text-align:center;margin:0'>4º</div><div class='tag t-gry' style='text-align:center;margin:0'>5º</div></div>
<div style='margin-top:26px;background:#0E8DFE;color:#fff;border-radius:22px 22px 6px 22px;padding:22px 26px;font-size:29px;margin-left:80px'>Oi, Marcos! Conseguiu ver o orçamento? Tenho horário amanhã às 9h 🙂</div>
<div style='margin-top:16px;background:#eef2f7;border-radius:22px 22px 22px 6px;padding:22px 26px;font-size:29px;margin-right:120px'>Vi sim! Pode marcar 🙌</div>
<div style='margin-top:22px;text-align:center'><span class='tag t-grn' style='font-size:25px'>✓ Respondeu: os retornos param</span></div>
</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1390px'>Até 5 retornos automáticos, direto da nuvem.</div>""" + logo() + NOTE)))

# S3 confirmação de agendamento
S.append(("ls_03_confirmacao", page(headline("Marcou? A confirmação", "vai sozinha.", size=96, top=270) + """
<div class='panel' style='top:700px'><div class='ui'>
<div style='display:flex;align-items:center;gap:20px'><div style='width:120px;height:130px;border-radius:22px;background:#0A192C;color:#fff;text-align:center;padding-top:12px'><div style='font-size:24px;font-weight:700;color:#8fa3bd'>SÁB</div><div style='font-size:64px;font-weight:900'>18</div></div>
<div><div class='nm'>Ana Lima · 9h00</div><div class='msg'>Troca de pastilhas de freio</div><span class='tag t-grn' style='display:inline-block;margin-top:10px'>Agendado</span></div></div>
<div style='margin-top:28px;font-size:24px;color:#7d8a9c;text-align:center'>Sexta, 10h00 · enviada automaticamente</div>
<div style='margin-top:12px;background:#0E8DFE;color:#fff;border-radius:22px 22px 6px 22px;padding:22px 26px;font-size:29px;margin-left:60px'>Oi, Ana! Confirmando seu horário amanhã, sábado, às 9h. Podemos contar com você? 🚗</div>
<div style='margin-top:16px;background:#eef2f7;border-radius:22px 22px 22px 6px;padding:22px 26px;font-size:29px;margin-right:200px'>Confirmado! 👍</div>
</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1400px'>Sem ligar para ninguém. Menos falta, agenda cheia.</div>""" + logo() + NOTE)))

# S4 distribuição automática
S.append(("ls_04_distribuicao", page(headline("Chegou lead?", "Já tem dono.") + """
<div class='panel' style='top:720px'><div class='ui'>
<div style='display:flex;align-items:center;gap:20px;background:#f5f9ff;border-radius:22px;padding:18px'>""" + ini("RF","#e3f0ff","#0b6fd0") + """<div><div class='nm'>Rafael Freitas</div><div class='msg'>Vi o anúncio, quero saber o preço</div></div><span class='tag t-blue'>Novo</span></div>
<div style='text-align:center;font-size:60px;color:#0E8DFE;margin:6px 0'>↓</div>
<div style='text-align:center;font-weight:800;font-size:30px'>Distribuição automática</div>
<div style='display:flex;justify-content:center;gap:34px;margin-top:22px'>
<div style='text-align:center;opacity:.45'>""" + who("P") + """<div style='font-size:22px;margin-top:8px'>Paula</div></div>
<div style='text-align:center;transform:scale(1.25)'>""" + who("G") + """<div style='font-size:22px;margin-top:8px;font-weight:800'>Gustavo</div></div>
<div style='text-align:center;opacity:.45'>""" + who("R") + """<div style='font-size:22px;margin-top:8px'>Rita</div></div></div>
<div style='margin-top:30px;text-align:center'><span class='tag t-grn' style='font-size:26px'>✓ Rafael agora é do Gustavo</span></div>
</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1360px'>Você escolhe quem recebe. Ninguém fica sem resposta esperando alguém pegar.</div>""" + logo() + NOTE)))

# S5 transferência
S.append(("ls_05_transferencia", page(headline("Passou pra outro?", "Com todo o histórico.", size=96) + """
<div class='panel' style='top:700px'><div class='ui'>
<div style='display:flex;align-items:center;justify-content:center;gap:28px'>
<div style='text-align:center'>""" + who("G") + """<div style='font-size:24px;margin-top:8px;font-weight:700'>Gustavo<br><span style='color:#7d8a9c;font-weight:500'>Vendas</span></div></div>
<div style='font-size:70px;color:#0E8DFE'>→</div>
<div style='text-align:center'>""" + who("R") + """<div style='font-size:24px;margin-top:8px;font-weight:700'>Rita<br><span style='color:#7d8a9c;font-weight:500'>Financeiro</span></div></div></div>
<div style='margin-top:28px;font-size:27px'>
<div style='padding:14px 18px;background:#f5f9ff;border-radius:14px;margin-bottom:10px'>💬 Conversa completa desde o 1º "oi"</div>
<div style='padding:14px 18px;background:#f5f9ff;border-radius:14px;margin-bottom:10px'>📄 Orçamento: R$ 1.250</div>
<div style='padding:14px 18px;background:#f5f9ff;border-radius:14px'>📝 Observação: "pagar no Pix, 2x"</div></div>
</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1360px'>Transfere para outro atendente ou equipe. O cliente não precisa explicar de novo.</div>""" + logo() + NOTE)))

# S6 visibilidade
S.append(("ls_06_visibilidade", page(headline("Cada um vê", "o que é seu.") + """
<div class='panel' style='top:720px'><div class='ui'>
<div class='row'><div class='ini' style='background:#0A192C;color:#fff'>👑</div><div><div class='nm'>Admin</div><div class='msg'>Vê tudo e decide o que os outros podem</div></div></div>
<div class='row'><div class='ini' style='background:#0E8DFE;color:#fff'>📊</div><div><div class='nm'>Gerente</div><div class='msg'>Acompanha a equipe</div></div></div>
<div class='row'><div class='ini' style='background:#e3f0ff;color:#0b6fd0'>💬</div><div><div class='nm'>Atendente</div><div class='msg'>Foca nos clientes dele</div></div></div>
</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1340px'>Permissões por perfil, no mesmo número de WhatsApp.</div>""" + logo() + NOTE)))

# S7 preço
S.append(("ls_07_preco", page("""
<div class='head' style='top:280px'><div class='t1' style='font-size:96px'>Quanto custa<br><span class='pill'>o Lomax CRM?</span></div></div>
<div class='panel' style='top:690px'><div class='ui' style='text-align:center;padding:46px 34px'>
<div style='font-size:34px;font-weight:700;color:#5a6a80'>30 dias grátis, sem cartão. Depois:</div>
<div class='big' style='font-size:190px;color:#0E8DFE;line-height:1;margin-top:14px'>R$ 99,90</div>
<div style='font-size:38px;font-weight:800'>por mês, com 2 usuários</div>
<div style='margin-top:30px;display:flex;flex-direction:column;gap:12px;font-size:30px;text-align:left'>
<div>➕ Usuário extra: R$ 49,90/mês</div><div>💸 Sem cobrança por mensagem</div><div>🧾 Pix ou boleto</div></div>
</div></div>""" + logo())))

# Dúvidas
def faq(name, q, a, txt, theme="dark"):
    return (name, page(f"""
<div class='head' style='top:300px'><div class='tag' style='display:inline-block;background:#0E8DFE;color:#fff;font-size:28px;letter-spacing:3px;padding:12px 26px;border-radius:14px'>DÚVIDA FREQUENTE</div>
<div class='q' style='margin-top:50px'>{q}</div></div>
<div style='position:absolute;left:0;right:0;top:880px;text-align:center'><span class='ans'>{a}</span></div>
<div class='lead' style='position:absolute;left:110px;right:110px;top:1140px'>{txt}</div>""" + logo(theme), theme))

S.append(faq("ls_08_computador", "Preciso deixar o computador ligado?", "Não.",
  "O Lomax roda na nuvem. Retornos e confirmações saem com o seu computador desligado."))
S.append(faq("ls_09_numero", "Uso o mesmo número que já tenho?", "Sim.",
  "Você conecta pelo QR Code, como no WhatsApp Web. A equipe toda atende nesse número, pelo computador."))
S.append(faq("ls_10_bloqueio", "Meu número pode ser bloqueado?", "Pode.",
  "Com qualquer ferramenta, e até sem nenhuma. O Lomax reduz o risco: envios em horário comercial, com limites, e retorno que para quando o cliente responde."))
S.append(faq("ls_11_mensagem", "Pago por mensagem enviada?", "Não.",
  "Mensalidade fixa. Atenda à vontade: a conta não muda com o número de mensagens."))

# S12 isso ou aquilo
S.append(("ls_12_caderno_funil", page("""
<div class='head' style='top:300px'><div class='t1' style='font-size:104px'>Onde estão<br><span class='pill'>seus clientes?</span></div></div>
<div style='position:absolute;left:84px;right:84px;top:700px;display:flex;gap:30px'>
<div class='ui' style='flex:1;text-align:center;padding:40px 20px;background:#fff8e6'>
<div style='font-size:120px'>📒</div><div class='nm' style='margin-top:10px'>No caderno</div>
<div class='msg' style='white-space:normal;max-width:none;margin-top:12px'>"Ligar pro Marcos"<br>... qual Marcos?</div></div>
<div class='ui' style='flex:1;text-align:center;padding:40px 20px;border:4px solid #0E8DFE'>
<div style='font-size:120px'>🗂️</div><div class='nm' style='margin-top:10px'>No funil</div>
<div class='msg' style='white-space:normal;max-width:none;margin-top:12px'>Marcos · Sem resposta<br>2º retorno enviado</div></div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1290px'>Se você respondeu "no caderno", o Lomax foi feito pra você.</div>""" + logo())))

# S13 bastidores
S.append(("ls_13_oficina", page("""
<div class='head' style='top:320px'><div class='t1' style='font-size:100px'>Nasceu no balcão<br><span class='pill'>de uma oficina.</span></div></div>
<div class='lead' style='position:absolute;left:110px;right:110px;top:760px'>O Lomax foi criado e testado todos os dias numa oficina de verdade, no Rio de Janeiro, com o WhatsApp lotado de clientes.</div>
<div style='position:absolute;left:84px;right:84px;top:1110px;display:flex;gap:22px;justify-content:center'>
<div class='chipbig' style='background:#16253a;font-size:34px'>🔧 Feito na prática</div><div class='chipbig' style='background:#16253a;font-size:34px'>💬 Usado todo dia</div></div>""" + logo("dark"), "dark")))

# S14 CTA
S.append(("ls_14_teste", page("""
<div class='head' style='top:320px'><div class='t1' style='font-size:110px'>Teste grátis<br><span class='pill'>por 30 dias.</span></div></div>
<div class='lead' style='position:absolute;left:110px;right:110px;top:780px;color:#c9d6e8'>Sem cartão. Conecta o seu WhatsApp pelo QR Code e já começa a organizar hoje.</div>
<div style='position:absolute;left:0;right:0;top:1060px;text-align:center'><span class='chipbig'>👆 Toque no link</span></div>""" + logo("dark"), "dark")))

# Capas de destaque
ICONS = {
 "como_funciona": "<path d='M20 30h60M20 50h60M20 70h36' stroke='#fff' stroke-width='9' stroke-linecap='round'/>",
 "equipe": "<circle cx='36' cy='38' r='12' fill='#fff'/><circle cx='66' cy='38' r='12' fill='#fff'/><path d='M14 78c2-14 12-22 22-22s20 8 22 22M44 78c2-14 12-22 22-22s20 8 22 22' fill='#fff'/>",
 "precos": "<text x='50' y='70' text-anchor='middle' font-family='Barlow' font-weight='900' font-style='italic' font-size='58' fill='#fff'>R$</text>",
 "duvidas": "<text x='50' y='76' text-anchor='middle' font-family='Barlow' font-weight='900' font-style='italic' font-size='78' fill='#fff'>?</text>",
}
for k, svg in ICONS.items():
    S.append((f"capa_{k}", f"""<!doctype html><html><head><meta charset='utf-8'><style>{font_faces()}*{{margin:0}}body{{width:1080px;height:1920px;background:#0A192C;display:flex;align-items:center;justify-content:center}}
.c{{width:620px;height:620px;border-radius:50%;background:#0E8DFE;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 22px rgba(14,141,254,.18)}}</style></head>
<body><div class='c'><svg viewBox='0 0 100 100' width='340' height='340'>{svg}</svg></div></body></html>"""))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/stories", w=W, h=H)
    print(len(S))
