valor_produto= float(input('Digite aqui o valor do produto que deseja comprar:'))
print('''Métodos de pagamento:
      [1] À vista dinheiro/cheque com 10% de desconto
      [2] À vista no cartão com 5% de desconto
      [3] Em até 2x no cartão preço normal do produto
      [4] 3x ou mais no cartão de crédito 20% de juros''')
escolha_comprador= int(input('Digite aqui o método de pagamento que deseja:'))
if escolha_comprador==1:
    desconto= valor_produto-valor_produto*0.10
    print(f'Referente ao valor do produto R${valor_produto:.2f} o mesmo com 10% de desconto será R${desconto:.2f}!')
elif escolha_comprador==2:
    desconto= valor_produto-valor_produto*0.05
    print(f'Referente ao valor do produto R${valor_produto:.2f} o mesmo com 5% de desconto será R${desconto:.2f}!')
elif escolha_comprador==3:
    print(f'O valor do produto será R${valor_produto:.2f}!')
elif escolha_comprador==4:
    juros= valor_produto+valor_produto*0.20
    print(f'Referente ao valor do produto de R${valor_produto:.2f} o mesmo em 3x ou mais no cartão será R${juros:.2f}!')
else:
    print('Escolha inválida!')
print('Obrigado por comprar em nossas lojas!')

'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''