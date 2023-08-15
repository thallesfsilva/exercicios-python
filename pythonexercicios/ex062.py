'''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.O programa encerrará quando
ele disser que quer mostrar 0 termos.
'''


p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
c = 1
while c <= 10:
    print('{} - '.format(t), end='')
    t += r
    c += 1
print('FIM')
ts = 10
maisTermos = False
while not maisTermos:
    opção = int(input('''Deseja mais termos?
Caso não queira, digite 0: '''))
    if opção > 0:
        while opção > 0:
            t += r
            print('{} - '.format(t), end='')
            opção -= 1
            ts += 1
        print('FIM')
    elif opção == 0:
        print('Até a próxima')
        maisTermos = True
    else:
        print('Dado inválido. Tente novamente')
print('Progressão finalizada com {} termos mostrados!'.format(ts))