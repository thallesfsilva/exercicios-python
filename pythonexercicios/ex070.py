'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou
não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

print('-' * 20)
print('{:^20}'.format('MERCADO DO THALLES'))
print('-' * 20)
total = prodMais = menorPreco = cont = 0
barato = ''
while True:
    prod = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Quanto custa o produto: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        prodMais += 1
    if cont == 1 or preco < menorPreco:         #até a linda 26, funciona para encontrar o menor valor
        menorPreco = preco
        barato = prod
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar sua compra? [S/N]')).strip().upper()
        print('-' * 30)
    if continuar == 'N':
        break
print('FIM DA COMPRA')
print(f'O total da compra foi de R${total:.2f}')
print(f'{prodMais} custam mais que R$1000,00')
print(f'O produto mais barato foi {prod} e custa R${menorPreco:.2f}.')
