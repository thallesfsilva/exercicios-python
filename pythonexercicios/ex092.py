'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - ano
trabalhador['ctps'] = int(input('CTPS (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['anoCont'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['anoCont'] + 35) - datetime.now().year)
print('-=' * 30 )
for k, v in trabalhador.items():
    print(f'  - {k} tem o valor {v}')