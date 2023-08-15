s1 = float(input('Primeigo segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos formam o seguinte triângulo: ', end = '')
    if s1 == s2 == s3:
        print('Triângulo equilátero!')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('Triângulo escaleno!')
    else:
        print('Triângo isósceles!')
else:
    print('Os segmentos não formam um triângulo!')
