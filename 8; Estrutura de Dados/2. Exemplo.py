"""
Salvar em um arquivo chamado: carteira_de_clientes.txt
Fazer leitura de dados no arquivo carteira_de_clientes.txt e mostre no terminal
"""

import os
from dataclasses import dataclass
os.system("cls || clear")

# Estrutura de dados.
@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_CLIENTES = 2

lista_clientes = []

for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome = input("Digite seu nome: "),
        sobrenome = input("Digite o seu sobrenome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite o seu peso: ")),
        altura = float(input("Digite a sua altura: "))
    )
                    
    lista_clientes.append(cliente)

print("\n=== Exibindo dados dos alunos ===")
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")    
    print(f"Sobrenome: {cliente.sobrenome}")    
    print(f"Idade: {cliente.idade}")    
    print(f"Peso: {cliente.peso}")    
    print(f"Altura: {cliente.altura}")

# Definindo arquivo para salvar os dados.
nome_do_arquivo = "Lista_de_alunos_SENAI.txt"

with open(nome_do_arquivo, "w") as arquivo_clientes:
    for cliente in lista_clientes:
        arquivo_clientes.write(f"{cliente.nome},{cliente.sobrenome}, {cliente.idade}, {cliente.peso}, {cliente.altura}")

arquivo_clientes.close()

print("\n=== Dados dos alunos salvo com sucesso! ===")

lista_clientes = []

print("\n=== Acessando dados de um arquivo ===")

with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        nome, sobrenome, idade, peso, altura = dados
        dados = linha.strip().split(",")
        lista_clientes.append(Cliente(nome=nome,
                                      sobrenome=sobrenome,
                                      idade=int(idade),
                                      peso=float(peso),
                                      altura=float(altura)))
arquivo_clientes.close()

print("\n=== Exibindo dados dos alunos ===")
for aluno in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Sobrenome: {cliente.sobrenome}")
    print(f"Idade: {cliente.idade}")
    print(f"Peso: {cliente.peso}")
    print(f"Altura: {cliente.altura}")
