valor_casa= float(input('Digite aqui o valor da casa que deseja comprar:'))
salario_comprador= float(input('Digite aqui o valor do seu salário:R$'))
anos_pagamento= int(input('Em quantos anos deseja pagar?'))
valor_parcelas=valor_casa/(anos_pagamento*12)
if valor_parcelas<= salario_comprador*0.30:
    print(f'Seu empréstimo foi APROVADO, o valor das parcelas será R${valor_parcelas:.2f}.')
else:
    print(f'Seu empréstimo foi NEGADO, o valor das parcelas ultrapassam 30% de seu salario!')
print('Obrigado por escolher nosso banco!')


'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''