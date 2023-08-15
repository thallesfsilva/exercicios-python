'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valor = par = terCol = segMai = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite o valor para [{l}, {c}]: '))
        matriz[l][c] = valor
        if valor % 2 == 0:
            par += valor
        if c == 2:
            terCol += valor
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares é: {par}.')
print(f'A soma dos valores da terceira coluna é: {terCol}.')
for c in range(0, 3):
    if c == 0:
        segMai = matriz[1][c]
    elif matriz[1][c] > segMai:
        segMai = matriz[1][c]
print(f'O maior valor da segunda linha é: {segMai}.')
