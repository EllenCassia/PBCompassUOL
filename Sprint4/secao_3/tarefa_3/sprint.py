import hashlib

while True:
    texto = input("Digite uma string (ou 's' para sair): ")
    
    if texto.lower() == 's':
        break
    
    sha1 = hashlib.sha1()
    
    sha1.update(texto.encode('utf-8'))
    
    hash_resultado = sha1.hexdigest()
    print("Hash SHA-1:", hash_resultado)
