n1 = int(input('Digite um valor inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(n1,bin(n1)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(n1, oct(n1)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção inválida. Tente novamente!!!')