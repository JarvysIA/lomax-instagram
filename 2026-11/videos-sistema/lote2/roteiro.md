# Vídeos do sistema — lote 2 — roteiro segundo a segundo

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

## 01_ia_madrugada.mp4 — IA de madrugada: às 03h10 o cliente manda 3 mensagens seguidas e o Agente responde tudo numa resposta só

**26.5 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,2 | começo — 3 s parados |
| 0:03,2–0:06,6 | 03h10: a oficina está fechada. Lista de conversas |
| 0:06,6–0:08,4 | um cliente novo escreve de madrugada |
| 0:08,4–0:12,2 | abre a conversa: a 1ª mensagem do cliente |
| 0:12,2–0:14,8 | chega a 2ª mensagem: ele pergunta se parcela |
| 0:14,8–0:18,9 | chega a 3ª mensagem: ele pede o valor da troca de óleo |
| 0:18,9–0:23,5 | o Agente de IA responde UMA vez, com tudo: o orçamento e o parcelamento |
| 0:23,5–0:26,5 | fim — 3 s parados |

- A resposta é a do Agente de IA DE VERDADE (“Duda”), com a tabela de preços da empresa fictícia — não é texto colado. Uma resposta só para as três mensagens: o orçamento da troca de óleo e, nele, o parcelamento que o cliente perguntou.
- Na vida real o Agente espera 20 segundos depois da última mensagem do cliente (é assim que ele junta mensagens seguidas) e só então responde. Na gravação essa espera foi pulada, e o resto da espera, com a tela parada, foi encurtado.
- O relógio: durante a gravação a empresa fictícia foi posta num fuso onde eram 03h10 de verdade naquele instante. Para o sistema ela estava fechada (expediente das 8h às 18h), e por isso o Agente — ligado no modo “à noite” — atendeu. A barra do celular e a hora das mensagens mostram esse relógio.
- O cliente é fictício e escreve pelo webhook de testes.
- Espera encurtada: "o Agente de IA responder" levou 26.9 s de verdade nos testes; no vídeo aparecem 4 s (a tela estava parada nesse intervalo).

## 02_ia_loja_fechada.mp4 — IA com a loja fechada, às 14h: a cliente pergunta preço e tamanho e o Agente responde com a tabela da loja

**20.2 s** · 1170×2532 · Flor de Maria · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,2 | começo — 3 s parados |
| 0:03,2–0:04,5 | 14h, loja fechada. Lista de conversas |
| 0:04,5–0:06,2 | uma cliente escreve perguntando o preço e o tamanho do vestido |
| 0:06,2–0:12,1 | abre a conversa: a pergunta da cliente |
| 0:12,1–0:17,2 | o Agente de IA responde sozinho, com a tabela da loja: o vestido, os tamanhos, o preço e o pagamento |
| 0:17,2–0:20,2 | fim — 3 s parados |

- A resposta é a do Agente de IA DE VERDADE da loja fictícia (“Flora”), com a tabela dela: o vestido, os tamanhos, o preço e a forma de pagamento saem do cadastro. Não é texto colado.
- O DIA: a gravação foi feita numa QUARTA-FEIRA (18/11/2026, a data que aparece na conversa), não num domingo. Para o sistema se comportar como no domingo, a loja fictícia ficou sem expediente nesse dia — que é exatamente o que um domingo é para o sistema. O Agente, ligado no modo “fora do horário”, atendeu por isso. Para ter um domingo de verdade na tela, é só regravar esta cena num domingo.
- O relógio das 14h: a empresa fictícia foi posta num fuso onde eram 14h de verdade naquele instante.
- Nos testes, a espera de 20 s que o Agente faz antes de responder foi pulada. A cliente é fictícia e escreve pelo webhook de testes.
- Espera encurtada: "o Agente de IA responder" levou 24.3 s de verdade nos testes; no vídeo aparecem 4 s (a tela estava parada nesse intervalo).

## 03_ia_clinica.mp4 — IA na clínica: a paciente pergunta o valor da consulta e o Agente responde

**20.5 s** · 1170×2532 · Clínica Vitalis · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,2 | começo — 3 s parados |
| 0:03,2–0:04,6 | lista de conversas da clínica, em horário de atendimento |
| 0:04,6–0:06,3 | uma paciente nova escreve perguntando o valor da consulta |
| 0:06,3–0:12,3 | abre a conversa: a pergunta da paciente |
| 0:12,3–0:17,5 | o Agente de IA responde sozinho: a consulta, o valor e a forma de pagamento, da tabela da clínica |
| 0:17,5–0:20,5 | fim — 3 s parados |

- A resposta é a do Agente de IA DE VERDADE (“Clara”), com a tabela de preços da clínica fictícia: a consulta, o valor e a forma de pagamento saem do cadastro da empresa. Não é texto colado.
- A clínica está ABERTA na cena: o Agente dela está no modo “sempre” (atende também no horário de atendimento).
- Nos testes, a espera de 20 s que o Agente faz antes de responder (para juntar mensagens seguidas) foi pulada.
- O relógio da tela: a empresa fictícia foi posta num fuso onde era horário comercial na hora da gravação.
- A paciente é fictícia e escreve pelo webhook de testes.
- Espera encurtada: "o Agente de IA responder" levou 27.5 s de verdade nos testes; no vídeo aparecem 4 s (a tela estava parada nesse intervalo).

## 05_anuncio_23h.mp4 — Anúncio às 23h: o lead chega pelo anúncio, o Agente responde e o card aparece no funil com “Veio do anúncio”

**27.7 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,1 | começo — 3 s parados |
| 0:03,1–0:04,3 | 23h: a oficina está fechada. Lista de conversas |
| 0:04,3–0:05,9 | um lead chega pelo anúncio da troca de óleo |
| 0:05,9–0:10,8 | abre a conversa: a mensagem que veio do anúncio |
| 0:10,8–0:14,0 | o Agente de IA responde na hora, com o orçamento |
| 0:14,0–0:15,6 | volta para a lista |
| 0:15,6–0:20,6 | abre o Funil: o card do lead está em Novo, já com responsável e a origem “Anúncio” |
| 0:20,6–0:24,7 | toca no card: na ficha, a seção “Veio do anúncio” |
| 0:24,7–0:27,7 | fim — 3 s parados |

- O lead é fictício: a mensagem entra pelo webhook de testes com os mesmos campos que o WhatsApp manda quando a pessoa clica num anúncio “Clique para WhatsApp” (título, texto e link do anúncio).
- A resposta é a do Agente de IA DE VERDADE (“Duda”), com a tabela de preços da empresa fictícia. Nos testes, a espera de 20 s que ele faz antes de responder foi pulada.
- O responsável do card é escolhido de verdade pela distribuição automática do funil (rodízio); numa regravação pode cair outro atendente.
- O relógio das 23h: a empresa fictícia foi posta num fuso onde eram 23h de verdade naquele instante; para o sistema ela estava fechada, e por isso o Agente (modo “à noite”) atendeu.
- Espera encurtada: "o lead do anúncio chegar" levou 1.7 s de verdade nos testes; no vídeo aparecem 1.2 s (a tela estava parada nesse intervalo).
- Espera encurtada: "o Agente de IA responder" levou 22.4 s de verdade nos testes; no vídeo aparecem 3 s (a tela estava parada nesse intervalo).

## 06_rodizio.mp4 — Rodízio: três leads chegam seguidos e cada um cai com um atendente diferente

**18.5 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,1 | começo — 3 s parados |
| 0:03,1–0:04,6 | funil de Atendimento, coluna Novo vazia |
| 0:04,6–0:07,9 | chega o 1º lead (Pedro Sales): o card aparece em Novo com Bruna Costa |
| 0:07,9–0:11,0 | chega o 2º lead (Amanda Reis): o card aparece em Novo com Juliana Alves |
| 0:11,0–0:12,5 | chega o 3º lead (Felipe Castro): o card aparece em Novo com Diego Martins |
| 0:12,5–0:15,5 | três leads, três atendentes diferentes: o rodízio dividiu sozinho |
| 0:15,5–0:18,5 | fim — 3 s parados |

- Quem escolhe o atendente é a distribuição automática do sistema, em rodízio entre os três atendentes marcados para receber no funil (Juliana Alves, Diego Martins e Bruna Costa). A ordem em que eles aparecem pode mudar numa regravação.
- Quem está olhando a tela é o dono (Carlos), que enxerga os cards de todos.
- Os três leads são fictícios e escrevem pelo webhook de testes. “Sem nome” no card é do sistema: o contato ainda não foi salvo com nome (aparece o nome do WhatsApp).
- O relógio da tela: a empresa fictícia foi posta num fuso onde era horário comercial na hora da gravação.
- Espera encurtada: "o 1º lead chegar" levou 4.6 s de verdade nos testes; no vídeo aparecem 1.5 s (a tela estava parada nesse intervalo).
- Espera encurtada: "ler no banco com quem cada lead ficou" levou 19.9 s de verdade nos testes; no vídeo aparecem 1.5 s (a tela estava parada nesse intervalo).

## 07_retorno_para_sozinho.mp4 — Retorno que para sozinho: o retorno automático sai, o cliente responde e a sequência de retornos para

**26.7 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,1 | começo — 3 s parados |
| 0:03,1–0:05,6 | funil, coluna “Sem resposta”: o Marcos pediu orçamento ontem e sumiu |
| 0:05,6–0:07,6 | o retorno automático sai sozinho: o card ganha o selo “Follow-up 1/5” |
| 0:07,6–0:13,5 | abre a conversa: o retorno enviado, com o selo “Automática” |
| 0:13,5–0:15,5 | o Marcos responde |
| 0:15,5–0:16,9 | volta para a lista de conversas |
| 0:16,9–0:18,9 | abre o Funil: “Sem resposta” ficou vazia (0) |
| 0:18,9–0:23,6 | o card voltou sozinho para “Em atendimento”, sem o selo do follow-up: os próximos retornos foram cancelados |
| 0:23,6–0:26,7 | fim — 3 s parados |

- O relógio foi adiantado no banco: a conversa foi montada com data de ontem e o 1º retorno, que venceria depois, passou a vencer na hora da gravação. Quem escreve e manda o retorno é a automação de verdade, com o texto cadastrado na empresa fictícia.
- Quando o cliente responde, é o sistema que para a sequência: os retornos seguintes são cancelados, o card sai de “Sem resposta” e volta para “Em atendimento”, sem o selo “Follow-up 1/5”.
- O cliente é fictício e responde pelo webhook de testes.
- O relógio da tela: a empresa fictícia foi posta num fuso onde era horário comercial na hora da gravação (o retorno automático só sai no expediente).
- Espera encurtada: "a rodada das automações mandar o retorno" levou 12.7 s de verdade nos testes; no vídeo aparecem 2.5 s (a tela estava parada nesse intervalo).

## 08_perfis_de_acesso.mp4 — Perfis de acesso: a mesma tela vista pela atendente (só o que é dela) e pelo dono (tudo)

**25.2 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,1 | começo — 3 s parados |
| 0:03,1–0:03,6 | celular da Juliana (atendente): o Funil, em “Em atendimento” |
| 0:03,6–0:05,8 | ela vê só o atendimento que é dela (1 card) |
| 0:05,8–0:10,4 | toca em “Conversas”: só as conversas dela |
| 0:10,4–0:13,0 | CORTE — celular do Carlos (dono): a mesma tela, com os atendimentos de todos os atendentes |
| 0:13,0–0:17,3 | toca em “Conversas”: as conversas de todos os atendentes |
| 0:17,3–0:19,0 | volta ao Funil |
| 0:19,0–0:22,2 | troca para o funil “Oficina”: ele vê os dois funis da empresa |
| 0:22,2–0:25,2 | fim — 3 s parados |

- São dois celulares, com um corte seco entre eles: primeiro o da Juliana (perfil Atendente), depois o do Carlos (o dono, perfil Administrador). As telas são as mesmas: o Funil, na etapa “Em atendimento”, e a lista de Conversas.
- Quem decide o que cada um enxerga é o sistema: a empresa fictícia tem o recurso “visibilidade restrita” ligado, e com ele quem não é administrador vê só os atendimentos dele. O Carlos vê os de todos os atendentes e os dois funis da empresa (“Atendimento” e “Oficina”).
- A lista “Funil” é uma caixa de escolha do celular: no vídeo o toque aparece e o valor muda, sem a roleta do aparelho.
- Os clientes e os atendimentos são fictícios, montados no banco de testes.

## 09_equipe_mesmo_numero.mp4 — Equipe toda no mesmo número: dois atendentes respondendo clientes diferentes ao mesmo tempo

**29.4 s** · 1920×1080 · Oficina do Carlos · computador, tela dividida

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,2 | começo — 3 s parados |
| 0:03,2–0:05,5 | tela dividida: à esquerda o computador da Juliana, à direita o do Diego — o mesmo WhatsApp da oficina |
| 0:05,5–0:08,5 | dois clientes escrevem quase juntos: a Fernanda cai na tela da Juliana e o Lucas na do Diego |
| 0:08,5–0:23,3 | os dois atendentes digitam ao mesmo tempo, cada um na sua conversa |
| 0:23,3–0:26,4 | as duas respostas saem pelo mesmo número, cada uma com o nome de quem atendeu |
| 0:26,4–0:29,4 | fim — 3 s parados |

- São duas janelas do sistema, lado a lado, como num monitor dividido ao meio: à esquerda a Juliana, à direita o Diego — dois logins diferentes, na mesma empresa e no MESMO número de WhatsApp. Cada janela tem a sua seta de mouse.
- Cada atendente vê só as conversas dele: a empresa fictícia tem o recurso “visibilidade restrita” ligado. As duas respostas saem pelo mesmo número, cada uma com o nome de quem atendeu.
- O menu lateral do sistema está recolhido nas duas janelas (é o botão do próprio sistema), para a conversa ter mais espaço.
- A digitação é feita com o teclado de verdade nas duas janelas, com as letras intercaladas entre uma e outra, para os dois escreverem ao mesmo tempo.
- As duas janelas foram reduzidas um pouco (94%) para caberem lado a lado em 1920×1080 com o layout de computador do sistema.
- Os clientes são fictícios e escrevem pelo webhook de testes; o que os atendentes enviam vai para um WhatsApp de mentira.

## 10_audio_longo.mp4 — Áudio longo: a cliente manda 1 minuto de áudio e aparece a transcrição inteira

**23.1 s** · 1170×2532 · Oficina do Carlos · celular

| tempo | o que acontece |
|---|---|
| 0:00,0–0:03,1 | começo — 3 s parados |
| 0:03,1–0:05,7 | lista de conversas da Juliana |
| 0:05,7–0:07,0 | a Cristina manda um áudio de 1 minuto |
| 0:07,0–0:10,9 | abre a conversa: o áudio da cliente, de 1:02 |
| 0:10,9–0:13,4 | embaixo do áudio aparece a transcrição automática, inteira |
| 0:13,4–0:20,1 | desliza a conversa: a transcrição continua até o fim do áudio |
| 0:20,1–0:23,1 | fim — 3 s parados |

- O áudio é fictício: um texto de 1 minuto e 2 segundos lido pela voz do computador (uma cliente contando um barulho no carro e pedindo horário). O vídeo é mudo: o áudio não toca.
- A transcrição é a de verdade do sistema (a mesma que os clientes com o Agente de IA recebem em todo áudio), feita na hora sobre esse áudio. O texto que aparece é o que o sistema entendeu, sem retoque.
- A oficina está aberta na cena: o Agente dela só atende fora do horário, então quem responde é a atendente.
- O relógio da tela: a empresa fictícia foi posta num fuso onde era horário comercial na hora da gravação.
- Espera encurtada: "o áudio chegar" levou 51.3 s de verdade nos testes; no vídeo aparecem 2.5 s (a tela estava parada nesse intervalo).

## 11_confirmacao_completa.mp4 — Confirmação de agendamento: sai sozinha no dia anterior, e a resposta ao “1” também

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

- Este vídeo é a mesma gravação da cena 7 do lote 1 (18/11/2026, 17h49): não foi gravado de novo.
- A consulta está marcada para o dia seguinte ao da gravação; a confirmação é mandada pela automação de verdade, na véspera. Só o minuto do envio foi adiantado no banco (o padrão é às 10h do dia útil anterior).
- O texto é o modelo de confirmação da empresa fictícia, com a data e a hora preenchidas pelo sistema.
- A resposta “1” da cliente entra pelo webhook de testes.
- O “Agendamento confirmado ✅” é a resposta automática do sistema ao “1” (texto padrão, que cada empresa pode trocar). De verdade ela sai de 20 a 40 segundos depois do “1”; no vídeo essa espera, com a tela parada, foi encurtada.
- Espera encurtada: "a rodada das automações mandar a confirmação" levou 16 s de verdade nos testes; no vídeo aparecem 2.5 s (a tela estava parada nesse intervalo).
- Espera encurtada: "a resposta da cliente chegar" levou 2 s de verdade nos testes; no vídeo aparecem 1.2 s (a tela estava parada nesse intervalo).
- Espera encurtada: "a resposta automática sair" levou 25.5 s de verdade nos testes; no vídeo aparecem 2.4 s (a tela estava parada nesse intervalo).

## Cenas puladas

- **04 — IA que não sabe: o cliente pergunta algo fora da tabela, o Agente diz que vai confirmar com a equipe e a conversa passa para um atendente** — PULADA. Não existe em produção do jeito descrito. Hoje, quando o Agente de IA não sabe responder (o assunto não está na tabela nem no que a empresa ensinou), ele NÃO manda mensagem nenhuma ao cliente: a conversa simplesmente fica para a equipe responder. À noite, quem cobre é a mensagem fixa de “fora do horário” da Recepção automática, se a empresa a tiver ligada. Não há um “vou confirmar com a equipe” saindo para o cliente, nem um aviso na tela de que a conversa passou para um atendente. Conferido em 18/11/2026 no código do Agente e numa sonda nos testes (uma paciente perguntou sobre implante à clínica fictícia, que não tem implante na tabela: o Agente não respondeu nada).
