#Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. 
#Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).


def preencher_lista_recursivamente(lista, n): 

    pares = 0
    impares = 0
    
    if n > 0:
        number = int(input("Digite um número: "))
        if number %2 == 0:
            pares += 1
        else:
            impares += 1
        lista.append(number)
        preencher_lista_recursivamente(lista, n - 1) # Aqui está adicionando o número na lista recursivamente, e decrementando o n.

lista = []
preencher_lista_recursivamente(lista, 3)
