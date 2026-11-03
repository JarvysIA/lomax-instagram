"""l10_s2 (checagem de 03/11; ideia do Columba/@ativocode 02/11: passar a senha do WhatsApp pra equipe toda tira o controle do número).
Recursos confirmados: usuários próprios, perfis admin/gerente/atendente (quem vê o quê), troca de usuário na mesma vaga."""
from base import *
from c9 import single

S = [single("l10_s2_login", "Ainda passa a senha", "do WhatsApp pra equipe?", "Cada um com o seu login.",
    "No Lomax, cada pessoa entra com o próprio usuário e você define quem vê o quê: admin, gerente e atendente. Se alguém sai, você troca o usuário e o número continua com a empresa.",
    dark=True, size=74)]

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out14")
    print(len(S))
