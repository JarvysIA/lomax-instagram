import json, sys
B = "https://raw.githubusercontent.com/JarvysIA/lomax-instagram/main/2026-10/lote7/"
CH = "6ac9900a6a5c39ccb66abc0a"
ALT = {
 "l7_c1": ["As 5 mensagens que todo carioca manda no seu WhatsApp.",
           "Qual é o valor? No Lomax: mensagem rápida /preco, a equipe toda responde igual.",
           "Tá aberto sábado? às 23h40. No Lomax: a conversa entra em Novo no funil e a equipe vê quem está esperando.",
           "Vou ver e te falo. No Lomax: retorno automático em horário comercial.",
           "Fala com o Paulo, ele já sabe. No Lomax: histórico na conversa e nome de quem respondeu.",
           "Vi o anúncio de vocês. No Lomax: origem do anúncio no card e distribuição automática.",
           "Feito por carioca, pra carioca. Suporte pelo WhatsApp e por vídeo. Teste 30 dias grátis."],
 "l7_c2": ["Seu WhatsApp passa nesse teste? 8 perguntas.",
           "Perguntas 1 a 4 sobre clientes esperando, quem respondeu, continuidade e número único.",
           "Perguntas 5 a 8 sobre retorno, anúncio, resposta de preço e domingo sem celular.",
           "Resultado: 0 a 3 plantão total, 4 a 6 no meio do caminho, 7 a 8 atendimento redondo.",
           "Cada não tem resposta no Lomax. Teste 30 dias grátis."],
 "l7_c3": ["Você paga o anúncio. E o cliente fica no vácuo?",
           "Linha do tempo: clique às 10:02, oi às 10:03, ninguém responde até 12:40, cliente já resolveu.",
           "O problema não é o anúncio. É o que acontece depois do oi.",
           "No Lomax o oi tem dono: distribuição automática, origem no card, funil por etapas e retorno automático.",
           "Anúncio bom merece resposta. Teste 30 dias grátis."],
 "l7_c4": ["Medo de CRM complicado? A gente começa junto.",
           "Passo 1: cria a conta, 30 dias grátis sem cartão.",
           "Passo 2: chamada de vídeo com hora marcada para configurar equipes, funil e mensagens rápidas.",
           "Passo 3: suporte em tudo pelo WhatsApp.",
           "Passo 4: R$ 99,90 por mês com 2 usuários, extra R$ 49,90, Pix ou boleto."],
 "l7_s1_nao_espera": ["No Rio, cliente não espera. Ele fecha com quem responde primeiro."],
 "l7_s2_preco": ["Lomax CRM: R$ 99,90 por mês, 2 usuários inclusos, extra R$ 49,90, Pix ou boleto, 30 dias grátis."],
}
TXT = {
 "l7_c1": "Se você atende cliente no Rio pelo WhatsApp, já recebeu as cinco. Hoje mesmo, provavelmente. 😅\n\n“Qual é o valor?”, “Tá aberto sábado?” às 23h, “Vou ver e te falo”, “Fala com o Paulo” e “Vi o anúncio de vocês”.\n\nArrasta pro lado pra ver como cada uma é respondida no Lomax, sem depender de um celular só.\n\nQual dessas chega mais aí? Conta nos comentários. 👇\n\n#riodejaneiro #pequenasempresas #lomaxcrm",
 "l7_s1_nao_espera": "No Rio, cliente não espera. Ele manda “oi” pra três lugares e fecha com quem responde primeiro.\n\nCom a equipe toda atendendo no mesmo número, pelo computador, a resposta não fica presa num celular.\n\n#atendimentoaocliente #riodejaneiro #lomaxcrm",
 "l7_c2": "Teste rápido: 8 perguntas sobre o atendimento da sua empresa no WhatsApp. Conta quantos “sim” você marcou e deixa o número nos comentários. 👇\n\nSalva o post pra refazer o teste daqui a um mês.\n\n#pequenasempresas #atendimentoaocliente #lomaxcrm",
 "l7_c3": "Você paga o anúncio, o cliente manda “oi, quanto fica?” e... ninguém responde. Cada um achou que o outro tinha visto.\n\nO problema quase nunca é a campanha. É o que acontece depois do “oi”.\n\nNo Lomax, cada conversa nova já cai com um atendente, o card mostra que o cliente veio do anúncio e quem sumiu recebe retorno automático em horário comercial.\n\n#trafegopago #pequenasempresas #lomaxcrm",
 "l7_c4": "Medo de CRM complicado? Aqui ninguém começa sozinho.\n\n1. Cria a conta e testa por 30 dias.\n2. Marca uma chamada de vídeo e a gente configura junto: equipes, etapas do funil e mensagens rápidas.\n3. Dúvida no dia a dia? Chama no WhatsApp.\n\nDepois, R$ 99,90 por mês com 2 usuários.\n\n#pequenasempresas #riodejaneiro #lomaxcrm",
 "l7_s2_preco": "Quanto custa o Lomax? R$ 99,90 por mês, com 2 usuários. Usuário extra por R$ 49,90. Pix ou boleto.\n\nE antes de pagar qualquer coisa, são 30 dias pra testar com a sua equipe.\n\nFicou alguma dúvida? Pergunta aqui nos comentários que a gente responde.\n\n#pequenasempresas #lomaxcrm",
 "l7_r1": "Segunda-feira, 8h, Rio de Janeiro. O WhatsApp da oficina já lotado e um celular só pra dar conta. 📲\n\nFoi assim, no balcão de um auto center em Jacarepaguá, que o Lomax nasceu. Hoje a equipe toda atende no mesmo número, cada conversa nova já cai com um atendente e o funil mostra quem está esperando.\n\nFeito por carioca, pra carioca. O teste de 30 dias está no link do perfil.\n\n#riodejaneiro #jacarepagua #lomaxcrm",
 "l7_r2": "“Oi, quanto fica?” às 10:03. Ninguém respondeu até 12:40. O cliente já fechou com outro.\n\nAnúncio bom merece resposta. No Lomax, a conversa nova cai direto com um atendente e o card avisa que veio da campanha.\n\nFeito no Rio, com suporte pelo WhatsApp e ajuda por vídeo com hora marcada.\n\n#trafegopago #riodejaneiro #lomaxcrm",
}
DUE = {"l7_c1": "2026-10-25T10:30:00Z", "l7_s1_nao_espera": "2026-10-25T15:00:00Z", "l7_r1": "2026-10-25T22:00:00Z",
       "l7_c2": "2026-10-26T10:30:00Z", "l7_c3": "2026-10-26T15:00:00Z", "l7_r2": "2026-10-26T22:00:00Z",
       "l7_c4": "2026-10-27T10:30:00Z", "l7_s2_preco": "2026-10-27T15:00:00Z"}

def inp(k):
    if k.startswith("l7_r"):
        assets = {"videos": [{"url": f"https://raw.githubusercontent.com/JarvysIA/lomax-instagram/main/2026-10/lote7/{k}.mp4", "metadata": {"thumbnailOffset": 26000 if k == "l7_r1" else 29000}}]}
        md = {"instagram": {"type": "reel", "shouldShareToFeed": True}}
    else:
        alts = ALT[k]
        names = [k] if len(alts) == 1 else [f"{k}_{i+1}" for i in range(len(alts))]
        assets = {"images": [{"url": B + n + ".jpg", "metadata": {"altText": a}} for n, a in zip(names, alts)]}
        md = {"instagram": {"type": "post", "shouldShareToFeed": True}}
    return {"channelId": CH, "text": TXT[k], "schedulingType": "automatic", "mode": "customScheduled",
            "dueAt": DUE[k], "saveToDraft": True, "assets": assets, "metadata": md}

keys = sys.argv[1:]
q = "mutation M(" + ",".join(f"$v{i}: CreatePostInput!" for i in range(len(keys))) + ") {" + " ".join(
    f"p{i}: createPost(input: $v{i}) {{ ... on PostActionSuccess {{ post {{ id status dueAt }} }} ... on MutationError {{ message }} }}" for i in range(len(keys))) + "}"
print(json.dumps({"query": q, "variables": {f"v{i}": inp(k) for i, k in enumerate(keys)}}, ensure_ascii=False))
