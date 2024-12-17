"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

import os

os.system("cls || clear")
cid = (input("Em que cidade você nasceu?: ")).strip()
print(cid[:5].upper() == "Santo")