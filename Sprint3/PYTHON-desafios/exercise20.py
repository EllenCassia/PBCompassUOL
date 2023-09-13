
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def reverse_list_in_place(lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]  # Troca os elementos
        inicio += 1
        fim -= 1

# Chama a função para inverter a lista 'a' no local
reverse_list_in_place(a)

print(a)
