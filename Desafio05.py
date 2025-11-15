n1= float(input('Digite aqui sua primeira nota:'))
n2= float(input('Digite aqui sua segunda nota:'))
nome= str(input('Digite aqui seu nome:')).strip()
media= (n1+n2)/2
if media<5.0:
    print(f'Sua média é {media}, você foi reprovado!')
elif 5.0 <= media <=6.9:
    print(f'Sua média é {media}, você está de recuperação')
else:
    print(f'Sua média é {media}, você foi aprovado!')
print(f'Tenha uma boa noite {nome}!')



'''
Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atigida:
Média abaixo de 5.0:REPROVADO
Média entre 5.0 e 6.9 RECUPERAÇÃO
Média entre 7.0 ou superior:APROVADO
'''
