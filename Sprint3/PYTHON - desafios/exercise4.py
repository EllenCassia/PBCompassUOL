# Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
#Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

for i in range(2, 101):# Começar de 2, pois todo número abaixo de 2 não é primo. E termina em 101 porquê começa em 2
    is_prime = True # Está boolean serve para determinar se o número i é primo ou não.
    for j in range(2, i): # Ele verifica se o número i é divisível por qualquer número no intervalo
        if i % j == 0: # não é primo
            is_prime = False
            break
    if is_prime: # é primo
        print(i)
