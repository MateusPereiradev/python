from time import sleep
nota_1= float(input('Informe aqui sua primeira nota:'))
nota_2= float(input('Informe aqui sua segunda nota:'))
media= (nota_1+nota_2)/2
print('Calculando notas...')
sleep(3)
if media<5.0:
    print(f'Referente a sua primeira nota {nota_1} e a sua segunda nota {nota_2} sua média é {media}, você foi REPROVADO!')
elif 5.0<= media <6.9:
    print(f'Referente a sua primeira nota {nota_1} e a sua segunda nota {nota_2} sua média é {media}, você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print(f'Referente a sua primeira nota {nota_1} e a sua segunda nota {nota_2} sua média é {media}, você foi APROVADO ')
print('Fim do programa')


'''
Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atigida: 
Média abaixo de 5.0:REPROVADO
Média entre 5.0 e 6.9 RECUPERAÇÃO
Média entre 7.0 ou superior:APROVADO
'''
