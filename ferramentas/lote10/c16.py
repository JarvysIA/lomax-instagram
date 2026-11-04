"""l10_s3 (checagem de 04/11; ideia do Columba 03/11: "Quem está falando?" com várias pessoas no mesmo número).
Recurso confirmado: cada mensagem sai com o nome de quem atendeu (story ls_21, carrossel l9_c1)."""
from base import *
from c9 import single

S = [single("l10_s3_quem_fala", "“Quem está", "falando aí?”", "Agora o cliente sabe.",
    "Com a equipe toda no mesmo número, o cliente se perde. No Lomax, cada mensagem sai com o nome de quem atendeu. O cliente sabe com quem fala, e você sabe quem respondeu.",
    dark=False, size=92)]

if __name__ == "__main__":
    render_pngs(S, "/home/claude/l5/out16")
    print(len(S))
