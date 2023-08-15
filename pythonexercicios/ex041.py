from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today()
ano = ano_atual.year
idade = ano - nasc
if idade <= 9:
    print('O atleta pertence a categoria \033[4;31;42mMIRIM\033[m')
elif idade <= 14:
    print('O atleta pertence a categoria \033[7;31;42mINFANTIL\033[m')
elif idade <= 19:
    print('O atleta pertence a categoria \033[0;35;41mJÚNIOR\033[m')
elif idade <= 25:
    print('O atleta pertence a categoria \033[0;36;47mSÊNIOR\033[m')
else:
    print('O atleta pertence a categoria \033[1;35;41mMASTER\033[m')
