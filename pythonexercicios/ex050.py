soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite  o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
if soma == 0 and cont == 0:
    print('Você não informou nenhum número par.')
elif cont == 1:
    print('Você digitou apenas um número par. Seu valor é {}.'.format(soma))
elif cont > 1:
    print('Você informou {} valores pares. E a soma dos mesmos é igual à {}'.format(cont, soma))
