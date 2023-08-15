import random
from time import sleep
numeros = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(numeros)
n = int(input('Escolha um número inteiro de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if n == escolhido:
    print('VOCÊ VENCEU!!!')
else:
    print('VOCÊ PERDEU!!!')
