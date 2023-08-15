'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.
'''

continuar = 'S'
maior = menor = c = soma = media = 0
while continuar in 'S':
    n = int(input('Digite um valor: '))
    c += 1
    soma += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
media = soma / c
print('''Você digitou {} valores e a média foi {}.
O maior valor foi {} e o menor foi {}.'''.format(c, media, maior, menor))
