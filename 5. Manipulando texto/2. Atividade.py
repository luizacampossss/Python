"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

a) O nome com todas as letras maiúsculas
b) O nome com todas minúsculas
c) Quantas letras ao todo (sem considerar os espaços)
d) Quantas letras tem o primeiro nome
"""

import os

os.system("cls || clear")

nome = input("Digite seu nome completo: ").strip()

print("Analisando seu nome...")
print(f"Seu nome em maiúsculo é {nome.upper()}")
print(f"Seu nome em minusculo é {nome.lower()}")
print(f"Seu nome tem ao todo {len.nome - nome.count('')}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome tem {len(nome.split()[0])} letras")

