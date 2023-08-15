'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

pop = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pop) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            mai = dados[1]
    pop.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(pop)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in pop:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in pop:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()
