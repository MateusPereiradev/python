from datetime import date
ano_nascimento= int(input('Digite aqui seu ano de nascimento:'))
idade= date.today().year - ano_nascimento
if idade <= 9:
    print(f'Com {idade} anos você está na categoria \033[34mMIRIM!')
elif idade <= 14:
    print(f'Com {idade} anos você está na categoria \033[34mINFANTIL!')
elif idade <= 19:
    print(f'Com {idade} anos você está na categoria \033[34mJÚNIOR!')
elif idade ==20:
    print(f'Com {idade} anos você está na categoria \033[34mSÊNIOR!')
else:
    print(f'Com {idade} anos você está na categoria \033[34mMASTER!')
print('Fim do programa de categorização de atletas!')

'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
até 9 anos:Mirin
até 14 ano:Infantil
até 19 anos:Júnior
até 20 anos:Sênior
Acima:master
'''
