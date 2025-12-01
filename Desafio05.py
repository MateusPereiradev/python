from time import sleep
nota_1= float(input('Digite aqui o valor de sua primeira nota:'))
nota_2= float(input('Digite aqui o valor de sua segunda nota:'))
média= (nota_1+nota_2)/2
print('Calculando seu resultado...')
sleep(3)
if média < 5.0:
    print(f'Referente sua média de {média}, você foi \033[31mREPROVADO!')
elif 5.0<= média <6.9:
    print(f'Referente sua média de {média}, você está de \033[34mRECUPERAÇÃO!')
elif média >= 7.0:
    print(f'Referente sua média de {média}, você foi \033[32mAPROVADO!')
print('Fim do programa de média de nota!')


'''
Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atigida: 
Média abaixo de 5.0:REPROVADO
Média entre 5.0 e 6.9 RECUPERAÇÃO
Média entre 7.0 ou superior:APROVADO
'''
