'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')

n1 = int(input('Digite um número entre 0 e 20: '))

while n1 < 0 or n1 > 20:
    n1 = int(input('Tente novamente. Digite um número entre 0 e 5: '))

print(f'Você digitou o número {(n[n1])}.')
