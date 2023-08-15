'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while
'''

print('=-' * 10)
print('GERADO DE PA')
primeiro = int(input('Informe o primeiro termo: '))
razão = int(input('Informe a razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print('{} - '.format(termo), end='')
    termo += razão
    c += 1
print('FIM')

