peso= float(input('Digite aqui seu peso:'))
altura= float(input('Digite aqui sua altura:'))
imc= peso/altura**2
if imc <18.5:
    print(f'Referente ao seu IMC de {imc} você está \033[31mABAIXO DO PESO!')
elif 18.5<= imc <25:
    print(f'Referente ao seu IMC de {imc} você está com o \033[32mPESO IDEAL!')
elif 25<= imc <30:
    print(f'Referente ao seu IMC de {imc} você está com \033[31mSOBREPESO!')
elif 30<= imc <40:
    print(f'Referente ao seu IMC de {imc} você está com \033[31mOBESIDADE!')
elif imc >= 40:
    print(f'Referente ao seu IMC de {imc} você está com OBESIDADE \033[31mMÓRBIDA!')
print('Fim do programa de calcular IMC!')

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
