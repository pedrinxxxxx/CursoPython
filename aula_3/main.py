nome=input("digite seu nome: ")
idade=input("digite sua idade: ")
cor=input("digite sua cor favorita: ")
comida=input("digite sua comida favorita: ")
animal=input("digite seu animal favorito: ")
jogo=input("digite o seu jogo favorito: ")
print(f"hola {nome} voce tem {idade} anos e sua cor favorita é {cor} e sua comida favorita é {comida} e seu animal favorito é {animal} seu jogo favorito é {jogo}")




# numero 2

numero1=float(input("digite o primeiro numero: "))
numero2=float(input("digite o segundo numero: "))
operacao=input("escolha a operaçao (+,-,*,/):")

if operacao=="+":
    resutado=numero1+numero2

elif operacao=="-":
    resutado=numero1-numero2

elif operacao=="*":
    resutado=numero1*numero2

elif operacao=="/":
    resutado=numero1/numero2

else:
    resutado="operaçao invalida"

print(f"o resultado da operaçao é:{resutado}")


print("o resutado e", resutado )
