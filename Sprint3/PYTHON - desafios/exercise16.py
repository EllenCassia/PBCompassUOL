# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

#A string deve ter valor  "1,3,4,6,10,76"

def soma_string(string):
    lista = string.split(',') # Serve para separar a string em uma lista, usando o separador ','   
    soma = 0
    for i in lista:
        soma += int(i)
    return soma

print(soma_string("1,3,4,6,10,76"))