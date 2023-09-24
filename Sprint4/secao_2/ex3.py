from functools import reduce

def calcula_saldo(lancamentos) -> float: 
    calcular_valor = lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0]

    saldo_total = reduce(lambda cont, valor: cont + valor, map(calcular_valor, lancamentos), 0)

    return saldo_total

lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

saldo = calcula_saldo(lancamentos)
print(saldo)
