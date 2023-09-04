# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

try:
    # Abre o arquivo para leitura
    with open('C:\\Users\\ellen\\Downloads\\arquivo.txt','r') as arquivo:
        # Lê todo o conteúdo do arquivo
        conteudo = arquivo.read()
        # Imprime o conteúdo na tela
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except IOError:
    print("Ocorreu um erro de E/S ao ler o arquivo.")

    

