def cadastrarPromocao(nomePromocao, descicaoPromocao):
    mycursor = conbd.cursor()
    sql = "INSERT INTO promocao (Nome, Descricao ) VAlUES (%s, %s)"
    values = (nomePromocao, descricaoPromocao)
    mycursor.execute(sql, values)
    Promocao = mycursor.lastrowid
    
    conbd.commit()
    print("promocao cadastrada com sucesso")
    mycursor.close()