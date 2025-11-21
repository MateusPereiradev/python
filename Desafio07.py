from time import sleep
peso= float(input('Digite aqui seu peso:'))
altura= float(input('Digite aqui sua altura:'))
imc= peso/altura**2
print('Calculando IMC...')
sleep(3)
if imc<18.5:
    print(f"Seu IMC é {imc}, você está ABAIXO do peso!")
elif 18.5<= imc < 25:
    print(f'Seu IMC é {imc}, você está com o peso IDEAL!')
elif 25<= imc <30:
    print(f'Seu IMC é {imc}, você está com SOBREPESO!')
elif 30<= imc <40:
    print(f'Seu IMC é {imc}, você está com OBESIDADE!')
elif imc>40:
    print(f'Seu IMC é {imc}, você está com OBESIDADE MÓRBIDA!')
print('Tenha uma boa noite!')



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
