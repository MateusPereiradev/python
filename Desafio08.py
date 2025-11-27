produto= float(input('Digite aqui o valor do produto:'))
print('''Escolha de pagamento:
      [1] À vista no dinheiro/cheque com 10% de desconto
      [2] À vista no cartão com 5% de desconto
      [3] Em até 2x no cartão preço normal do produto
      [4] Em 3x ou mais no cartão acrescimo de 20% do valor do produto''')
forma_pagamento= int(input('Selecione aqui a forma de pagamento:'))
if forma_pagamento==1:
    desconto= produto-produto*0.10
    print(f'Referente ao valor do produto de R${produto:.2f}, o mesmo com 10% de desconto será R${desconto:.2f}!')
elif forma_pagamento==2:
    desconto= produto-produto*0.05
    print(f'Referente ao valor do produto R${produto:.2f}, o valor com 5% de desconto será R${desconto:.2f}!')
elif forma_pagamento==3:
    print(f'Referente ao valor do produto R${produto:.2f}, o mesmo nessa forma de pagamente permanece o mesmo valor!')
elif forma_pagamento==4:
    numero_parcelas= int(input('Digite aqui em quantas x deseja dividir, aceitamos até 12x com juros:'))
    prazo=produto+produto*0.20
    valor_parcelas= prazo/numero_parcelas
    print(f'Referente ao valor do produto R${produto:.2f}, o mesmo a prazo ficará no valor de R${prazo:.2f}, divido em {numero_parcelas}x o valor das parcelas serão de R${valor_parcelas:.2f}! ')

print('Obrigado por comprar em nossas lojas, volte sempre!')
'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''