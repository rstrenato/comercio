from datetime import datetime
from bd import *
from conexaobd import conexao



a = input("digite o nome da promocao: ")
b = input("digite a descricao da promocao: ")
c = input("digite a data inicio (formato: dd-mm-yyyy): ")
c = datetime.strptime(c, "%d-%m-%Y").strftime("%Y-%m-%d")
d = input("digite a data fim (formato: dd-mm-yyyy): ")
d = datetime.strptime(d, "%d-%m-%Y").strftime("%Y-%m-%d")



print("promocao cadastrada com sucesso")
