import os
import sys

if getattr(sys, 'frozen', False):
    # Se o script está sendo executado como um executável
    BASE_DIR = sys._MEIPASS  # O diretório temporário do PyInstaller
else:
    # Se o script está sendo executado no modo normal
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

FONTS_DIR = os.path.join(BASE_DIR, "infra", "assets", "fonts")
IMAGE_DIR = os.path.join(BASE_DIR, "infra", "assets", "images")
SOUND_DIR = os.path.join(BASE_DIR, "infra", "assets", "sounds")
FILE_DIR = os.path.join(BASE_DIR, "infra", "assets", "files")
