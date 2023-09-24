def calcular_valor_maximo(operadores, operandos) -> float:
    disc = dict(zip(operadores, operandos))
    resultados = map(lambda item: item[1][0] + item[1][1] if item[0] == '+' else item[1][0] - item[1][1] if item[0] == '-' else item[1][0] * item[1][1] if item[0] == '*' else item[1][0] / item[1][1], disc.items())
    return max(resultados)

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

print(calcular_valor_maximo(operadores, operandos))
