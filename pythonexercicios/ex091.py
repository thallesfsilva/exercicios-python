'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogada = dict()
for c in range(1, 5):
    jogada[f'jogador{c}'] = randint(1, 6)
for k, v in jogada.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = list()
print('-='*30)
print(' == RANKING DOS JOGADORES == ')
sleep(1)
'''for i in sorted(jogada, key = jogada.get, reverse=True):
    print(f'{i:>3}{jogada[i]:>12}')
    sleep(1)'''
ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'  {i+1}o. lugar: {v[0]} com {v[1]}.')
    sleep(1)