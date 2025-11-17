from datetime import date
from time import sleep
nome= str(input('Digite aqui seu nome:')).strip().capitalize()
nascimento= int(input('Digite aqui o ano do seu nascimento:'))
ano_atual= date.today().year
idade= ano_atual-nascimento
print('Calculando categoria...')
sleep(3)
if idade <=9:
    print(f'Sua idade é de {idade} anos, você está na categoria MIRIN!')
elif idade <=14:
    print(f'Sua idade é de {idade} anos, você está na categoria INFANTIL!')
elif idade <=19:
    print(f'Sua idade é de {idade} anos, você está na categoria JÚNIOR!')
elif idade <=20:
    print(f'Sua idade é de {idade} anos, você está na categoria SENIOR!')
elif idade>20:
    print(f'Sua idade é de {idade} anos, você está na categoria MASTER! ')
print(f'Tenha um bom dia {nome}!')
'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
até 9 anos:Mirin
até 14 ano:Infantil
até 19 anos:Júnior
até 20 anos:Sênior
Acima:master
'''
