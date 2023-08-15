fra = str(input('Digite um a frase: ')).upper().strip()
print('A letra A aparece {} vezes.'.format(fra.count('A')))
print('A primeira letra A aparece na posição {}'.format(fra.find('A')+1))
print('A última letra A aparece na posição {}.'.format(fra.rfind('A')+1))