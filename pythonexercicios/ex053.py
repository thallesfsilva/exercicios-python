print('-=' * 20)
print('Detector de palíndromos')
print('-=' * 20)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()#separa os espaços no meio da frase
junto = ''.join(palavras)#juntar as palavras sem espaço
inverso = ''
'''inverso = junto[::-1]'''#linha de comando para não precisar usar o "for"
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndro!')
else:
    print('A frase digitada não é um palíndromo!')