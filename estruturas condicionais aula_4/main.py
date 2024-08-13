# numero 3
numero1=float(input("digite o primeiro numero:nota1"))
numero2=float(input("digite o segundo  numero:nota2"))
numero3=float(input("digite o terceiro numero:nota3"))



operacao=input("escolha a operacao(+,/): ")

if operacao == '+':
    resultado= numero3 + numero2 + numero1

print(f"esse e o total {resultado}")

operacao=input("escolha a operacao(+,/): ")
if operacao == '/':
    media =resultado / 3


print(f"a media e {media}")

if media > 6:
    print("aprovado")
else:
    print("reprovado")
