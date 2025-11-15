from datetime import date
nascimento= int(input('Digite aqui o ano de nascimento do atleta:'))
nome= str(input('Digite aqui seu nome:')).strip()
ano_atual= date.today().year
idade_atleta= ano_atual-nascimento
if idade_atleta<=9:
    print(f'Você tem {idade_atleta} anos, e está na categoria Mirin!')
elif idade_atleta<=14:
    print(f'Você tem {idade_atleta} anos, e está na categoria Infantil!')
elif idade_atleta <=19:
    print(f'Você tem {idade_atleta} anos, e está na categoria Júnior!')
elif  idade_atleta<=20:
    print(f'Você tem {idade_atleta} anos, e está na categoria Sênior!')
else:
    print(f'Você tem {idade_atleta} anos, e está na categoria Master!')
print(f'Tenha uma boa noite {nome}!')

'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
até 9 anos:Mirin
até 14 ano:Infantil
até 19 anos:Júnior
até 20 anos:Sênior
Acima:master
'''
