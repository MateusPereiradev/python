valor_casa= float(input('Digite o valor da casa:R$'))
salário_comprador= float(input('Digite o salário do comprador:R$'))
anos_pagamento= int(input('Em quantos anos será pago?'))
prestação_mensal= valor_casa/(anos_pagamento*12)
if prestação_mensal <= salário_comprador*0.30:
    print(f'O empréstimo foi \033[32mAPROVADO\033[m, o valor da prestação mensal será R${prestação_mensal:.2f}!')
else:
    print(f'O empréstimo foi \033[31mNEGADO\033[m, o valor da prestação calculada foi R${prestação_mensal:.2f}!')
print('Fim do programa de empréstimo bancário!')
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''