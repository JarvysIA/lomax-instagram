"""Post único l8_s1 (27/10): 'Você não esqueceu o cliente.' Ideia recriada da checagem diária."""
from base import *
from c7 import css
S = [("l8_s1_nao_esqueceu", page(f"""<div class="s light">{STRIPES}
<div style="position:absolute;top:250px;left:96px;right:96px">
<div class="h" style="font-size:100px">Você não esqueceu</div>
<div class="h" style="font-size:100px;margin-top:14px">o cliente.</div>
<div class="h" style="font-size:76px;margin-top:40px">Eram 47 conversas</div>
<div class="h" style="font-size:76px;margin-top:16px"><span class="pl">abertas.</span></div>
<div class="b" style="font-size:40px;margin-top:56px;line-height:1.42">Ninguém lembra de todo mundo de cabeça. No Lomax, quem pediu orçamento e sumiu recebe <b>retorno automático</b> em horário comercial, até 5 vezes, e ele para sozinho quando o cliente responde.</div>
</div><div class="note">Número ilustrativo.</div>{logo(False)}</div>""", css))]
if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out8"); print("ok")
