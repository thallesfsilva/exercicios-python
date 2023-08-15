'''from math import sqrt
caop = float(input('Comprimento do cateto oposto: '))
caad = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}!'.format(sqrt(caop * caop + caad * caad)))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}!'.format(hi))
