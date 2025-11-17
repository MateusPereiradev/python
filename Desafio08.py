from time import sleep
print('=='*15)
print('===== LOJAS PYTHON ======')
print('=='*15)  
valor_produto= float(input('Digite aqui o valor do produto:'))
print('''Qual será a forma de pagamento:
      [1] À vista dinheiro/cheque com 10% de desconto
      [2] À vista no cartão com 5% de desconto
      [3] Em até 2x no cartão será o preço normal
      [4] 3x ou mais no cartão 20% de juros''')
escolher_metodo= int(input('Digite aqui de 1 a 4 o metodo de pagamento:'))
print('Calculando preços...')
sleep(3)
print('Só mais um instante...')
sleep(2)
if escolher_metodo==1:
    desconto= valor_produto*0.10
    print(f'Referente ao valor do produto de R${valor_produto:.2f}, com o desconto de 10% o valor será R${valor_produto-desconto:.2f}')
elif escolher_metodo==2:
    desconto= valor_produto*0.05
    print(f'Referente ao valor do produto R${valor_produto:.2f}, com o desconto de 5% o valor será R${valor_produto-desconto}')
elif escolher_metodo==3:
    print(f'O valor do produto será normal, sendo assim você pagará R${valor_produto:.2f}')
elif escolher_metodo==4:
    parcelas= int(input('Digite aqui em quantas vezes você quer dividir:'))
    juros= valor_produto+valor_produto*0.20
    dividido= juros/parcelas
    print(f'Referente ao valor do produto R${valor_produto:.2f}, em {parcelas}x, o valor do produto será R${juros:.2f} e o valor das parcelas serão R${dividido:.2f}')
else:
    print('Opção invalida, tente novamente!!')
print('Obrigado por comprar em nossas lojas!')




'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''