from time import sleep
nota_1= float(input('Digite aqui o valor da primeira nota:'))
nota_2= float(input('Digite aqui o valor da segunda nota:'))
media= (nota_1+nota_2)/2
if media < 5.0:
    print(f'Referente a sua média de {media}, você foi \033[31mREPROVADO!')
elif 5.0<= media < 6.9:
    print(f'Referente a sua média de {media}, você está de \033[36mRECUPERAÇÃO!')
elif media >=7.0:
    print(f'Referente a sua média de {media}, você está \033[32mAPROVADO!')
print('Fim do programa de média de notas do aluno!')
'''
Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atigida: 
Média abaixo de 5.0:REPROVADO
Média entre 5.0 e 6.9 RECUPERAÇÃO
Média entre 7.0 ou superior:APROVADO
'''
