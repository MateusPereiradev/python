from time import sleep
print('=='*25)
print('===== Simulador de Empréstimo Bancário =====')
print('=='*25)
nome= str(input('Digite aqui o seu nome:')).strip().capitalize()
valor_casa= float(input('Digite o valor da casa: R$'))
salario= float(input('Digite o seu salário: R$'))
anos= int(input('Em quantos anos você pretende pagar a casa?'))
prestacao= valor_casa/(anos*12)
porcentagem_salario= salario*0.30
print('Analisando as informações...')
sleep(3)
if prestacao <= porcentagem_salario:
    print(f'Empréstimo APROVADO! Referente ao valor da casa R${valor_casa:.2f}, com o salário de R${salario:.2f}, as prestações mensais serão de R${prestacao:.2f}.')
else:
    print(f'Empréstimo NEGADO! Referente ao valor da casa R${valor_casa:.2f}, com o salário de R${salario:.2f}, as prestações mensais serão de R${prestacao:.2f}')
print(f'Tenha um bom dia {nome}!!')



'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''