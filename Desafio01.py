valor_casa= float(input('Digite aqui o valor da casa que deseja comprar:'))
salario= float(input('Digite aqui o seu salário:'))
anos_pagamento= int(input('Digite aqui em quantos anos deseja pagar:'))
prestacao_mensal= valor_casa/(anos_pagamento*12)
if prestacao_mensal<=salario*0.30:
    print(f'Referente ao valor da casa de R${valor_casa:.2f} e o valor da prestação R${prestacao_mensal:.2f} seu empréstimo foi aceito!')
else:
    print(f'Referente ao valor da casa de R${valor_casa:.2f} e o valor da prestaçao R${prestacao_mensal:.2f} seu empréstimo foi negado!')
print('Obrigado por usar nossa calculadora de empréstimo!')



'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''