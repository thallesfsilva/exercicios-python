'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

listaNum = []
pares = []
impares = []
while True:
    listaNum.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
for i, v in enumerate(listaNum):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {listaNum}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')