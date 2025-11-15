valor_produto= float(input('Digite aqui o valor do produto: R$'))
nome= str(input('Digite aqui o seu nome:')).strip()
print('''Escolha a forma de pagamento:
      [1] À vista dinheiro/cheque 10% de desconto
      [2] À vista no cartão 5% de desconto
      [3] Em até 2x no cartão preço normal
      [4] 3x ou mais no cartão 20% de juros''')
forma_pagamento= int(input('Escolha a forma de pagamento de 1 a 4:'))
if forma_pagamento==1:
    print(f'O valor do produto é R${valor_produto:.2f}, com 10% de desconto passará para R${valor_produto-valor_produto*0.10:.2f}')
elif forma_pagamento==2:
    print(f'O valor do produto é R${valor_produto:.2f}, com 5% de desconto passará para R${valor_produto-valor_produto*0.05:.2f}')
elif forma_pagamento==3:
    print(f'O valor do produto é R${valor_produto:.2f}, parcelado em 2x no cartão, permanecerá o mesmo preço.')
else:
    print(f'O valor do produto é R${valor_produto:.2f}, em 3x ou mais no cartão, com 20% de juro será R${valor_produto+valor_produto*0.20:.2f}')

'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''