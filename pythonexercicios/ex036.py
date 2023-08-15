casa = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
pres = casa / (anos * 12)
if pres / salario <= 0.3:
    print('Crédito aprovado! Você pagará {} prestações no valor de R${:.2f}'.format(anos * 12, pres))
else:
    print('Crédito não aprovado!')