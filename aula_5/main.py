#aula 4

idade1=float(input("digite sua idade :  "))
salario1=float(input("digite seu salario :  "))


if idade1 > 12:
    if idade1 < 18:
        print("pre adolescente")


if salario1 < 3000:
    if salario1 > 1540:
        print("pobre")

if salario1 < 1540:
    print("pobre pra k7")

if salario1 > 3000:
    if salario1 < 8000:
         print("rico")

if salario1 > 8000:
    print("rico pra k7")

if idade1 < 12:
    if idade1 > 0:
        print("criança")

if idade1 > 17:
    print("adulto")

if idade1 > 45:
    print("idoso")