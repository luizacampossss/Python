"""
Faça um programa em python que abra e reproduza o aúdio de um arquivo mp3.
"""

import os
import pygame

os.system("cls || clear")

try:
    # Carregando o arquivo MP3
    pygame.mixer.music.load("tribodaperiferia.mp3")
    pygame.mixer.music.play()

    print("Tocando música...")

    # Mantendo o programa em execução enquanto a música toca
    while pygame.mixer.music.get_busy():
        pass

except pygame.error as e:
    print(f"Erro ao carregar ou tocar o áudio: {e}")