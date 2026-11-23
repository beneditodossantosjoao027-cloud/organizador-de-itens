import os
import shutil
import time
import winreg
from pathlib import Path

INTERVALO = 10  # confere a cada 10 segundos

# extensão -> nome da pasta (tudo minúsculo)
CATEGORIAS = {
    "video": {".mp4", ".mkv", ".avi", ".mov", ".webm",},
    "img":{".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"},
    "pdf": {".pdf"},
    "som": {".mp3", ".wav", ".ogg", ".flac", ".m4a"},
    "instalador": {".exe", ".msi"},
}

# inverte o dicionário: ".pdf" -> "pdf", ".mp3" -> "som", ...
EXT_PARA_PASTA = {ext: pasta for pasta, exts in CATEGORIAS.items() for ext in exts}


def pasta_downloads():
    
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders",
        ) as chave:
            valor, _ = winreg.QueryValueEx(chave, "{374DE290-123F-4565-9164-39C4925E467B}")
            return Path(os.path.expandvars(valor))
    except Exception:
        return Path.home() / "Downloads"


DOWNLOADS = pasta_downloads()


def arquivo_pronto(caminho):
    
    try:
        antes = caminho.stat().st_size
        time.sleep(2)
        return antes == caminho.stat().st_size
    except OSError:
        return False


def destino_livre(pasta, nome):
    
    destino = pasta / nome
    contador = 1
    while destino.exists():
        p = Path(nome)
        destino = pasta / f"{p.stem}_{contador}{p.suffix}"
        contador += 1
    return destino


def organizar():
    for item in DOWNLOADS.iterdir():
        if not item.is_file():
            continue
        categoria = EXT_PARA_PASTA.get(item.suffix.lower())
        if not categoria:
            continue
        if not arquivo_pronto(item):
            continue
        pasta_destino = DOWNLOADS / categoria
        pasta_destino.mkdir(exist_ok=True)
        try:
            shutil.move(str(item), str(destino_livre(pasta_destino, item.name)))
        except (OSError, shutil.Error):
            pass  


while True:
    try:
        organizar()
    except Exception:
        pass
    time.sleep(INTERVALO)