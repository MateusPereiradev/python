casa= float(input('Digite aqui o valor da casa:'))
salario= float(input('Digite aqui o valor do seu salário:'))
anos= int(input('Digite aqui em quantos anos você quer pagar:'))
nome= str(input('Digite aqui seu nome:')).strip()
prestacao=casa/(anos*12)
salario_30= salario*0.30
if prestacao<= salario_30:
    print(f'Seu emprestimo de R${casa:.2f} foi aceito, as prestações vão custar R${prestacao:.2f}')
else:
    print(f'Seu emprestimo de R${casa:.2f} foi negado, pois ultrapassa 30% de seu salario que é R${salario_30:.2f}')
print(f'Tenha uma boa noite {nome}!')



'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''