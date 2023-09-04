# Faça um programa que gere uma nova lista contendo apenas números ímpares.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
listPar = []

def interatorList(list, n): # passa a lista que sera percorrida, e n para mostrar o tamanho da lista
    if n < 0: # condição de parada da recursividade
        return
    if list[n] % 2 != 0: # lógica pra ver se o numero é ímpar
        listPar.append(list[n]) 
    interatorList(list,n-1) # itera recursivamente a lista, e decrementa o n

interatorList(a,len(a) - 1)   # Subtrai 1 para começar da última posição da lista
print(sorted(listPar))