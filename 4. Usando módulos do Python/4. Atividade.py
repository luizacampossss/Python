
"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""
import math
import os
os.system("cls || clear")

num = float(input("Digite um valor: "))
num2 = math.trunc(num)
print(f"O valor digitado foi {num} e a sua porção inteira é {num2}")