from datetime import date
from time import sleep
nascimento= int(input("Digite aqui o nascimento do atleta:"))
idade= date.today().year-nascimento
print("Calculando categorias...")
sleep(3)
if idade<=9:
    print(f"Sua idade é {idade} anos, sua categoria é MIRIN!")
elif idade<=14:
    print(f"Sua idade é {idade} anos, sua categoria é INFANTIL!")
elif idade<=19:
    print(f"Sua idade é {idade} anos, sua categoria é JÚNIOR!")
elif idade<=20:
    print(f"Sua idade é {idade} anos, sua categoria é SÊNIOR!")
elif idade>20:
    print(f"Sua idade é {idade} anos, sua categoria é MASTER!")
print("Tenha uma ótima noite!!")
'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
até 9 anos:Mirin
até 14 ano:Infantil
até 19 anos:Júnior
até 20 anos:Sênior
Acima:master
'''
