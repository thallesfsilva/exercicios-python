'''
Melhore o jogo do exercício 028 onde o computador vai "pensar" em um
número inteiro entre 0 e 10. Só que agora o jogador vai tebtar adivinhar
até acertar, mostrando no final quantos palpites foram necessários.
'''

'''import random
from time import sleep
erro = 0
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = random.choice(numeros)
n = int(input('Escolha um número inteiro de 0 a 10: '))
print('PROCESSANDO...')
sleep(3)
if n != escolhido:
    erro += 1
while n != escolhido:
    erro += 1
    n = int(input('Tente mais uma vez: '))
    print('PROCESSANDO...')
    sleep(3)
print('Você acertou com {} tentativas.'.format(erro))'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente: ')
        elif jogador > computador:
            print('Menos.. Tente novamente: ')
print('Você acertou com {} tentativas. Parabéns!'.format(palpite))

