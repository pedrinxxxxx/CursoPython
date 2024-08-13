
herois = [
 {"nome": "mina", "elemento": "psycco", "poder": 200,"armas": "espada" },
 {"nome": "matsu", "elemento": "fogo", "poder": 220,"armas": "martelo"},
 {"nome": "Legolas", "elemento": "luz", "poder": 300,"armas": "arco"},
 {"nome": "geolos", "elemento": "vento", "poder": 120,"armas": "cajado"},
 {"nome": "glovh", "elemento": "planta", "poder": 180,"armas": "cajado"},
 {"nome": "marks", "elemento": "dark", "poder": 230,"armas": "espada"},
]

dragoes = [
 {"nome": "haksip", "elemento": "eletricidade", "poder": 90,"arma compativel": "espada"},
 {"nome": "stropj", "elemento": "eletricidade", "poder": 130,"arma compativel": "martelo"},
 {"nome": "ryzor", "elemento": "luz,eletricidade", "poder": 280,"arma compativel": "espada"},
 {"nome": "razor", "elemento": "dark", "poder": 270,"arma compativel": "cajado"},
 {"nome": "sweety", "elemento": "psycco", "poder": 200,"arma compativel": ""},
 {"nome": "axarara", "elemento": "vento", "poder": 100,"arma compativel": "martelo"},
]



aliancas_magicas = []
for heroi in herois:
    for dragao in dragoes:
        if heroi["armas"] == dragao["arma compativel"]:
            aliancas_magicas.append((heroi["nome"], dragao["nome"]))

print("Alianças Mágicas Formadas:")
for alianca in aliancas_magicas:
    print(f"{alianca[0]} e {alianca[1]}")









































