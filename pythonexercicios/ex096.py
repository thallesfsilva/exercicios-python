def area():
    a = l * c
    print(f'A área do terreno {l:.1f} x {c:.1f} é de {a:.1f}m².')

print('  CONTROLE DE TERRENOS  ')
print('-' * 24)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area()