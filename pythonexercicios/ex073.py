'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Flamengo.
'''

times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Atlético-PR',
         'Atlético-MG', 'Santos', 'Fortaleza', 'Flamengo', 'São Paulo',
         'Grêmio', 'Internacional', 'Bragantino', 'Bahia', 'Goiás',
         'Vasco da Gama', 'Corinthians', 'Cuiabá', 'Coritiba', 'América-MG')

print('-' * 50)
print(f'Os 5 primeiros times são: {times[:5]}')

print('-' * 50)
print(f'Os 4 últimos colocados são: {times[-4:]}')

print('-' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')

print('-' * 50)
print(f'O Flamengo está na {times.index("Flamengo") + 1}ª posição.')