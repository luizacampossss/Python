import os
import emoji

os.system("cls || clear")

def menu():
    print("""
Deseja participar do sorteio?
1 - Sim
2 - Não                    
          """)
while True:
    menu()
    resposta = (input("Digite a sua resposta: ")).lower()
    match resposta:
        case "sim":
            import random
            num = random.randint(1,10)
            print(f"Este é o seu número da sorte: {num}")
        case "nao":
            print("Ok, vc não quer participar. See you later!")
            break
        case _:
            print("Informação inválida, tente novamente.")

