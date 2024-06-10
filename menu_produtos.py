from bd import *
from conexaobd import conexao

conbd = conexao()


while True:
    print("selecione a opção desejada: ")
    print("1. cadastrar produto")
    print("2. alterar produto")
    print("3. excluir produto")
    print("4. sair")
    opcao=input("escolha uma opção: ")
    if opcao=="1":
        a = input("digite o nome do produto: ")
        b = input("digite a descricao do produto: ")
        c = float(input("digite o preco do produto: "))
        cadastrarProdutos(conbd, a, b, c,)

    break