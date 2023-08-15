peso = float(input('Informe seu peso: (Kg) '))
alt = float(input('Imporme sua altura: (m) '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('O seu IMC é {:.1f}.Você está abaixo do peso ideal!'.format(imc))
elif imc < 25:
    print('O seu IMC é {:.1f}. Seu peso está ideal.'.format(imc))
elif imc < 30:
    print('O seu IMC é {:.1f}. Você está sobrepeso.'.format(imc))
elif imc < 40:
    print('O seu IMC é {:.1f}. Você está com obesidade!'.format(imc))
else:
    print('O seu IMC é {:.1f}. Você está com obesidade móbida.'.format(imc))
