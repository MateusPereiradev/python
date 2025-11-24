from time import sleep
produto= float(input('Digite aqui o valor do produto:'))
print('''Escolha a forma de pagamento:
      [1] à vista dinheiro/cheque 10% de desconto
      [2] à vista no cartão com 5% de desconto
      [3] em até 2x preço normal do produto
      [4] 3x ou mais no cartão com 20% de juros''')
escolha= int(input('Escolha o metodo de pagamento:'))
print('Calculando valores...')
sleep(3)
if escolha==1:
    desconto= produto-produto*0.10
    print(f'Referente ao valor do produto de R${produto:.2f}, o valor com desconto de 10% será R${desconto:.2f}')
elif escolha==2:
    desconto= produto-produto*0.05
    print(f'Referente ao valor do produto R${produto:.2f}, o valor com 5% de desconto será R${desconto:.2f}')
elif escolha==3:
    print(f'O valor será R${produto:.2f}')
elif escolha==4:
    parcela= int(input('Escolha a quantidade de parcelas até 12x:'))
    valor_parcela= (produto+produto*0.30)/parcela
    valor_produto= produto+produto*0.20
    print(f'''Referente ao valor do produto R${produto:.2f}, o mesmo em 
          {parcela}x será R${valor_produto} e os valor das parcelas serão de R${valor_parcela:.2f}''')
print('Tenha um bom dia, e obrigado por comprar em nossas lojas!!')

'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''