def cadastrarProdutos (conbd, nome, descricao, preco, Quantidade):
    mycursor = conbd.cursor()
    sql = "INSERT INTO produtos (Nome, Descricao, Preco) VAlUES (%s, %s, %s)"
    valores = (nome, descricao, preco)
    mycursor.execute(sql, valores)
    ID_Produto = mycursor.lastrowid
    sql1 = "INSERT INTO estoque (ID_Produto, Quantidade) VAlUES (%s, %s)"
    valores1 = (ID_Produto, Quantidade)
    mycursor.execute(sql1, valores1)
    conbd.commit()
    print("produto cadastrado com sucesso")
    mycursor.close()
    
    
