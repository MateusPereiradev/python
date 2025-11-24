<<<<<<< HEAD
valor_casa= float(input('Digite aqui o valor da casa que deseja comprar:'))
salario_comprador= float(input('Digite aqui o valor do seu salário:R$'))
anos_pagamento= int(input('Em quantos anos deseja pagar?'))
valor_parcelas=valor_casa/(anos_pagamento*12)
if valor_parcelas<= salario_comprador*0.30:
    print(f'Seu empréstimo foi APROVADO, o valor das parcelas será R${valor_parcelas:.2f}.')
else:
    print(f'Seu empréstimo foi NEGADO, o valor das parcelas ultrapassam 30% de seu salario!')
print('Obrigado por escolher nosso banco!')
=======
valor_casa= float(input('Digite aqui o valor da casa que deseja comprar:R$'))
valor_salario= float(input('Digite aqui o valor de seu salário:R$'))
anos_pagamento= int(input('Digite aqui em quantos anos deseja pagar:'))
prestacao= valor_casa/(anos_pagamento*12)
if prestacao<=valor_salario*0.30:
    print(f'Seu empréstimo foi APROVADO, os valores das prestações serão R${prestacao:.2f}')
else:
    print(f'Seu empréstimo foi NEGADO, os valor das prestações ultrapassam 30% de seu salário R${prestacao:.2f}')
print('Obrigado por fazer sua simulação em nosso banco!!')

>>>>>>> 4ec890497deb2e817b786e779d65e2bcb0d7ead3
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''