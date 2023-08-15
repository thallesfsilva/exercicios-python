'''
Faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F'. Caso errado, peça a digitação
novamente até ter um valor válido
'''

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dado inválido. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))