from time import sleep
nota_1= float(input('Digite aqui a sua primeira nota:'))
nota_2= float(input('Digite aqui a sua segunda nota:'))
media = (nota_1+nota_2)/2
print('Calculando a média...')
sleep(3)
if media<5:
    print(f'Referente a primeira nota {nota_1} e a segunda {nota_2}, a media é {media} e você está REPROVADO!')
elif 5.0<= media <6.9:
    print(f'Referente a primeira nota {nota_1} e a segunda {nota_2}, a media é {media} e você está de RECUPERAÇÃO!')
else:
    print(f'Referente a primeira nota {nota_1} e a segunda {nota_2}, a media é {media} e você foi APROVADO!')
print('Obrigado por usar no programa de média de nota de alunos!')


'''
Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atigida: 
Média abaixo de 5.0:REPROVADO
Média entre 5.0 e 6.9 RECUPERAÇÃO
Média entre 7.0 ou superior:APROVADO
'''
