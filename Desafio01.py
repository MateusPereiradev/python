valor_casa= float(input('Digite aqui o valor da casa que deseja comprar:R$'))
salário_comprador= float(input('Digite aqui o valor do seu salário:R$'))
anos_pagamento= int(input('Informe aqui em quantos anos deseja pagar:'))
prestação= valor_casa/(anos_pagamento*12)
if prestação <= salário_comprador*0.30:
    print(f'Referente ao valor da casa de R${valor_casa:.2f}, as prestações em {anos_pagamento} anos serão de R${prestação:.2f}, seu empréstimo foi \033[32mAPROVADO!')
elif prestação > salário_comprador*0.30:
    print(f'Referente ao valor da casa de R${valor_casa:.2f}, as prestações em {anos_pagamento} anos serão de R${prestação:.2f}, seu empréstimo foi \033[31mNEGADO!')
print('Fim do programa de empréstimo!')


'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''