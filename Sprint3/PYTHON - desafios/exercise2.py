#Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. 
#Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).

for i in range(3):
    number = int(input("Digite um número: "))
    if number % 2 == 0:
        print("Par:", number)
    else:
        print("Ímpar:", number)





