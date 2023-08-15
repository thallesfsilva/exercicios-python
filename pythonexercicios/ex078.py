'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.
'''

maior = menor = 0
num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('-=' * 30)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}... ', end='')
print()
