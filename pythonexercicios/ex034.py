sal1 = float(input('Digite o salário do funcionário: R$'))
if sal1 > 1250:
    sal2 = sal1 * 1.10
if sal1 <= 1250:
    sal2 = sal1 * 1.151
print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(sal1, sal2))