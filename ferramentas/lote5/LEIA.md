# Motor das artes do lote 5

- `base.py`: identidade (Barlow, cores, logo) e render dos carrosséis 1080x1350 com Playwright.
- `reel_lib.py`: Reels 1080x1920 a 30 fps. Cada Reel é um HTML com `render(t)`; legendas palavra a palavra com `buildCaps`.
- `mix.py`: voz + trilha com ducking + efeitos, normalizado.
- `c1..c3.py` e `r1..r3.py`: os posts do lote 5.

Preparar: `pip install playwright && python3 -m playwright install chromium && npm i @fontsource/barlow`.
Áudios da ElevenLabs ficam fora do repositório (flow "Lomax lote 5 (Reels)").
