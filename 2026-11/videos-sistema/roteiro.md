# Vídeos do sistema — roteiro segundo a segundo

Gravações do **Lomax CRM funcionando de verdade**, no ambiente de TESTES, com empresas fictícias (Oficina do Carlos,
Clínica Vitalis e a loja Flor de Maria). Nenhum dado real e nenhuma mensagem para número de verdade: os "clientes"
escrevem pelo webhook de testes e o que o sistema envia vai para um WhatsApp de mentira.

- Celular: 390×844 gravado em 3x (**1170×2532**), MP4 H.264, 30 fps. Computador: **1920×1080**.
- Todo vídeo tem **3 s parados no começo e 3 s parados no fim** (para entrada e saída de legenda).
- O círculo branco é o toque do dedo; no computador, a seta do mouse.
- A coluna "tempo" é o instante **do vídeo** (minuto:segundo,décimo) em que a coisa acontece — é por ela que se
  sincroniza legenda e narração. Num toque, é o instante em que o círculo aparece; numa coisa que o sistema faz
  sozinho (chegou mensagem, o Agente respondeu), é quando ela aparece na tela.
- Sem áudio: os vídeos são mudos.
- Onde diz "espera encurtada": o sistema de testes demorou mais do que o vídeo mostra, com a tela parada, e o excesso
  foi cortado. Nada do que aparece foi acelerado.

## 01_ia_noite.mp4 — Agente de IA à noite: às 22h10 o cliente pede orçamento e o Agente responde sozinho

**22.5 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,2 | começo — 3 s parados |
| 0:03,2–0:03,7 | 22h10: a oficina está fechada. Lista de conversas |
| 0:03,7–0:06,9 | um cliente novo escreve pedindo orçamento da troca de óleo |
| 0:06,9–0:13,9 | abre a conversa: a pergunta do cliente, às 22h10 |
| 0:13,9–0:19,1 | o Agente de IA responde sozinho, com o orçamento no modelo da empresa |
| 0:19,1–0:22,5 | fim — 3 s parados |

- A resposta é a do Agente de IA DE VERDADE, rodando nos testes com a tabela de preços da empresa fictícia — não é texto colado. Ele se apresenta (“Sou a Duda, assistente virtual da Oficina do Carlos”) e manda o orçamento no modelo cadastrado pela empresa, com a forma de pagamento. A mensagem sai com o selo “Automática · Duda - Assistente Virtual”.
- O relógio: durante a gravação a empresa fictícia foi posta num fuso onde eram 22h10 de verdade naquele instante. Para o sistema ela estava fechada (expediente das 8h às 18h), e por isso o Agente — ligado no modo “à noite” — atendeu. A barra do celular e a hora das mensagens mostram esse relógio.
- Nos testes, a espera que o Agente faz antes de responder (20 s, para juntar mensagens seguidas do cliente) foi pulada.
- O cliente é fictício e escreve pelo webhook de testes.
- Espera encurtada: "o Agente de IA responder" levou 29.5 s de verdade nos testes; no vídeo aparecem 5 s (a tela estava parada nesse intervalo).

## 02_audio.mp4 — Áudio: a cliente manda um áudio pedindo preço, aparece a transcrição e o Agente responde

**25.5 s** · 1170×2532 · Clínica Vitalis · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,2 | começo — 3 s parados |
| 0:03,2–0:06,2 | lista de conversas da clínica |
| 0:06,2–0:07,8 | a Larissa manda um áudio |
| 0:07,8–0:13,1 | abre a conversa: o áudio da cliente |
| 0:13,1–0:17,2 | embaixo do áudio aparece a transcrição automática |
| 0:17,2–0:22,5 | o Agente de IA responde sozinho, com o preço e a forma de pagamento |
| 0:22,5–0:25,5 | fim — 3 s parados |

- O áudio é fictício: uma frase lida pela voz do computador (“Oi, boa tarde! Eu queria saber quanto custa uma limpeza nos dentes, e como eu faço para pagar.”), 9 segundos. O vídeo é mudo: o áudio não toca.
- A transcrição é a de verdade do sistema (a mesma que os clientes com o Agente de IA recebem), feita na hora sobre esse áudio.
- A resposta é a do Agente de IA de verdade da clínica fictícia (“Clara”), com o preço da tabela dela. Nos testes, a espera de 20 s que o Agente faz antes de responder foi pulada.
- Espera encurtada: "o áudio chegar" levou 45.8 s de verdade nos testes; no vídeo aparecem 3 s (a tela estava parada nesse intervalo).
- Espera encurtada: "a transcrição do áudio" levou 10.6 s de verdade nos testes; no vídeo aparecem 3.5 s (a tela estava parada nesse intervalo).
- Espera encurtada: "o Agente de IA responder" levou 9.3 s de verdade nos testes; no vídeo aparecem 4 s (a tela estava parada nesse intervalo).

## 03_lead_chegando.mp4 — Lead chegando: cai no funil com responsável e “Veio do anúncio”

**18.5 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,3 | começo — 3 s parados |
| 0:03,3–0:05,0 | funil de Atendimento, coluna Novo vazia |
| 0:05,0–0:07,5 | o cliente escreve pelo anúncio: o card aparece em Novo, já com responsável |
| 0:07,5–0:11,1 | toca no card: abre a ficha do lead |
| 0:11,1–0:15,4 | na ficha: o responsável e a seção “Veio do anúncio” |
| 0:15,4–0:18,5 | fim — 3 s parados |

- O lead é fictício: a mensagem entra pelo webhook de testes com os mesmos campos que o WhatsApp manda quando a pessoa clica num anúncio “Clique para WhatsApp” (título, texto e link do anúncio).
- O responsável (Juliana Alves) é escolhido de verdade pela distribuição automática do funil, em rodízio entre quem está marcado para receber. Numa regravação pode cair o outro atendente (Diego Martins).
- “Sem nome” no card é do sistema: o contato ainda não foi salvo com nome (aparece o nome do WhatsApp).

## 04_mensagem_rapida.mp4 — Mensagem rápida: “/” e a resposta pronta de preço

**22.9 s** · 1170×2532 · Flor de Maria · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,5 | começo — 3 s parados (na tela: lista de conversas: a Aline perguntou o valor (2 não lidas)) |
| 0:03,5–0:07,5 | abre a conversa da Aline |
| 0:07,5–0:09,0 | toca na caixa de mensagem |
| 0:09,0–0:10,7 | digita “/”: abre a lista de respostas prontas |
| 0:10,7–0:12,9 | digita “pre”: sobra a resposta de preço |
| 0:12,9–0:16,3 | toca em /preco: o texto pronto entra na caixa |
| 0:16,3–0:19,9 | toca em Enviar: a resposta vai para a cliente |
| 0:19,9–0:22,9 | fim — 3 s parados |

- Tudo aqui é o sistema de verdade: a lista de respostas prontas abre ao digitar “/”, filtra enquanto se digita e o toque põe o texto na caixa.
- A mensagem é enviada de verdade pelo sistema — para o WhatsApp de mentira dos testes. A bolha fica azul-escura por um instante (enviando) e depois mostra o nome de quem atendeu (Camila Rocha).

## 05_retorno_automatico.mp4 — Retorno automático: o cliente que sumiu recebe o retorno com o texto da empresa

**23.4 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,4 | começo — 3 s parados (na tela: funil de Atendimento) |
| 0:03,4–0:06,7 | toca em “Sem resposta”: o Marcos pediu orçamento ontem e sumiu (card parado há 22 h) |
| 0:06,7–0:17,1 | abre a conversa: a última mensagem é da oficina, de ontem |
| 0:17,1–0:20,3 | o retorno automático chega sozinho, com o texto da empresa e o selo “Automática” |
| 0:20,3–0:23,4 | fim — 3 s parados |

- O relógio foi adiantado no banco: a conversa foi montada com data de ontem e o retorno, que venceria depois, passou a vencer na hora da gravação. Quem escreve e manda o retorno é a automação de verdade.
- O texto do retorno é o modelo cadastrado na empresa fictícia (“Olá, {nome}, tudo bem? Conseguiu ver o orçamento…”), com o nome do cliente preenchido pelo sistema.
- Na vida real o primeiro retorno sai no dia seguinte, em horário comercial (a cena tem de ser gravada em dia útil, das 8h às 18h).
- Espera encurtada: "a rodada das automações mandar o retorno" levou 26.2 s de verdade nos testes; no vídeo aparecem 7 s (a tela estava parada nesse intervalo).

## 06_equipe_transferencia.mp4 — Equipe: transferência para outra equipe, com o histórico e o nome de quem atendeu

**25.2 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,3 | começo — 3 s parados (na tela: celular da Juliana (Atendimento): a conversa da Vanessa, com o nome de quem atendeu em cada mensagem) |
| 0:03,3–0:05,2 | toca em “Ver card” |
| 0:05,2–0:06,8 | toca em “Transferir…”: abre a janela da transferência |
| 0:06,8–0:08,3 | escolhe o funil “Oficina” |
| 0:08,3–0:10,8 | escolhe para quem vai: Rafael Souza |
| 0:10,8–0:13,6 | escreve o recado para quem recebe |
| 0:13,6–0:16,2 | toca em “Transferir”: atendimento transferido |
| 0:16,2–0:17,3 | CORTE — celular do Rafael (Oficina): a conversa da Vanessa chegou para ele, no funil da Oficina |
| 0:17,3–0:22,2 | abre a conversa: o aviso “Juliana Alves passou este atendimento para você”, o recado e o histórico inteiro |
| 0:22,2–0:25,2 | fim — 3 s parados |

- São dois celulares, com um corte seco entre eles: primeiro o da Juliana (equipe de Atendimento), que transfere; depois o do Rafael (equipe da Oficina), que recebe.
- As listas “Funil” e “Para quem” são caixas de escolha do celular: no vídeo o toque aparece e o valor muda, sem a roleta do aparelho.
- O aviso “A IA está pausada nesta conversa porque a equipe respondeu” aparece porque a Oficina do Carlos tem o Agente de IA ligado; é do sistema.
- As mensagens antigas da conversa (de ontem e de hoje) foram montadas no banco, com o nome de quem atendeu cada uma (Diego Martins e Juliana Alves).
- Espera encurtada: "a conversa abrir" levou 2.2 s de verdade nos testes; no vídeo aparecem 1.2 s (a tela estava parada nesse intervalo).

## 07_confirmacao_agendamento.mp4 — Confirmação de agendamento: sai sozinha no dia anterior, e a resposta ao “1” também

**25.5 s** · 1170×2532 · Clínica Vitalis · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,3 | começo — 3 s parados |
| 0:03,3–0:03,7 | agenda de hoje |
| 0:03,7–0:09,3 | toca em “próximo dia”: amanhã tem a limpeza da Beatriz, às 14h |
| 0:09,3–0:10,8 | a confirmação saiu sozinha: o selo vira “Aguardando resposta” |
| 0:10,8–0:12,4 | toca no horário da Beatriz: abre as opções do agendamento |
| 0:12,4–0:17,9 | abre a conversa: a mensagem de confirmação, com o selo “Automática” |
| 0:17,9–0:20,3 | a Beatriz responde “1” |
| 0:20,3–0:22,5 | o sistema responde sozinho “Agendamento confirmado ✅”, com o selo “Automática” |
| 0:22,5–0:25,5 | fim — 3 s parados |

- A consulta está marcada para o dia seguinte ao da gravação; a confirmação é mandada pela automação de verdade, na véspera. Só o minuto do envio foi adiantado no banco (o padrão é às 10h do dia útil anterior).
- O texto é o modelo de confirmação da empresa fictícia, com a data e a hora preenchidas pelo sistema.
- A resposta “1” da cliente entra pelo webhook de testes.
- O “Agendamento confirmado ✅” é a resposta automática do sistema ao “1” (texto padrão, que cada empresa pode trocar). De verdade ela sai de 20 a 40 segundos depois do “1”; no vídeo essa espera, com a tela parada, foi encurtada.
- Espera encurtada: "a rodada das automações mandar a confirmação" levou 16 s de verdade nos testes; no vídeo aparecem 2.5 s (a tela estava parada nesse intervalo).
- Espera encurtada: "a resposta da cliente chegar" levou 2 s de verdade nos testes; no vídeo aparecem 1.2 s (a tela estava parada nesse intervalo).
- Espera encurtada: "a resposta automática sair" levou 25.5 s de verdade nos testes; no vídeo aparecem 2.4 s (a tela estava parada nesse intervalo).

## 08_conectar_pelo_codigo.mp4 — Conectar o WhatsApp pelo celular, com o código (sem QR)

**29.1 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,3 | começo — 3 s parados (na tela: Configurações → WhatsApp: nenhum WhatsApp conectado ainda) |
| 0:03,3–0:06,2 | toca em “Conectar pelo código”: a tela pede o número do WhatsApp |
| 0:06,2–0:08,5 | digita o número com DDD |
| 0:08,5–0:12,6 | toca em “Gerar código”: aparece o código LMX7-K2P9, com a contagem |
| 0:12,6–0:15,1 | mais abaixo: os 3 passos para digitar o código no WhatsApp do celular (passo 1) |
| 0:15,1–0:20,4 | passos 2 e 3: “Conectar um aparelho” e “Conectar com número de telefone” |
| 0:20,4–0:22,6 | o código foi digitado no celular: a tela avisa sozinha “WhatsApp conectado!” |
| 0:22,6–0:26,1 | toca em Fechar: “Conectado!” |
| 0:26,1–0:29,1 | fim — 3 s parados |

- SIMULADO, como nos prints de 15/11: nenhum pareamento de verdade é pedido. O código LMX7-K2P9 é inventado e o número (21) 98765-4321 também; o “conectou” foi marcado no banco de testes.
- As telas, os textos, a contagem do código e a janela “WhatsApp conectado!” são os do sistema de verdade.
- A parte de digitar o código no WhatsApp do celular não aparece (acontece em outro aplicativo): o vídeo mostra os 3 passos desenhados e depois a tela avisando sozinha que conectou.
- Espera encurtada: "o código aparecer" levou 21.4 s de verdade nos testes; no vídeo aparecem 2 s (a tela estava parada nesse intervalo).
- Espera encurtada: "o WhatsApp conectar" levou 24.7 s de verdade nos testes; no vídeo aparecem 2.5 s (a tela estava parada nesse intervalo).

## 09_ia_noite_computador.mp4 — Visão do computador: o Agente de IA à noite, com o funil ao lado da conversa

**22.9 s** · 1920×1080 · Oficina do Carlos · computador

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,1 | começo — 3 s parados |
| 0:03,1–0:04,8 | computador, à noite: o funil de Atendimento da oficina (fechada) |
| 0:04,8–0:09,0 | uma cliente nova escreve: o card aparece na coluna Novo, já com responsável |
| 0:09,0–0:14,4 | clica no ícone de conversa do card: a conversa abre em janela própria, ao lado do funil |
| 0:14,4–0:19,9 | o Agente de IA responde sozinho, com o orçamento no modelo da empresa |
| 0:19,9–0:22,9 | fim — 3 s parados |

- É a mesma situação da cena 1, com outra cliente fictícia, alguns minutos depois (o relógio aparece na hora das mensagens, dentro da janela da conversa).
- No computador, clicar no ícone de conversa do card abre a conversa numa JANELA PRÓPRIA do navegador. Como um vídeo grava uma tela só, essa janela foi desenhada por cima do funil, à direita, no tamanho em que o navegador a abre — a moldura cinza com “Lomax CRM — conversa” é da gravação; o que está dentro é o sistema.
- A resposta é a do Agente de IA de verdade; a espera de 20 s antes de responder foi pulada, como na cena 1.
- O responsável do card é escolhido pela distribuição automática (rodízio).
- Espera encurtada: "o Agente de IA responder" levou 16.3 s de verdade nos testes; no vídeo aparecem 4 s (a tela estava parada nesse intervalo).

