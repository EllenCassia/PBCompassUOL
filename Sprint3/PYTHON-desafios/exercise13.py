# Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. 
# Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listPow = []

def my_map(lista, f):
    resultado = []

    for numero in lista:
        numberPow = numero ** f  # Calcula a potência corretamente
        resultado.append(numberPow)

    return resultado

listPow = my_map(a, 2)
print(listPow)
