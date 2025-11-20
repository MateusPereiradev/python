valor_casa= float(input('Digite aqui o valor da casa que desaja comprar: R$'))
salario_comprador= float(input('Digite aqui o seu salário: R$'))
anos_pagamento= int(input('Em quantos anos você deseja pagar a casa?'))
prestacao_mensal= valor_casa/(anos_pagamento*12)
if prestacao_mensal<=(salario_comprador*0.30):
    print(f'''Seu empréstimo foi aprovado, parabéns!
    O valor da prestação mensal será de R${prestacao_mensal:.2f}''')
else:
    print('Seu empréstimo foi negado, tente novamente mais tarde.')
print('Obrigado por utilizar nosso sistema de empréstimos bancários!')

'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''