"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente e de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
import math
import os

os.system("cls || clear")

co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = math.hypot(co,ca)
print(f"A hipotenusa vai medir: {hi:.2f}")

# Sem biblioteca/módulo 
# co = float(input("Digite o comprimento do cateto oposto: "))
# ca = float(input("Digite o comprimento do cateto adjacente: "))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print(f"A hipotenusa vai medir {hi}")