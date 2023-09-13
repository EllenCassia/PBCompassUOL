class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        self.listaOrdenada = sorted(self.listaBaguncada)
        return self.listaOrdenada

    def ordenacaoDecrescente(self):
        self.listaOrdenada = sorted(self.listaBaguncada, reverse=True)
        return self.listaOrdenada

crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])
crescente_ordenada = crescente.ordenacaoCrescente()
decrescente_ordenada = decrescente.ordenacaoDecrescente()

print(crescente_ordenada)
print(decrescente_ordenada)
