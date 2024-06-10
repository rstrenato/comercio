from bd import *
from conexaobd import conexao

conbd = conexao()

a = input("digite o nome do produto: ")
b = input("digite a descricao do produto: ")
c = float(input("digite o preco do produto: "))
d = int(input("digite a quantidade do produto: "))
cadastrarProdutos(conbd, a, b, c, d)
