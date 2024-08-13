def personagems():
    herois_info = [
        {"nome": "Aragorn", "elemento": "terra", "poder": 80},
        {"nome": "Gandalf", "elemento": "fogo", "poder": 95},
        {"nome": "Legolas", "elemento": "ar", "poder": 75},
    ]
    dragoes_info = [
        {"nome": "Smaug", "elemento": "fogo", "poder": 90},
        {"nome": "Iceheart", "elemento": "gelo", "poder": 85},
        {"nome": "Stormwing", "elemento": "ar", "poder": 78},
    ]

    time = input("digite numero 1 para herois e 2 para dragoes : ")
    if time == "1":
        print("seu time e heroi")
        print("digite suas caracteristicas : ")
        nome = input("qual seu nome :")
        elemento = input("elemento : ")
        poder = input("poder : ")

    else:
        print("seu time e dragoes")
        print("digite suas caracteristicas : ")
        nome = input("qual seu nome :")
        elemento = input("elemento : ")
        poder = input("poder : ")
    x = ("seus dados sao ,nome:" + nome + "elemento : ", elemento, "poder : " + poder)
    print(x)

    if time == "1":
        herois_info[4]['nome'] = nome
        herois_info[4]['elemento'] = elemento
        herois_info[4]['poder'] = poder

    else:
        if time == "2":
            dragoes_info[4]['nome'] = nome
            dragoes_info[4]['elemento'] = elemento
            dragoes_info[4]['poder'] = poder
