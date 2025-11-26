peso= float(input('Digite aqui o seu peso:'))
altura= float(input('Digite aqui a sua altura:'))
imc= peso/altura**2
if imc < 18.5:
    print(f'Referente ao seu IMC de {imc:.2f}, você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print(f'Referente ao seu IMC de {imc:.2f}, você com o PESO IDEAL!')
elif 25 <= imc < 30:
    print(f'Referente ao seu IMC de {imc:.2f}, você está com SOBREPESO!')
elif 30 <= imc < 40:
    print(f'Referente ao seu IMC de {imc:.2f}, você está com OBESIDADE!')
elif peso >=40:
    print(f'Referente ao seu IMC {imc:.2f}, você está com OBESIDADE MÓRBIDA!')
print('Obrigado por usar nosso conversor de IMC!')



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
