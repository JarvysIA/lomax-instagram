"""Checagem de 18/11 (ideia do Columba/@ativocode 17/11: "Ainda tem interesse?" sem contexto não traz o cliente de volta).
Só recurso confirmado: retorno automático com o seu texto, em horário comercial, que para quando o cliente responde."""
import sys, os
F = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for d in ("lote5", "lote7", "lote8", "lote9", "lote10", "lote11"):
    sys.path.insert(0, os.path.join(F, d))
from base import render_pngs
from c9 import single
S = [single("l13_s3_interesse", "\"Ainda tem", "interesse?\"", "Não traz ninguém.",
    "Lembra o que o cliente pediu: <b>\"Oi, Carla! O orçamento do câmbio do HR-V continua de pé até sexta.\"</b> No Lomax, o retorno automático sai com o seu texto, em horário comercial, e para sozinho quando o cliente responde.",
    dark=True, size=100, note="Exemplo ilustrativo.")]
if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out13c"); print(len(S))
