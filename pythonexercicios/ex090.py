'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
weconteúdo da estrutura na tela.
'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] >= 7 :
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

'''print(f'O nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual {aluno["situacao"]}')'''

for k, v in aluno.items()
    print(f' - {k} é igual a {v}')