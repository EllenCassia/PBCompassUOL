class Pessoa:
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