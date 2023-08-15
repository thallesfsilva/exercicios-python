'''

Faça um programa que leia um número qualquer e mostre seu fatorial.

FORMULA QUE EU APRENDI

print('Digite um número para')
n = int(input('Calcular seu fatorial: '))
f = 1
n1 = 2
while n1 <= n:
    f = f * n1
    n1 = n1 + 1
print('O fatorial de {}! é {}'.format(n, f))


FÓMULA SIMPLES

from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O Fatorial de {}! é {}'.format(n, f))'''

#FORMULA DO CURSO
n = int(input('Digite um valor para calcular o seu fatorial: '))
c = n
f = 1
print('Calculado {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))