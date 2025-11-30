from time import sleep
from datetime import date
ano_nascimento= int(input('Digite aqui o ano de seu nascimento:'))
idade= date.today().year-ano_nascimento
if idade <=9:
    print(f'Referente a sua idade de {idade} anos, sua categoria é \033[31mMIRIN!')
elif idade <= 14:
    print(f'Referente a sua idade de {idade} anos, sua categoria é \033[32mINFANTIL!')
elif idade <=19:
    print(f'Referente a sua idade de {idade} anos, sua categoria é \033[33mJÚNIOR!')
elif idade <=20:
    print(f'Referente a sua idade de {idade} anos, sua categoria é \033[34mSÊNIOR!')
elif idade > 20:
    print(f'Referente a sua idade de {idade} anos, sua categoria é \033[35mMASTER!')
    
print('Fim do programa de categoria de natação!')


'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
até 9 anos:Mirin
até 14 ano:Infantil
até 19 anos:Júnior
até 20 anos:Sênior
Acima:master
'''
