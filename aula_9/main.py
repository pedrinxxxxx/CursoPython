lista=("pizza","hamburgue")
compra=input("escolha um item da lista: ")
existe=False
for item in lista:
    if  item ==compra:
        print("temos o produto")
        existe=True
        break
if existe ==False:
    print("o produto",compra,"esta fora de estoque")