'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

listaNum = list()
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > listaNum[-1]:
        listaNum.append(valor)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(listaNum):
            if valor <= listaNum[pos]:
                listaNum.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {listaNum}')
