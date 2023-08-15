'''num = int(input('Digite um número: '))
n = str(num)
print('Unidades: {}'.format(n[3]))
print('Dezenas: {}'. format(n[2]))
print('Centenas: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidades: {}'.format(u))
print('Dezenas: {}'. format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))

