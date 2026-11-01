"""l10_s1 (checagem de 01/11; ideia de WhaScale 31/10: antes de escolher a ferramenta, pergunte se é fácil de usar e se o suporte ajuda).
Recursos confirmados: suporte em tudo pelo WhatsApp e ajuda por vídeo com hora marcada."""
from base import *
from c9 import single

S = [single("l10_s1_ajuda", "Antes de escolher", "um sistema, pergunte:", "Quem me ajuda?",
    "Lista de recurso bonita não adianta se ninguém te ajuda a configurar. No Lomax, a gente monta junto com você por vídeo, com hora marcada, e tira dúvida no dia a dia pelo WhatsApp.",
    dark=False, size=84)]

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out13")
    print(len(S))
