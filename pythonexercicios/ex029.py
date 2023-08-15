v = float(input('Em que velocidade o carro passou pelo radar de 80Km/h? '))
if v < 80:
    print('O motorista não excedeu o limite de velocidade!!!')
else:
    vm = v - 80
    print('O motorista excedeu a velocidade máxima do radar!! \nSua multa será de: R${:.2f}'.format(vm * 7.00))
