valor_produto= float(input('Digite aqui o valor do produto:'))
print('''Escolha aqui a forma de pagamento:
      [1] à vista dinheiro/cheque com 10% de desconto
      [2] à vista no cartão com 5% de desconto
      [3] em até 2x no cartão preço normal
      [4] em 3x ou mais no cartão 20% de juros''')
escolha_comprador= int(input('Escolha aqui sua forma de pagamento de 1 a 4:'))
if escolha_comprador==1:
    desconto= valor_produto-valor_produto*0.10
    print(f'Referente ao valor do produto de R${valor_produto:.2f} com o desconto de 10% ficará \033[32mR${desconto:.2f}!')
elif escolha_comprador==2:
    desconto= valor_produto-valor_produto*0.05
    print(f'Referente ao valor do produto de R${valor_produto:.2f} com o desconto de 5% ficará \033[32mR${desconto:.2f}!')
elif escolha_comprador==3:
    print(f'O valor do produto será o mesmo em 2x no cartão de crédito!')
elif escolha_comprador==4:
    juros=valor_produto+valor_produto*0.20
    print(f'Referente ao valor do produto R${valor_produto:.2f} o mesmo com pagamento a prazo será \033[32mR${juros:.2f}!')
    
print('Obrigado por comprar em nossas lojas!')


'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''