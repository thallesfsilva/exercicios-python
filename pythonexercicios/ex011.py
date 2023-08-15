x = float(input('Quantos metros de altura tem a sua parede? '))
y = float(input('Quantos metros de largura tem a sua parede? '))
a = x * y
print('Sua parete tem a dimensão de {}x{} e sua área é de {}m2'.format(x, y, a))
t = a / 2
print('Serão necessários {} litros de tinta!'.format(t))
