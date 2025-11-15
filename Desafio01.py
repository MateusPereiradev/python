casa_valor= float(input('Digite aqui o valor da casa que deseja comprar: R$'))
salario_comprador= float(input('Digite aqui o seu salário: R$'))
anos_pagamento= int(input('Digite aqui em quantos anos você pretende pagar:'))
mensal=anos_pagamento*12
prestacao_mensal=casa_valor/mensal
salario_30= salario_comprador*0.30
if prestacao_mensal <= salario_30:
    print(f'Referente ao valor da casa R${casa_valor:.2f}, seu empréstimo foi aprovado!\n o valor da prestação mensal será R${prestacao_mensal:.2f}')
else:
    print(f'Referente ao valor da casa R${casa_valor:.2f}, seu empréstimo foi negado!')
print('Fim do programa')
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''