"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitiso separados.

unidade:4
dezena:3
centena:3
milhar:1

"""

import os

os.system("cls || clear")

num = int(input("Informe um número: "))
n = str(num)

print(f"Analisando o número {num}")

u = num / 1 % 10
d = num / 10 % 10
c = num / 100 % 10
m = num / 100 % 10

print(f"Analisando o número: {num}")
print(f"Unidade: {u:.1f}")
print(f"Dezena: {d:.1f}")
print(f"Centena {c:.1f}")
print(f"Milhar {m:.1f}")
