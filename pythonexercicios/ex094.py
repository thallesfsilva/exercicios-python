'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

pessoa = dict()
pop = list()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pop.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Foram cadastradas {len(pop)} pessoas. ')
média = soma/ len(pop)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in pop:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas que estão acima da média ', end='')
for p in pop:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')