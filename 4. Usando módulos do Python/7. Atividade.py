"""
O mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalhos dos alunos. Faça um programa que leia
o nome dos quatro alunos e mostre a ordem sorteada.
"""

import os
import random

os.system("cls || clear")

n1 = input("Digite primeiro aluno: ")
n2 = input("Digite segundo aluno: ")
n3 = input("Digite terceiro aluno: ")
n4 = input("Digite quarto aluno: ")

lista = [n1,n2,n3,n4]
lista_sorteio = random.shuffle(lista)
print("A ordem da apresentação será:")
print(lista)