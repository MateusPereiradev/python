nota_1= float(input('Informe aqui sua primeira nota:'))
nota_2= float(input('Informe aqui sua segunda nota:'))
média= (nota_1+nota_2)/2
if média < 5.0:
    print(f'Sua média foi {média:.1f} você está \033[31mREPROVADO!')
elif 5.0 <= média < 7.0:
    print(f'Sua média foi {média:.1f} você está de \033[33mRECUPERAÇÃO!')
elif média >= 7.0:
    print(f'Sua média foi {média:.1f} voce está \033[32mAPROVADO!')
print('Fim do programa de cálculo de média escolar!')


'''
Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atigida: 
Média abaixo de 5.0:REPROVADO
Média entre 5.0 e 6.9 RECUPERAÇÃO
Média entre 7.0 ou superior:APROVADO
'''
