from datetime import date
ano_nascimento= int(input('Digite aqui o seu ano de nascimento:'))
ano_atual= date.today().year
idade= ano_atual-ano_nascimento
if idade <=9:
    print(f'Referente a sua idade de {idade} anos, sua categoria é MIRIN!')
elif idade <=14:
    print(f'Referente a sua idade de {idade} anos, sua categoria é INFANTIL!')
elif idade <=19:
    print(f'Referente a sua idade de {idade} anos, sua categoria é JÚNIOR!')
elif idade <=20:
    print(f'Referente a sua idade de {idade} anos, sua categoria é SÊNIOR!')
else:
    print(f'Referente a sua idade de {idade} anos, sua categoria é MASTER!')
print('Fim do programa')

'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
até 9 anos:Mirin
até 14 ano:Infantil
até 19 anos:Júnior
até 20 anos:Sênior
Acima:master
'''
