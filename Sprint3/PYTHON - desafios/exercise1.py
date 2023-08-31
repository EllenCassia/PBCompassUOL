#Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

nome = input("Nome: ")
idade = int(input("Idade: "))


# Obtém o ano atual
from datetime import datetime
anoAtual = datetime.now().year

idadeCem = 100 - idade
anoCompletaCem = anoAtual + idadeCem
print(anoCompletaCem)

