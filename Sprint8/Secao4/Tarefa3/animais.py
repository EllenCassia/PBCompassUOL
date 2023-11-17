animais = ["gato", "cachorro", "pássaro", "peixe", "elefante", "girafa", "leão", "tigre", "zebra", "macaco",
           "rato", "coelho", "cobra", "lagarto", "tartaruga", "pato", "abelha", "formiga", "borboleta", "aranha"]

animais.sort()

for animal in animais:
    print(animal)

with open('animais.csv', 'w') as arquivo:
    for animal in animais:
        arquivo.write(animal + '\n')
