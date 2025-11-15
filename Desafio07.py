peso= float(input('Digite aqui seu peso:'))
altura= float(input('Digite aqui sua altura:'))
nome= str(input('Digite aqui seu nome:'))
imc= peso/altura**2
if imc <18.5:
    print(f'Seu imc é {imc}, você está abaixo do peso!')
elif 18.5 <= imc <=25:
    print(f'Seu imc é {imc}, você está com o peso ideal!')
elif 25 <= imc <=30:
    print(f'Seu imc é {imc}, você está com sobrepeso!')
elif 30 <= imc <= 40:
    print(f'Seu imc é {imc}, você está com obesidade!')
else:
    print(f'Seu imc é {imc}, você está com obesidade mórbida!')
print(f'Tenha uma boa noite {nome}!')



'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:
Abaixo de 18.5:Abaixo do peso
Entre 18.5 e 25:peso ideal
entre 25 e 30:sobrepeso
30 até 40:obesidade
acima de 40:obesidade mórbida
#peso divido pela altura ao quadrado
'''
