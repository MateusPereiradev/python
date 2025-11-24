from datetime import date
from time import sleep
nascimento= int(input('Digite aqui o ano de seu nascimento:'))
ano_atual= date.today().year
idade=ano_atual-nascimento
falta_alistar=18-idade
passou_alistar= idade-18
print('Calculando idade...')
sleep(3)
if idade<18:
    print(f'Você tem {idade} anos, ainda faltam {falta_alistar} anos para se alistar!')
elif idade>18:
    print(f'Você tem {idade} anos, já passou {passou_alistar} anos para se alistar!')
else:
    print(f'Você tem {idade} anos, está na hora de se alistar')
print('Obrigado por usar nosso programa de conversão!')
'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
