"""Stories do lote S2 (21/10): 10 stories, 1 por dia, só com o que o Lomax faz hoje."""
from stories import page, logo, who, ini, headline, NOTE, faq, W, H
from base import render_pngs

S = []

S.append(("ls_16_suporte", page(headline("Travou na configuração?", "A gente te ajuda.", size=92, top=300) + """
<div style='position:absolute;left:84px;right:84px;top:760px;display:flex;flex-direction:column;gap:30px;align-items:center'>
<div class='ui' style='width:100%;display:flex;align-items:center;gap:26px'><div style='font-size:80px'>💬</div><div><div class='nm'>Suporte em tudo pelo WhatsApp</div><div class='msg' style='white-space:normal;max-width:none'>Do cadastro ao primeiro cliente no funil.</div></div></div>
<div class='ui' style='width:100%;display:flex;align-items:center;gap:26px'><div style='font-size:80px'>🎥</div><div><div class='nm'>Ajuda por vídeo com hora marcada</div><div class='msg' style='white-space:normal;max-width:none'>A gente configura junto com você.</div></div></div>
</div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1340px'>Ninguém fica sozinho no teste de 30 dias.</div>""" + logo())))

S.append(("ls_17_carioca", page("""
<div class='head' style='top:330px'><div class='t1' style='font-size:108px'>Feito por carioca,<br><span class='pill'>pra carioca.</span></div></div>
<div class='lead' style='position:absolute;left:110px;right:110px;top:790px;color:#c9d6e8'>O Lomax nasceu no balcão de uma oficina no Rio, com o WhatsApp lotado de cliente. Se você atende pelo WhatsApp aqui, ele foi feito pra você.</div>
<div style='position:absolute;left:0;right:0;top:1180px;text-align:center'><span class='chipbig'>Teste 30 dias grátis</span></div>""" + logo("dark"), "dark")))

S.append(("ls_18_barra", page(headline("Digita “/”", "e a resposta aparece.", size=100, top=290) + """
<div class='panel' style='top:740px'><div class='ui'>
<div style='background:#eef2f7;border-radius:18px;padding:20px 24px;font-size:32px;font-weight:700'>/pre<span style='opacity:.4'>|</span></div>
<div class='row' style='margin-top:10px'><div class='tag t-blue' style='margin:0;font-family:monospace;font-size:28px'>/preco</div><div class='msg' style='margin-left:10px'>Valores e formas de pagamento</div></div>
<div class='row'><div class='tag t-gry' style='margin:0;font-family:monospace;font-size:28px'>/prazo</div><div class='msg' style='margin-left:10px'>Quanto tempo leva</div></div>
<div class='row'><div class='tag t-gry' style='margin:0;font-family:monospace;font-size:28px'>/agendar</div><div class='msg' style='margin-left:10px'>Marcar horário</div></div>
</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1330px'>Mensagens rápidas: a equipe toda responde igual, em segundos.</div>""" + logo() + "<div class='note'>Exemplo. Os atalhos você cria do seu jeito.</div>")))

S.append(("ls_19_espera", page("""
<div class='head' style='top:300px'><div class='t1' style='font-size:96px'>Quanto tempo seu<br><span class='pill'>cliente espera?</span></div></div>
<div style='position:absolute;left:84px;right:84px;top:720px;display:flex;flex-direction:column;gap:24px'>
<div class='ui' style='display:flex;align-items:center;gap:24px'><span style='font-size:60px'>⚡</span><div class='nm'>Menos de 5 minutos</div></div>
<div class='ui' style='display:flex;align-items:center;gap:24px'><span style='font-size:60px'>⏳</span><div class='nm'>Uma hora ou mais</div></div>
<div class='ui' style='display:flex;align-items:center;gap:24px;border:4px solid #ef4444'><span style='font-size:60px'>😬</span><div class='nm'>Só amanhã</div></div>
</div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1330px'>No Lomax, o funil mostra quem está esperando e há quanto tempo.</div>""" + logo())))

S.append(("ls_20_anuncio", page(headline("Veio do anúncio?", "O card avisa.", top=300) + """
<div class='panel' style='top:720px'><div class='ui'><h5>Novo</h5>
<div class='row'>""" + ini("RS", "#e3f0ff", "#0b6fd0") + """<div><div class='nm'>Rafael Souza</div><div class='msg'>Vi o anúncio, quanto fica?</div></div><span class='tag t-blue'>📣 Anúncio</span></div>
<div class='row'>""" + ini("JL", "#e1f6e9", "#1f8a4c") + """<div><div class='nm'>Juliana Lima</div><div class='msg'>Oi! Tem horário sábado?</div></div><span class='tag t-blue'>📣 Anúncio</span></div>
<div class='row'>""" + ini("BT", "#fff3d1", "#9a6500") + """<div><div class='nm'>Bruno Teixeira</div><div class='msg'>Bom dia, tudo bem?</div></div><span class='tag t-gry'>Direto</span></div>
</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1330px'>Você sabe quem a campanha trouxe e não deixa ninguém esperando.</div>""" + logo() + NOTE)))

S.append(("ls_21_quem_respondeu", page(headline("Quem respondeu?", "Tá escrito.", top=300) + """
<div class='panel' style='top:720px'><div class='ui'>
<div style='background:#eef2f7;border-radius:22px 22px 22px 6px;padding:22px 26px;font-size:30px;margin-right:140px'>Meu carro fica pronto hoje?</div>
<div style='margin-top:18px;background:#0E8DFE;color:#fff;border-radius:22px 22px 6px 22px;padding:22px 26px;font-size:30px;margin-left:100px'><b>Paulo:</b><br>Fica sim! Às 17h pode buscar 🙂</div>
<div style='margin-top:18px;background:#0E8DFE;color:#fff;border-radius:22px 22px 6px 22px;padding:22px 26px;font-size:30px;margin-left:100px'><b>Carla:</b><br>Já deixei o Pix aqui embaixo.</div>
</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1330px'>Cada mensagem sai com o nome de quem atendeu.</div>""" + logo() + NOTE)))

S.append(faq("ls_22_cartao", "Precisa de cartão pra testar?", "Não.",
  "São 30 dias grátis, sem cartão. Depois, R$ 99,90 por mês com 2 usuários, no Pix ou boleto."))

S.append(faq("ls_23_equipe", "Minha equipe toda pode usar?", "Pode.",
  "Todo mundo atende no mesmo número, pelo computador. 2 usuários inclusos e R$ 49,90 por usuário extra."))

S.append(("ls_24_vaga", page(headline("Atendente saiu?", "A vaga fica.", top=300) + """
<div class='panel' style='top:720px'><div class='ui'><h5>Usuários · 2 de 2 vagas</h5>
<div class='row'>""" + who("G") + """<div><div class='nm'>Gabriel</div><div class='msg'>Admin</div></div></div>
<div class='row' style='opacity:.45'>""" + who("V") + """<div><div class='nm' style='text-decoration:line-through'>Vitor</div><div class='msg'>Saiu da empresa</div></div></div>
<div class='row'>""" + who("P") + """<div><div class='nm'>Patrícia</div><div class='msg'>Entrou na mesma vaga</div></div><span class='tag t-grn'>R$ 0 a mais</span></div>
</div></div>
<div class='sub' style='position:absolute;left:84px;right:84px;top:1330px'>Conversas e histórico ficam na empresa. Quem chega já encontra tudo.</div>""" + logo() + NOTE)))

S.append(("ls_25_bora", page("""
<div class='head' style='top:330px'><div class='t1' style='font-size:108px'>Bora organizar<br><span class='pill'>esse WhatsApp?</span></div></div>
<div class='lead' style='position:absolute;left:110px;right:110px;top:800px;color:#c9d6e8'>30 dias grátis, sem cartão. Suporte pelo WhatsApp do primeiro ao último dia.</div>
<div style='position:absolute;left:0;right:0;top:1080px;text-align:center'><span class='chipbig'>👆 Toque no link</span></div>""" + logo("dark"), "dark")))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/stories", w=W, h=H)
    print(len(S))
