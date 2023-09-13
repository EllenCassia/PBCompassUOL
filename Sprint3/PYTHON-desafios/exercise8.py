# Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

def interatorList(lista, n):
    if n < 0:
        return
    palavra = ''
    for i in range(len(lista[n]) - 1, -1, -1):  # Começa no último caractere, condição de parada q loop vai até -1, e pra loop ser de trás para frente
        palavra += lista[n][i]
    if(palavra == lista[n]):
        print(f'{lista[n]} é um palíndromo')
    else:
        print(f'{lista[n]} não é um palíndromo')   
    interatorList(lista, n - 1) # 

a = ['moto','radar','radio','audio','arara','maça']
interatorList(a, len(a) - 1)

 