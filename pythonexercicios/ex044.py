print('{:=^40}'.format(' LOJAS THALLES '))
valor = float(input('Digite o valor total das compras: R$ '))
print('''ESCOLHA A FORMA DE PAGAMENTO:
[ 1 ] Dinheiro/ Pix
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Selecione a opção: '))
if opção == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(valor, valor * 0.9))
elif opção == 2:
    print('Sua compra no valor de R${:.2f} passa a custar R${:.2f}'.format(valor, valor * 0.95))
elif opção == 3:
    print('Você deverá pagar 2 parcelas de {:.2f}'.format(valor / 2))
elif opção == 4:
    parc = int(input('Você pagará em quantas parcelas? '))
    vp = (valor * 1.2) / parc
    print('Você deve pagar {} parcelas de R${:.2f}'.format(parc, vp))
    print('Sua compra de R${:.2f} passa a valer R${:.2f}'.format(valor, valor * 1.2))
else:
    valor = 0
    print('\033[331mOPÇÃO INVÁLIDA DE PAGAMENTO! TENTE NOVAMENTE')