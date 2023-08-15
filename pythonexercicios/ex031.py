d = float(input('Digite quantos Km terá sua viagem: '))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print('O valor da sua passagem será de R${:.2f}'.format(p))