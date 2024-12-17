

"""
Conversão de Temperaturas
"""

import os

os.system("cls || clear")

c = float(input("Digite a temperatura em celsius: "))
f = ((9*c)/5)+32
k =((f-32/1.8)+273.15)

print(f"A temperatura de {c:.2f} convertida em fahrenheit ficou {f:.2f} e de fahrenheit em kelvin {k:.2f}")

