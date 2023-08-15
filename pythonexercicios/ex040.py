n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Você está reprovado!')
elif 5.0 <= m <= 6.9:
    print('Você está de recuperação')
else:
    print('Parabéns. Você está aprovado!!!')