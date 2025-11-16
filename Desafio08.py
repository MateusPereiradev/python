print('===== LOJAS PYTHON =====')
valor_produto= float(input('Digite aqui o valor do produto: R$'))
print('''Escolha o método de pagamento:
      [1] À vista dinheiro/cheque com 10% de desconto
      [2] À vista no cartão com 5% de desconto
      [3] Em até 2x no cartão preço normal
      [4] 3x no cartão ou mais com 20% de juros ''')
metodo_pagamento= int(input('Digite aqui a opção de pagamento desejada de 1 a 4:'))
if metodo_pagamento==1:
    valor_desconto= valor_produto-valor_produto*0.10
    print(f'Referente ao valor do produto R${valor_produto:.2f}, com 10% de desconto ficará R${valor_desconto:.2f}')

'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''