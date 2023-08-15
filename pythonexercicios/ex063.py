'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
'''

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
t = int(input('Quantos termos você deseja mostrar? '))
print('~' * 30)
a = 0
b = 1
while t > 0:
    print('{} - '.format(a), end='')
    c = a + b
    a = b
    b = c
    t -= 1
print('FIM')
print('~' * 30)