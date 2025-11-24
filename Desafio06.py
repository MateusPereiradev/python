from datetime import date
nascimento= int(input('Digite aqui o ano de seu nascimento:'))
ano_atual= date.today().year
idade= ano_atual-nascimento
if idade<= 9:
    print(f'Você tem {idade} anos e está na categoria MIRIN!')
elif idade<= 14:
    print(f'Você tem {idade} anos e está na categoria INFANTIL!')
elif idade<= 19:
    print(f'Você tem {idade} anos e está na categoria JÚNIOR!')
elif idade<= 20:
    print(f'Você tem {idade} anos e está na categoria SÊNIOR!')
else:
    print(f'Você tem {idade} anos e está na categoria MASTER!')
print('Obrigado por usar nosso programa!')


'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
até 9 anos:Mirin
até 14 ano:Infantil
até 19 anos:Júnior
até 20 anos:Sênior
Acima:master
'''
