"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo
o nome do escolhido
"""

import os
import random
os.system("cls || clear")

n1 = input("\nPrimeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")

lista = {n1,n2,n3,n4}
lista_sorteio = list(lista)
escolhido = random.choice(lista_sorteio)

print(f"\nO aluno escolhido foi: {escolhido}")
