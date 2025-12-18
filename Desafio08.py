produto= float(input('Digite aqui o valor do produto que deseja comprar:R$'))
print('''Escolha o método de pagamento:
      [1] À vista dinheiro/cheque
      [2] À vista no cartão
      [3] Em até 2x no cartão
      [4] 3x ou mais no cartão ''')
escolha_comprador= int(input('Escolha a opção de pagamento de 1 a 4:'))
if escolha_comprador==1:
    desconto= produto- produto*0.10
    print(f'O valor do produto com 10% de desconto será R${desconto:.2f}!')
elif escolha_comprador==2:
    desconto= produto-produto*0.05
    print(f'O valor do produto com 5% de desconto será R${desconto:.2f}!')
elif escolha_comprador==3:
    print(f'O valor do produto será parcelado em até 2x assim o seu preço será R${produto:.2f}!')
elif escolha_comprador==4:
    juros= produto+produto*0.20
    print(f'O valor do produto com 20% de juros será R${juros:.2f} dividido de 3x ou mais!')
else:
    print('Opção inválida de pagamento, tente novamente!')
print('Fim do programa de cálculo de preço final do produto!')

'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque:10% de desconto
à vista no cartão :5% de desconto
em até 2x no cartão:Preço normal
3x ou mais no cartão :20% de juros
'''