class Calculo:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

def main():
    x = 4
    y = 5

    calculadora = Calculo()
    
    resultado_soma = calculadora.soma(x, y)
    resultado_subtracao = calculadora.subtracao(x, y)

    print(f"Somando: {x} + {y} = {resultado_soma}")
    print(f"Subtraindo: {x} - {y} = {resultado_subtracao}")

if __name__ == "__main__":
    main()
