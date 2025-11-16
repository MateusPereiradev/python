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
elif metodo_pagamento==2:
    valor_desconto=valor_produto-valor_produto*0.05
    print(f'Referente ao valor do produto R${valor_produto:.2f}, com 5% de desconto ficará R${valor_desconto:.2f}')
elif metodo_pagamento==3:
    print(f'Referente ao valor do produto R${valor_produto:.2f}, em até 2x no cartão o preço será o normal.')
else:
    valor_juros= valor_produto+valor_produto*0.30
    print(f'Referente ao valor do produto R${valor_produto:.2f}, em 3x ou mais no cartão terá 20% de juros, ficando R${valor_juros:.2f}')
print('Obrigado por comprar na nossa LOJA PYTHON! Volte Sempre!')    

'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''