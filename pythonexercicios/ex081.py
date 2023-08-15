'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

c = 0
listaNum = list()
while True:
    num = int(input('Digite um valor: '))
    listaNum.append(num)
    c += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
listaNum.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {c} elementos.') #posso usar o len(listaNum)
print(f'Os valores em ordem decrescente são {listaNum}.')
if 5 in listaNum:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')