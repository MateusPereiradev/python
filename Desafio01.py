valor_casa= float(input('Digite aqui o valor da casa que deseja comprar:R$'))
valor_salario= float(input('Digite aqui o valor de seu salário:R$'))
anos_pagamento= int(input('Digite aqui em quantos anos deseja pagar:'))
prestacao= valor_casa/(anos_pagamento*12)
if prestacao<=valor_salario*0.30:
    print(f'Seu empréstimo foi APROVADO, os valores das prestações serão R${prestacao:.2f}')
else:
    print(f'Seu empréstimo foi NEGADO, os valor das prestações ultrapassam 30% de seu salário R${prestacao:.2f}')
print('Obrigado por fazer sua simulação em nosso banco!!')

'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''