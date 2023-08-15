'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
 usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

masc = fem = maiorIdade = mulherMenorIdade = 0
while True:
    print('-' * 20)
    print('CADASTRO DE PESSOAS')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'F':
            fem +=1
            if idade < 20:
                mulherMenorIdade += 1
            if idade >= 18:
                maiorIdade += 1
        elif sexo == 'M':
            masc += 1
            if idade >= 18:
                maiorIdade +=1
    continuar = ' '
    while continuar not in 'SN':
        print('-' * 24)
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas maiores de 18 anos: {maiorIdade}')
print(f'Ao todo temos {masc} homens cadastrados.')
print(f'E temos {mulherMenorIdade} mulheres com menos de 20 anos.')

