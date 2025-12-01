valor_casa= float(input('Digite aqui o valor da casa que deseja:'))
salário= float(input('Digite aqui o valor do seu salário:'))
<<<<<<< HEAD
anos= int(input('Digite aqui em quantos anos deseja pagar:'))
prestação= valor_casa/(anos*12)
if prestação <= salário*30:
    print(f'Referente ao valor da casa de R${valor_casa:.2f} a prestação será R${prestação:.2f} em {anos} anos, sendo assim seu empréstimo foi \033[32mAPROVADO!')
else:
    print(f'Referente ao valor da casa de R${valor_casa:.2f} a prestação será R${prestação:.2} sendo assim seu empréstimo foi \033[31mNEGADO!')
print('Fim do programa de empréstimo!')
=======
anos_pagamento= int(input('Digite aqui em quantos anos deseja pagar:'))
prestação= valor_casa/(anos_pagamento*12)
if prestação<=salário*0.30:
    print(f'O valor da casa escolhida é R${valor_casa:.2f}, o valor das prestações divididas em {anos_pagamento} anos será R${prestação:.2f}, sendo assim seu empréstimo foi APROVADO!')
else:
    print(f'Referete ao valor da casa R${valor_casa:.2f}, o valor das prestações divididas em {anos_pagamento} anos será R${prestação:.2f}, sendo assim seu empréstimo foi NEGADO!')
print('Obrigado por usar nossos meios de crédito!')


>>>>>>> 11659a7bff77a8f745c2ada2b8315648b9fb3b64
'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''