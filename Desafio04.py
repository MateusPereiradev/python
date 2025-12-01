from datetime import date
ano_nascimento= int(input('Digite aqui o ano de seu nascimento:'))
idade= date.today().year-ano_nascimento
falta= 18-idade
passou= idade-18
if idade < 18:
    print(f'Você tem {idade} anos, ainda faltam {falta} anos para se alistar no exército!')
elif idade > 18:
    print(f'Você tem {idade} anos, já passou {passou} anos para se alistar no exército!')
elif idade==18:
    print(f'Você tem {idade} anos, está na hora de se alistar para o exército!')
print('Fim do programa de alistamento, obrigado!')




'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
