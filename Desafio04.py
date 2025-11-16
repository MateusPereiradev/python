from datetime import date
ano_nascimento= int(input('Digite aqui o seu ano de nascimento:'))
ano_atual= date.today().year
nome= str(input('Digite aqui seu nome:')).strip()
idade= ano_atual-ano_nascimento
falta_anos= 18-idade
passou= idade-18
if idade <18:
    print(f'Você tem {idade} anos\n ainda falta {falta_anos} anos para o alistamento militar!')
elif idade==18:
    print(f'Você tem {idade} anos \n está na hora de se alistar ao serviço militar!')
else:
    print(f'Você tem {idade} anos \n já passou {passou} anos do tempo de alistamento militar!')
print(f'Tenha um bom dia {nome}!')


'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
