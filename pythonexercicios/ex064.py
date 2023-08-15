'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
'''

s = n = c = 0
parar = False
while not parar:
    n = int(input('Digite um número: [999 para parar] '))
    if n != 999:
        c += 1
        s += n
    else:
        parar = True
print('Você digitou {} números e a soma entre eles foi de {}.'.format(c, s))