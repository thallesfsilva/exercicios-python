'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

'''listaNum = []
valores = []
for c in range(1, 8):
    valores.append(int(input(f'Digite o {c}o. valor: ')))
    listaNum.append(valores[:])
    valores.clear()
print('-=' * 30)
print('O valores pares digitados foram: ', end='')
for p in listaNum:
    if p[0] % 2 == 0:
        print(f'{p[0]} ', end='')
print()
print(f'Os valores ímpares digitados foram: ', end='')
for p in listaNum:
    if p[0] % 2 != 0:
        print(f'{p[0]} ', end='')
print()'''

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')