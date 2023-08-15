termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao #fómula para calcular o enésimo
for c in range(termo, decimo + razao, razao):
    print(c, end= ' - ')
print('ACABOU')