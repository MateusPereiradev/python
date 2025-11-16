from time import sleep
nome= str(input('Digite aqui seu nome:')).strip()
peso= float(input('Digite aqui seu peso:'))
altura= float(input('Digite aqui sua altura:'))
imc= peso/altura**2
print('Calculando seu IMC...')
sleep(3)
if imc<18.5:
    print(f'Seu IMC é {imc:.2f}, você está ABAIXO DO PESO.')
elif 18.5<=imc<25:
    print(f'Seu IMC é {imc:.2f}, você está no PESO IDEAL.')
elif 25<=imc<30:
    print(f'Seu IMC é {imc:.2f}, você está em SOBREPESO.')
elif 30<=imc<40:
    print(f'Seu IMC é {imc:.2f}, você está em OBESIDADE.')
else:
    print(f'Seu IMC é {imc:.2f}, você está em OBESIDADE MÓRBIDA;')
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
