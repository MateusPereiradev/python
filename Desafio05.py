nome= str(input('Digite aqui seu nome:')).strip().capitalize()
nota_1= float(input('Digite aqui a primeira nota:'))
nota_2= float(input('Digite aqui a segunda nota:'))
media= (nota_1+nota_2)/2
if media < 5.0:
    print(f'Sua média é de {media}, voce foi REPROVADO!')
elif 5.0<= media <=6.9:
    print(f'Sua média é de {media}, você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print(f'Sua média é de {media}, você está APROVADO!')
print(f'Tenha uma ótima tarde {nome}')


'''
Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atigida: 
Média abaixo de 5.0:REPROVADO
Média entre 5.0 e 6.9 RECUPERAÇÃO
Média entre 7.0 ou superior:APROVADO
'''
