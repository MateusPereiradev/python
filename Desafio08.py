valor_produto= float(input('Digite aqui o valor do produto:'))
nome= str(input('Digite aqui seu nome:'))
print('''Qual será a forma de pagamento?
      [1] à vista dinheiro/chegue tem 10% de desconto
      [2] à vista no cartão tem 5% de desconto
      [3] em até 2x no cartão o preço é normal
      [4] 3x ou mais no cartão tem um acrescimo de 20% de juros''')
forma_pagamento= int(input('Selecione aqui a forma de pagamento:'))
if forma_pagamento==1:
    print(f'O valor do produto à vista é R${valor_produto-valor_produto*0.10:.2f}')
elif forma_pagamento==2:
    print(f'O valor do produto no cartão à vista é R${valor_produto-valor_produto*0.05:.2f}')
elif forma_pagamento==3:
    print(f'O valor do produto em até 2x no cartão é R${valor_produto:.2f}')
else:
    print(f'O valor do produto em 3x ou mais é R${valor_produto+valor_produto*0.20:.2f}')
print(f'Tenha uma boa noite {nome}')


'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''