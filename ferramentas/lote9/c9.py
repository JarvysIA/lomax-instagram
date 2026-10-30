"""Lote 9 (30/10): tema "o que o Lomax faz sozinho" (automação que já existe) + Rio. 5 carrosséis + 7 posts únicos."""
from base import *
from c8 import css as css8
from c7 import cta

css = css8 + """
.tl2{position:relative;padding-left:70px}
.tl2:before{content:'';position:absolute;left:22px;top:12px;bottom:12px;width:4px;background:#2a3b52}
.ev{position:relative;margin-bottom:30px;background:#16253a;border-radius:22px;padding:22px 28px}
.ev:before{content:'';position:absolute;left:-58px;top:26px;width:28px;height:28px;border-radius:50%;background:#0E8DFE;box-shadow:0 0 0 6px #0A192C}
.ev .t{font-size:26px;font-weight:800;color:#7fc0ff;letter-spacing:1px}
.ev p{font-size:34px;font-weight:600;margin-top:6px;line-height:1.28}
.mv{display:flex;gap:24px;align-items:flex-start;margin-bottom:26px}
.mv .bd{flex:none;width:190px;text-align:center;border-radius:16px;padding:12px 0;font-weight:900;font-style:italic;font-size:34px}
.mv p{font-size:36px;line-height:1.3;font-weight:500}
.mv b{font-weight:800}
.big{font-weight:900;font-style:italic;font-size:220px;line-height:.85;color:#0E8DFE;letter-spacing:-4px}
.niche{display:inline-block;background:#fff;color:#0A192C;border-radius:999px;padding:16px 30px;font-size:34px;font-weight:700;margin:0 14px 18px 0;box-shadow:0 8px 24px rgba(10,25,44,.08)}
.bigok .ok{margin-bottom:46px}.bigok .ok p{font-size:40px}.bigok .ok .i{width:72px;height:72px;font-size:38px}
.biglist .mv{margin-bottom:46px}.biglist .mv p{font-size:40px}
.card2{background:#fff;color:#0A192C;border-radius:26px;padding:30px 34px;box-shadow:0 18px 40px rgba(0,0,0,.25)}
"""


def cnt(i, n): return f'<div class="count">{i}/{n}</div>'


def cover(name, l1, l2, pill, sub, dark=False, size=96):
    cls = "dark" if dark else "light"
    return (name, page(f"""<div class="s {cls}">{'' if dark else STRIPES}
<div style="position:absolute;top:290px;left:96px;right:96px">
<div class="h" style="font-size:{size}px">{l1}</div>
{f'<div class="h" style="font-size:{size}px;margin-top:14px">{l2}</div>' if l2 else ''}
<div class="h" style="font-size:{size}px;margin-top:24px"><span class="pl">{pill}</span></div>
<div class="b" style="font-size:40px;margin-top:52px">{sub}</div>
</div>{logo(dark)}<div class="foot">Arraste para o lado</div></div>""", css))


S = []

# ---------- C1: seu CRM trabalha ou só guarda contato? ----------
S.append(cover("l9_c1_1", "Seu CRM trabalha", "ou só guarda", "contato?", "5 coisas que o Lomax faz sozinho, todo dia. 👉"))
S.append(("l9_c1_2", page(f"""<div class="s dark">{cnt(2,4)}
<div style="position:absolute;top:220px;left:96px;right:96px" class="bigok">
<div class="h" style="font-size:72px;margin-bottom:60px">Sem ninguém <span class="blue">lembrar de nada:</span></div>
<div class="ok"><div class="i">🔀</div><p><b>Distribui</b> cada conversa nova pra um atendente.</p></div>
<div class="ok"><div class="i">⏰</div><p><b>Chama de volta</b> quem pediu orçamento e sumiu, até 5 vezes, em horário comercial.</p></div>
<div class="ok"><div class="i">📅</div><p><b>Confirma o horário</b> marcado no dia anterior.</p></div>
<div class="ok"><div class="i">📣</div><p><b>Marca no card</b> quem veio do anúncio.</p></div>
<div class="ok"><div class="i">✍️</div><p><b>Assina</b> cada mensagem com o nome de quem respondeu.</p></div>
</div>{logo()}</div>""", css)))
S.append(("l9_c1_3", page(f"""<div class="s dark">{cnt(3,4)}
<div style="position:absolute;top:280px;left:96px;right:96px">
<div class="h" style="font-size:80px">E tudo isso</div>
<div class="h blue" style="font-size:80px;margin-top:14px">com o computador desligado.</div>
<div class="b" style="font-size:40px;margin-top:54px;line-height:1.42">O Lomax roda na nuvem. Os retornos e as confirmações saem no horário certo mesmo depois que você fecha a loja. E o retorno para sozinho quando o cliente responde.</div>
</div>{logo()}</div>""", css)))
S.append(("l9_c1_4", page(cta("Automático,", "com o seu texto.", "Você escreve a mensagem uma vez, do seu jeito. O Lomax só envia na hora certa, no seu número."), css)))

# ---------- C2: retorno automático, como funciona ----------
S.append(cover("l9_c2_1", "Retorno automático:", "", "como funciona?", "As 5 perguntas que mais recebemos. 👉", dark=True, size=88))
FAQ = [("Quantas vezes ele chama?", "Até <b>5 retornos</b> automáticos pra quem sumiu."),
       ("E se o cliente responder?", "<b>Para na hora.</b> Ninguém recebe cobrança depois que já respondeu."),
       ("Manda de madrugada?", "Não. Os envios automáticos saem <b>só em horário comercial</b>."),
       ("Preciso deixar o PC ligado?", "Não. Roda <b>na nuvem</b>, mesmo com tudo desligado."),
       ("Quem escreve a mensagem?", "<b>Você.</b> Sai com o seu texto, no seu número.")]
items = "".join(f'<div class="mv"><div class="bd" style="background:#0E8DFE;font-size:30px;width:70px">{i+1}</div><p><b>{q}</b><br>{a}</p></div>' for i, (q, a) in enumerate(FAQ))
S.append(("l9_c2_2", page(f"""<div class="s dark">{cnt(2,3)}
<div class="biglist" style="position:absolute;top:190px;left:96px;right:96px">{items}</div>{logo()}</div>""", css)))
S.append(("l9_c2_3", page(cta("Cliente sumido", "volta a responder.", "O retorno automático do Lomax chama de novo quem pediu orçamento e esfriou, sem você precisar lembrar."), css)))

# ---------- C3: confirmação de agendamento ----------
S.append(cover("l9_c3_1", "Cliente marcou", "e não apareceu?", "De novo?", "Furo na agenda tem remédio simples. 👉"))
S.append(("l9_c3_2", page(f"""<div class="s dark">{cnt(2,4)}
<div style="position:absolute;top:220px;left:96px;right:96px">
<div class="h" style="font-size:70px;margin-bottom:50px">O furo quase sempre é <span class="blue">esquecimento.</span></div>
<div class="b" style="font-size:40px;line-height:1.45">Ninguém marca um horário pensando em faltar. A pessoa marca na segunda, a semana passa e o compromisso some da cabeça.</div>
<div class="b" style="font-size:40px;line-height:1.45;margin-top:34px">E ligar pra confirmar um por um vira mais uma tarefa que ninguém tem tempo de fazer.</div>
</div>{logo()}</div>""", css)))
S.append(("l9_c3_3", page(f"""<div class="s dark">{cnt(3,4)}
<div style="position:absolute;top:190px;left:96px;right:96px">
<div class="h" style="font-size:66px;margin-bottom:40px">No Lomax, <span class="blue">a confirmação vai sozinha:</span></div>
<div class="chat">
<div class="bo">Oi, Carlos! Passando pra confirmar seu horário amanhã, sábado, às 9h. Tudo certo? 🙂<small>sexta · 10:00 · automático</small></div>
<div class="bi">Confirmado, tô lá! 👍<small>10:12</small></div>
</div>
<div class="b" style="font-size:36px;margin-top:36px;line-height:1.4">O cliente marcou? O Lomax manda a confirmação <b style="color:#fff">no dia anterior</b>, com o texto que você escolheu.</div>
</div><div class="note">Exemplo ilustrativo, com dados fictícios.</div>{logo()}</div>""", css)))
S.append(("l9_c3_4", page(cta("Agenda cheia", "de quem aparece.", "Serve pra oficina, clínica, salão, pet shop: todo negócio que marca horário pelo WhatsApp."), css)))

# ---------- C4: mito ou verdade ----------
S.append(cover("l9_c4_1", "CRM de WhatsApp:", "", "mito ou verdade?", "5 dúvidas que travam quem quer se organizar. 👉", size=90))
MV = [("MITO", "#ff6b78", "<b>“Preciso deixar o computador ligado.”</b> O Lomax roda na nuvem."),
      ("MITO", "#ff6b78", "<b>“Quando o atendente sai, leva os clientes.”</b> A conversa e o histórico ficam na empresa."),
      ("VERDADE", "#22c55e", "<b>“A equipe toda atende no mesmo número.”</b> Cada um no seu computador."),
      ("MITO", "#ff6b78", "<b>“Pago por cada mensagem.”</b> No Lomax não tem cobrança por mensagem."),
      ("MITO", "#ff6b78", "<b>“É difícil de configurar.”</b> A gente configura junto, por vídeo com hora marcada.")]
items = "".join(f'<div class="mv"><div class="bd" style="background:{c};color:#0A192C">{t}</div><p>{p}</p></div>' for t, c, p in MV)
S.append(("l9_c4_2", page(f"""<div class="s dark">{cnt(2,3)}
<div class="biglist" style="position:absolute;top:190px;left:96px;right:96px">{items}</div>{logo()}</div>""", css)))
S.append(("l9_c4_3", page(cta("Ficou alguma", "dúvida?", "Pergunta pra gente no WhatsApp. Suporte em tudo, do cadastro ao primeiro cliente no funil."), css)))

# ---------- C5: pra quem é ----------
S.append(cover("l9_c5_1", "O Lomax é pra", "o seu negócio?", "Arrasta e vê.", "Se você atende cliente pelo WhatsApp, a resposta é sim. 👉", size=92))
NICHOS = ["🔧 Oficinas e auto centers", "🦷 Clínicas e consultórios", "🏠 Imobiliárias", "🐾 Pet shops e veterinárias",
          "📱 Assistências técnicas", "🛍️ Lojas e e-commerce", "📚 Escolas e cursos", "✂️ Salões e estética"]
S.append(("l9_c5_2", page(f"""<div class="s light">{cnt(2,3)}
<div style="position:absolute;top:200px;left:96px;right:96px">
<div class="h" style="font-size:66px;margin-bottom:48px">Quem já atende <span class="pl">pelo WhatsApp:</span></div>
{''.join(f'<span class="niche">{n}</span>' for n in NICHOS)}
<div class="b" style="font-size:36px;margin-top:30px;line-height:1.4">Se tem mais de uma pessoa respondendo, ou cliente que pede orçamento e some, o Lomax resolve.</div>
</div>{logo(False)}</div>""", css)))
S.append(("l9_c5_3", page(cta(), css)))

# ---------- posts únicos ----------
def single(name, l1, l2, pill, body, dark=True, note="", size=104):
    cls = "dark" if dark else "light"
    return (name, page(f"""<div class="s {cls}">{'' if dark else STRIPES}
<div style="position:absolute;top:270px;left:96px;right:96px">
<div class="h" style="font-size:{size}px">{l1}</div>
{f'<div class="h" style="font-size:{size}px;margin-top:14px">{l2}</div>' if l2 else ''}
<div class="h" style="font-size:{size}px;margin-top:24px"><span class="pl">{pill}</span></div>
<div class="b" style="font-size:40px;margin-top:56px;line-height:1.42">{body}</div>
</div>{f'<div class="note">{note}</div>' if note else ''}{logo(dark)}</div>""", css))


S.append(single("l9_s1_18h", "Sua loja fecha", "às 18h.", "O retorno não.",
    "Quem pediu orçamento hoje e sumiu recebe o retorno automático amanhã, em horário comercial. Com o computador desligado e você em casa."))
S.append(single("l9_s2_robo", "Automático", "", "não é robô.",
    "No Lomax, a mensagem automática é a sua: o seu texto, no seu número, na hora certa. Quem conversa com o cliente continua sendo a sua equipe.", dark=False))
S.append(("l9_s3_lembra", page(f"""<div class="s dark">
<div style="position:absolute;top:260px;left:96px;right:96px">
<div class="h" style="font-size:84px">O cliente não lembra</div>
<div class="h" style="font-size:84px;margin-top:14px">que você esqueceu.</div>
<div class="h" style="font-size:84px;margin-top:30px"><span class="pl">Lembra quem</span></div>
<div class="h" style="font-size:84px;margin-top:14px">respondeu primeiro.</div>
<div class="b" style="font-size:40px;margin-top:56px;line-height:1.42">Com cada conversa nova já caindo com um atendente, quem responde primeiro pode ser a sua empresa.</div>
</div>{logo()}</div>""", css)))
S.append(("l9_s4_confirma", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:240px;left:96px;right:96px">
<div class="h" style="font-size:96px">Amanhã, 9h.</div>
<div class="h" style="font-size:96px;margin-top:20px"><span class="pl">Confirmado. ✅</span></div>
<div class="card2" style="margin-top:56px">
<div style="font-size:24px;font-weight:800;color:#0E8DFE;letter-spacing:2px">CONFIRMAÇÃO AUTOMÁTICA · DIA ANTERIOR</div>
<div style="font-size:36px;margin-top:14px;line-height:1.35">“Oi, Juliana! Confirmando seu horário amanhã às 9h. Tudo certo?”</div>
<div style="font-size:30px;margin-top:18px;color:#1f8a4c;font-weight:800">Juliana: “Confirmadíssimo!” 🙌</div>
</div>
<div class="b" style="font-size:36px;margin-top:40px;line-height:1.4">Menos falta na agenda, sem ninguém ligar pra confirmar.</div>
</div><div class="note">Exemplo ilustrativo, com dados fictícios.</div>{logo(False)}</div>""", css)))
S.append(("l9_s5_setores", page(f"""<div class="s dark">
<div style="position:absolute;top:250px;left:96px;right:96px">
<div style="display:flex;gap:40px;align-items:flex-end"><div class="big">1</div><div class="h" style="font-size:64px;padding-bottom:16px">número.</div></div>
<div style="display:flex;gap:40px;align-items:flex-end;margin-top:20px"><div class="big">3</div><div class="h" style="font-size:64px;padding-bottom:16px">equipes.</div></div>
<div style="display:flex;gap:40px;align-items:flex-end;margin-top:20px"><div class="big" style="color:#22c55e">0</div><div class="h" style="font-size:64px;padding-bottom:16px">confusão.</div></div>
<div class="b" style="font-size:38px;margin-top:56px;line-height:1.4">Vendas, oficina e financeiro no mesmo WhatsApp. A conversa passa pra equipe certa com o histórico junto.</div>
</div>{logo()}</div>""", css)))
S.append(single("l9_s6_vaga", "O atendente saiu.", "", "Os clientes ficaram.",
    "No Lomax, as conversas e o histórico são da empresa. Quem entra na vaga encontra tudo, e trocar o usuário não custa nada a mais.", dark=False, size=96))
S.append(single("l9_s7_anuncio", "Veio do anúncio?", "", "O card avisa.",
    "O Lomax marca no card quem chegou pela campanha do Instagram ou do Facebook. Você sabe o que o anúncio trouxe e não deixa ninguém esperando."))

if __name__ == "__main__":
    import sys
    only = sys.argv[1:]
    items = [x for x in S if not only or any(x[0].startswith(o) for o in only)]
    render_pngs(items, "/home/claude/l5/out9")
    print(len(items))
