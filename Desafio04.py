from datetime import date
from time import sleep
ano_atual= date.today().year
nascimento= int(input('Digite aqui o ano do seu nascimento:'))
idade= ano_atual-nascimento
passou= idade-18
falta= 18-idade
print('Calculando sua idade, para ver quais passos você deve tomar...')
sleep(3)
if idade<18:
    print(f'Sua idade é {idade} anos, faltam {falta} anos para você se alistar!')
if idade==18:
    print(f'Sua idade é {idade} anos, está na hora de você se alistar!!')
elif idade>18:
    print(f'Sua idade é {idade} anos, já passou {passou} anos para você se alistar, vá até a base mais próxima para regularizar sua situação!! ')
print('Tenha um bom dia!')


'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
