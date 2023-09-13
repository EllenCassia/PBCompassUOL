from abc import ABCMeta, abstractmethod
class Passaro(metaclass=ABCMeta):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod 
    def voar(self):
        pass

    @abstractmethod
    def emitir_som(self):
        pass

class Pato(Passaro):
    def __init__(self, nome):
        super().__init__(nome)

    def voar(self):
        print(f"{self.nome} Voando...")

    def emitir_som(self):
        print(f"{self.nome} emitindo som...")
        print("Quack! Quack!")

class Pardal(Passaro):
    def __init__(self, nome):
        super().__init__(nome)

    def voar(self):
        print(f"{self.nome} Voando...")

    def emitir_som(self):
        print(f"{self.nome} emitindo som...")
        print("Piu! Piu!")

def main():
    pato = Pato("Pato")
    pardal = Pardal("Pardal")

    pato.voar()
    pato.emitir_som()

    pardal.voar()
    pardal.emitir_som()

main()            