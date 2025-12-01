from datetime import date
ano_nascimento= int(input('Digite aqui o seu ano de nascimento:'))
idade= date.today().year-ano_nascimento
falta= 18-idade
passou= idade-18
if idade < 18:
    print(f'Referente a sua idade de {idade} anos, ainda faltam {falta} anos para se alistar!')
elif idade > 18:
    print(f'Referente a sua idade de {idade} anos, já passou {passou} anos para se alistar!')
elif idade==18:
    print(f'Referente sua idade de {idade} anos, está na hora de se alistar!')
print('Fim do programa de alistamento!')


'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
