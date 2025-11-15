nascimento= int(input('Digite aqui o seu ano de nascimento:'))
nome= str(input('Digite aqui seu nome:')).strip()
idade=2025-nascimento
falta= 18-idade
passou= idade-18
if idade<18:
    print(f'Você tem {idade} anos, e ainda faltam {falta} anos para se alistar!')
if idade==18:
    print(f'Você tem {idade} anos, está na hora de se alistar!')    
if idade>18:
    print(f'Você tem {idade} anos, já passou {passou} anos para se alistar!')
print(f'Tenha uma boa noite, {nome}!')



'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
