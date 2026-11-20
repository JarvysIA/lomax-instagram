"""Lote 14: Reels "uso real" a partir das gravações do Code (2026-11/videos-sistema).
Cada Reel: segmentos da gravação alinhados à narração (tempo da narração -> ponto da gravação; congela o último quadro se faltar),
títulos em PNG transparente por cima, card final de 3 s, trilha baixa por baixo, -14 LUFS."""
import sys, os, subprocess, json
sys.path.insert(0,'/home/claude/lomax-instagram/ferramentas/lote5')
from base import font_faces, ROOT
from playwright.sync_api import sync_playwright
V='/home/claude/lomax-instagram/2026-11/videos-sistema/'
A='/home/claude/l14/aud/'
OUT='/home/claude/lomax-instagram/2026-11/lote14/'
TMP='/home/claude/l14/tmp/'
LEAD=0.3; TAIL=0.6; END=3.0
CSS=font_faces()+"""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:transparent;font-family:Barlow}
.t{position:absolute;left:50px;right:50px;top:58px;text-align:center;color:#fff;font-weight:900;font-style:italic;font-size:86px;line-height:1.02;letter-spacing:-2px;text-shadow:0 4px 18px rgba(0,0,0,.35)}
.p{display:inline-block;background:#0E8DFE;border-radius:22px;padding:2px 26px 12px;transform:rotate(-1.5deg);margin-top:8px}
.tag{position:absolute;left:0;right:0;bottom:22px;text-align:center;color:#8fa6c4;font-size:28px;font-weight:600;letter-spacing:.5px}
.end{position:absolute;inset:0;background:#0A192C;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center;padding:0 60px}
.end .a{font-weight:900;font-style:italic;font-size:92px;line-height:1.04;letter-spacing:-2px}
.end .b{font-size:44px;margin-top:44px;color:#c9d6e8;line-height:1.35}
.end .c{margin-top:60px;background:#0E8DFE;border-radius:999px;padding:26px 64px;font-size:50px;font-weight:800}
.end img{height:70px;margin-top:90px}
"""
def h(body): return f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>"
def title(a,b): return h(f"<div class=t>{a}<br><span class=p>{b}</span></div>")
def tag(): return h("<div class=tag>Gravação real do Lomax · empresa de teste, dados fictícios</div>")
def end(a,b,c,d): return h(f"<div class=end><div class=a>{a}<br><span style='color:#0E8DFE'>{b}</span></div><div class=b>{c}</div><div class=c>{d}</div><img src='file://{ROOT}/logo_on_dark.png'></div>")
def render(items,out):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
        for n,html in items:
            fp=os.path.abspath(f'{out}/{n}.html'); open(fp,'w').write(html); pg.goto('file://'+fp); pg.wait_for_timeout(300); pg.evaluate("document.fonts.ready")
            pg.screenshot(path=f"{out}/{n}.png",omit_background=True)
        b.close()
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))

def mask(w,h,r,path):
    from PIL import Image, ImageDraw
    im=Image.new('L',(w,h),0); ImageDraw.Draw(im).rounded_rectangle([0,0,w-1,h-1],r,fill=255); im.save(path)

def build(c):
    n=c['name']; d=f"{TMP}{n}/"; os.makedirs(d,exist_ok=True)
    nar=A+c['audio']; nd=dur(nar); vend=LEAD+nd+TAIL; total=vend+END
    items=[(f"t{i}",title(a,b)) for i,(t0,t1,a,b) in enumerate(c['titles'])]+[("tag",tag()),("end",end(*c['end']))]
    render(items,d)
    src=V+c['src']; segs=c['segs']; layout=c.get('layout','phone')
    if layout=='phone':
        W,H,X,Y=800,1532,140,316; pre=f"crop=1170:2240:0:0,scale={W}:{H},setsar=1"; mask(W,H,44,d+'mask.png')
    else:  # computador em tela dividida: as duas colunas de conversa lado a lado
        W,H,X,Y=840,1560,120,304
        pre=f"split[l][r];[l]crop=544:500:416:0,scale=840:772,pad=840:788:0:0:color=0x0A192C[l2];[r]crop=544:500:1376:0,scale=840:772[r2];[l2][r2]vstack,setsar=1"; mask(W,H,28,d+'mask.png')
    fc=[f"[0:v]tpad=stop_mode=clone:stop_duration=15,fps=30,{pre},split={len(segs)}"+''.join(f"[s{i}]" for i in range(len(segs)))]
    for i,(tn,ts) in enumerate(segs):
        t_start=0 if i==0 else LEAD+tn; t_end=vend if i==len(segs)-1 else LEAD+segs[i+1][0]
        ln=t_end-t_start; s0=ts-(LEAD if i==0 else 0)
        fc.append(f"[s{i}]trim=start={max(0,s0):.3f}:duration={ln:.3f},setpts=PTS-STARTPTS[g{i}]")
    fc.append(''.join(f"[g{i}]" for i in range(len(segs)))+f"concat=n={len(segs)}:v=1:a=0,format=rgba[cat]")
    fc.append(f"[cat][1:v]alphamerge[rnd]")
    fc.append(f"color=c=0x0A192C:s=1080x1920:r=30:d={vend:.3f}[bg];[bg][rnd]overlay={X}:{Y}:shortest=1[b0]")
    k=0; inputs=['-i',src,'-loop','1','-i',d+'mask.png']; idx=2
    last='b0'
    inputs+=['-i',d+'tag.png']; fc.append(f"[{last}][{idx}:v]overlay=0:0[k{k}]"); last=f"k{k}"; k+=1; idx+=1
    for i,(t0,t1,a,b) in enumerate(c['titles']):
        e0=0 if t0==0 else LEAD+t0; e1=vend if t1 is None else LEAD+t1
        inputs+=['-i',f"{d}t{i}.png"]; fc.append(f"[{last}][{idx}:v]overlay=0:0:enable='between(t,{e0:.3f},{e1:.3f})'[k{k}]"); last=f"k{k}"; k+=1; idx+=1
    inputs+=['-loop','1','-t',f'{END}','-i',d+'end.png']; ei=idx; idx+=1
    fc.append(f"[{last}]format=yuv420p[main];[{ei}:v]fps=30,format=yuv420p,trim=0:{END},setpts=PTS-STARTPTS[endc];[main][endc]concat=n=2:v=1:a=0[vout]")
    inputs+=['-i',nar,'-i',A+'music.mp3']; ni=idx; mi=idx+1
    fc.append(f"[{ni}:a]adelay={int(LEAD*1000)}|{int(LEAD*1000)},apad,atrim=0:{total:.3f},aformat=channel_layouts=stereo[vo]")
    fc.append(f"[{mi}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,aformat=channel_layouts=stereo,volume='if(lt(t,{vend:.3f}),0.13,0.42)':eval=frame,afade=t=out:st={total-1.2:.3f}:d=1.2[mu]")
    fc.append(f"[vo][mu]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[aout]")
    os.makedirs(OUT,exist_ok=True)
    cmd=['ffmpeg','-v','error','-y',*inputs,'-filter_complex',';'.join(fc),'-map','[vout]','-map','[aout]','-c:v','libx264','-crf','20','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-ar','48000','-t',f'{total:.3f}','-movflags','+faststart',OUT+n+'.mp4']
    subprocess.run(cmd,check=True); return OUT+n+'.mp4', total

R=[
 dict(name='l14_r1_madrugada',src='lote2/01_ia_madrugada.mp4',audio='r1.mp3',
  segs=[(0,3.4),(5.0,11.6),(6.3,14.4)],
  titles=[(0,3.5,'03h10.','Oficina fechada.'),(3.5,9.4,'3 mensagens','seguidas.'),(9.4,None,'A IA respondeu','tudo de uma vez.')],
  end=('Junta tudo.','Responde uma vez.','Agente de IA do Lomax<br>30 dias grátis, com o agente incluso','Link na bio')),
 dict(name='l14_r2_audio',src='02_audio.mp4',audio='r2.mp3',
  segs=[(0,5.0),(2.8,12.4)],
  titles=[(0,2.9,'Mandou áudio','pedindo preço?'),(2.9,7.6,'O Lomax','transcreve.'),(7.6,None,'E a IA','responde.')],
  end=('Mandou áudio?','A IA entende.','Agente de IA do Lomax<br>30 dias grátis, com o agente incluso','Link na bio')),
 dict(name='l14_r3_anuncio_23h',src='lote2/05_anuncio_23h.mp4',audio='r3.mp3',
  segs=[(0,3.4),(3.5,10.3),(7.0,18.3),(9.0,21.8)],
  titles=[(0,3.5,'23h. Lead','do anúncio.'),(3.5,7.0,'A IA respondeu','na hora.'),(7.0,None,'E o card avisa:','veio do anúncio.')],
  end=('Anúncio às 23h?','Alguém responde.','Agente de IA + origem do anúncio no card<br>30 dias grátis, com o agente incluso','Link na bio')),
 dict(name='l14_r4_rodizio',src='lote2/06_rodizio.mp4',audio='r4.mp3',
  segs=[(0,1.5),(4.5,7.5),(6.2,10.6)],
  titles=[(0,3.0,'3 clientes','chegaram juntos.'),(3.0,8.2,'Cada um','com um atendente.'),(8.2,None,'Rodízio','automático.')],
  end=('Ninguém briga','por cliente.','Distribuição automática entre a equipe<br>Teste 30 dias grátis, sem cartão','Link na bio')),
 dict(name='l14_r5_retorno',src='lote2/07_retorno_para_sozinho.mp4',audio='r5.mp3',
  segs=[(0,1.0),(5.8,11.0),(9.5,18.4)],
  titles=[(0,3.0,'Pediu orçamento','e sumiu?'),(3.0,8.0,'O retorno','sai sozinho.'),(8.0,None,'Respondeu?','O retorno para.')],
  end=('Lembra o cliente.','Sem insistir à toa.','Até 5 retornos, só em horário comercial<br>Teste 30 dias grátis, sem cartão','Link na bio')),
 dict(name='l14_r6_mesmo_numero',src='lote2/09_equipe_mesmo_numero.mp4',audio='r6.mp3',layout='desk',
  segs=[(0,4.5),(3.0,12.0),(6.0,19.5)],
  titles=[(0,2.7,'2 clientes.','Ao mesmo tempo.'),(2.7,6.0,'2 atendentes.','1 número.'),(6.0,None,'Cada um','no seu login.')],
  end=('A equipe toda','no mesmo número.','Cada um no seu login, com o nome em cada resposta<br>Teste 30 dias grátis, sem cartão','Link na bio')),
 dict(name='l14_r7_conectar',src='08_conectar_pelo_codigo.mp4',audio='r7.mp3',
  segs=[(0,0.0),(5.5,6.4),(7.6,12.0),(11.0,20.0)],
  titles=[(0,2.3,'"Me cadastrei e não','consegui conectar."'),(2.3,7.6,'Conecta','pelo celular.'),(7.6,11.4,'Gera o código.','Digita no WhatsApp.'),(11.4,None,'Pronto.','Conectado.')],
  end=('Sem computador.','Sem QR Code.','Conecta pelo celular, com um código<br>Teste 30 dias grátis, sem cartão','Link na bio')),
 dict(name='l14_r8_perfis',src='lote2/08_perfis_de_acesso.mp4',audio='r8.mp3',
  segs=[(0,2.6),(3.2,8.4),(5.0,10.8),(7.0,15.6),(8.9,18.6)],
  titles=[(0,4.8,'A atendente vê','só o dela.'),(4.8,10.6,'O dono vê','tudo.'),(10.6,None,'Cada um vê','o que precisa.')],
  end=('Cada um','no seu quadrado.','Perfis de acesso: atendente, gerente e administrador<br>Teste 30 dias grátis, sem cartão','Link na bio')),
 dict(name='l14_r9_mensagem_rapida',src='04_mensagem_rapida.mp4',audio='r9.mp3',
  segs=[(0,1.0),(3.0,8.4),(6.6,12.4),(9.0,15.6)],
  titles=[(0,3.0,'Perguntou o preço','de novo?'),(3.0,9.0,'Digita /pre.','Pronto.'),(9.0,None,'Toca','e envia.')],
  end=('Digitou /,','apareceu.','Mensagens rápidas para a equipe toda<br>Teste 30 dias grátis, sem cartão','Link na bio')),
 dict(name='l14_r10_confirmacao',src='07_confirmacao_agendamento.mp4',audio='r10.mp3',
  segs=[(0,3.5),(3.4,8.6),(5.6,16.9)],
  titles=[(0,3.4,'Cliente marca','e esquece?'),(3.4,8.0,'A confirmação','sai sozinha.'),(8.0,None,'Respondeu 1?','Confirmado.')],
  end=('Menos faltas.','Sem ninguém lembrar.','Confirmação automática no dia anterior<br>Teste 30 dias grátis, sem cartão','Link na bio')),
]
if __name__=='__main__':
    only=sys.argv[1:]
    for c in R:
        if only and c['name'] not in only: continue
        f,t=build(c); print(f, round(t,2))
