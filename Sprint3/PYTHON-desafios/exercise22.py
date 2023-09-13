class Pessoa:
    def __init__(self, id):
        self.__nome = None  # Atributo privado
        self.id = id  # Atributo público

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

def main():
    pessoa = Pessoa(0)  # Passando um valor para o atributo público id
    pessoa.nome = "Fulano De Tal"
    print(pessoa.nome)

if __name__ == "__main__":
    main()
