nascimento= int(input('Digite aqui o ano de seu nascimento:'))
idade= 2025-nascimento
falta= 18-idade
passou= idade-18
if idade<18:
    print(f'''Sua idade é de {idade} anos, você ainda vai se alistar no exército!
          Ainda faltam {falta} anos para se alistar''')
elif idade==18:
    print(f"Você tem {idade} anos, está na hora de se alistar!")
else:
    print(f'''Você tem {idade} anos, e já passou da hora de se alistar!!
          Já passou {passou} anos para se alistar!''')
print('Tenha uma boa noite!')

'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
