from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
valor = False
while not valor:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do Programa')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e de {} é {}'.format(n1, n2, soma))
        sleep(2)
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação de {} e de {} é {}.'.format(n1, n2, mult))
        sleep(2)
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
            sleep(2)
        elif n1 < n2:
            print('{} é menor que {}.'. format(n1, n2))
            sleep(2)
        else:
            print('Os dois valores são iguais')
            sleep(2)
    elif opcao == 4:
            print('Informe os números novamente.')
            n1 = int(input('Primeiro valor:'))
            n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        valor = True
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
print('Fim')
