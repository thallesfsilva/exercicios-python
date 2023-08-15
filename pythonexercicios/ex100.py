'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
'''

from random import randint

numeros = list()

def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print('-=' * 20)
    print(f'Os números sorteados foram: {numeros}.')


def somaPar():
    par = 0
    for c in range(len(numeros)):
        if numeros[c] % 2 == 0:
            par += numeros[c]
    print('-=' * 20)
    print(f'A soma dos números pares é igual a: {par}')


sorteia()
somaPar()
