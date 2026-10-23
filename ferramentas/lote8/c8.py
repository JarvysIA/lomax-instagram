"""Carrossel l8_c1 (23/10): "Quanto custa?" não se responde só com o preço. Ideia recriada a partir da checagem diária."""
from base import *
from c7 import css as css7, cta

css = css7 + """
.chat{background:#0b1522;border-radius:28px;padding:34px 30px}
.bi{background:#1e2c40;color:#fff;border-radius:24px 24px 24px 6px;padding:20px 26px;font-size:34px;margin:0 140px 18px 0;display:inline-block}
.bo{background:#0E8DFE;color:#fff;border-radius:24px 24px 6px 24px;padding:20px 26px;font-size:34px;margin:0 0 18px 120px;display:block}
.bo small,.bi small{display:block;font-size:20px;opacity:.7;margin-top:6px;text-align:right}
.part{display:flex;gap:26px;align-items:flex-start;margin-bottom:34px}
.part .n{flex:none;width:72px;height:72px;border-radius:20px;background:#0E8DFE;display:flex;align-items:center;justify-content:center;font-weight:900;font-style:italic;font-size:42px}
.part p{font-size:38px;line-height:1.3;font-weight:500}
.part b{font-weight:800}
"""
N = 5
def cnt(i): return f'<div class="count">{i}/{N}</div>'

S = []
S.append(("l8_c1_1", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:300px;left:96px;right:96px">
<div class="h" style="font-size:120px">“Quanto custa?”</div>
<div class="h" style="font-size:96px;margin-top:30px">Não responda</div>
<div class="h" style="font-size:96px;margin-top:20px"><span class="pl">só o preço.</span></div>
<div class="b" style="font-size:40px;margin-top:56px">A resposta que vende tem 3 partes. Arrasta. 👉</div>
</div>{logo(False)}<div class="foot">Arraste para o lado</div></div>""", css)))

S.append(("l8_c1_2", page(f"""<div class="s dark">{cnt(2)}
<div style="position:absolute;top:210px;left:96px;right:96px">
<div class="h" style="font-size:66px;margin-bottom:44px">O preço seco <span style="color:#ff6b78">termina assim:</span></div>
<div class="chat">
<div class="bi">Quanto fica a troca de óleo?<small>09:12</small></div>
<div class="bo">R$ 189.<small>09:40</small></div>
<div class="bi">Ok, vou ver. 👍<small>09:41</small></div>
<div style="text-align:center;font-size:26px;color:#8796ab;margin-top:16px">e nunca mais respondeu</div>
</div>
<div class="b" style="font-size:36px;margin-top:40px;line-height:1.4">Só o número, o cliente compara com o mais barato da rua. E some.</div>
</div><div class="note">Exemplo ilustrativo.</div>{logo()}</div>""", css)))

S.append(("l8_c1_3", page(f"""<div class="s dark">{cnt(3)}
<div style="position:absolute;top:230px;left:96px;right:96px">
<div class="h" style="font-size:70px;margin-bottom:60px">A resposta que vende <span class="blue">tem 3 partes:</span></div>
<div class="part"><div class="n">1</div><p><b>Uma pergunta rápida</b> pra entender o caso do cliente.</p></div>
<div class="part"><div class="n">2</div><p><b>O preço com o que está incluso</b>, pra ele saber o que está levando.</p></div>
<div class="part"><div class="n">3</div><p><b>O próximo passo</b>: um horário, uma data, uma escolha fácil.</p></div>
</div>{logo()}</div>""", css)))

S.append(("l8_c1_4", page(f"""<div class="s dark">{cnt(4)}
<div style="position:absolute;top:190px;left:96px;right:96px">
<div class="h" style="font-size:62px;margin-bottom:38px">Na prática:</div>
<div class="chat">
<div class="bi">Quanto fica a troca de óleo?</div>
<div class="bo">Me diz o modelo e o ano do carro que te passo certinho 🙂</div>
<div class="bi">Onix 2019</div>
<div class="bo">Pro seu Onix fica R$ 189, com óleo e filtro, em uns 30 min. Tenho sábado às 9h ou 10h30. Qual fica melhor?</div>
<div class="bi">9h! 🙌</div>
</div></div><div class="note">Exemplo ilustrativo, com valores fictícios.</div>{logo()}</div>""", css)))

S.append(("l8_c1_5", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:220px;left:96px;right:96px">
<div class="h" style="font-size:78px">Escreve uma vez.</div>
<div class="h" style="font-size:78px;margin-top:16px"><span class="pl">A equipe toda usa.</span></div>
<div class="b" style="font-size:36px;margin-top:40px;line-height:1.45">No Lomax, essa resposta vira uma <b>mensagem rápida</b>: digitou <b>/oleo</b>, ela aparece pronta. E se o cliente sumir depois do preço, o <b>retorno automático</b> chama ele de novo em horário comercial.</div>
<div style="margin-top:34px"><span class="chip">💬 Suporte em tudo pelo WhatsApp</span><span class="chip">🎥 Ajuda por vídeo com hora marcada</span></div>
<div class="cta" style="margin-top:24px">
<div style="font-size:44px;font-weight:800">Teste 30 dias grátis</div>
<div style="font-size:32px;margin-top:10px;opacity:.92">Sem cartão. Link na bio.</div>
</div></div>{logo(False)}</div>""", css)))

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out8")
    print(len(S))
