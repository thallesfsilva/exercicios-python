from datetime import date
ano = int(input('Digite o ano em que nasceu: '))
data_atual = date.today()
a = data_atual.year
b = a - ano
print('Você tem {} anos.'.format(b))
if b < 18:
    print('Você ainda vai se alistar!\nEm {} ano(s) você deverá se apresentar'.format(18 - b))
elif b == 18:
    print('Você deve se alistar nesse ano!!')
else:
    print('Você já passou do prazo de alistamento.\nEstá atrado {} ano(s)'.format(b - 18))
