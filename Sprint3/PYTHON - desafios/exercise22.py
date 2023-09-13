class Pessoa:
<<<<<<< HEAD
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
=======
    def __init__(self):
        pass
    def name(self, name):
        self._name = name
    def returnName(self):
        return self._name
    def id(self, id):
        self._id = id
    def returnId(self):
        return self._id

def main():
    pessoa = Pessoa(0)
    pessoa.name("João")
    pessoa.id(123)
    print(pessoa.returnName())
    print(pessoa.returnId())
main()    
>>>>>>> main
