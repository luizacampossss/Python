import emoji
import os

os.system("cls || clear")

# Usando códigos de emojis
texto = emoji.emojize("Olá, mundo! :earth_americas:")
print(texto)  # Saída: Olá, mundo! 🌎

# Convertendo um emoji para descrição
descricao = emoji.demojize("Olá, 🌟!")
print(descricao)  # Saída: Olá, :star: