n1= float(input('Digite aqui a primeira nota do aluno:'))
n2= float(input('Digite aqui a segunda nota do aluno:'))
nome= str(input('Digite aqui o nome do aluno:'))
media= (n1+n2)/2
if media <5:
    print(f'A média do aluno é {media}, o aluno está REPROVADO!')
elif 5.0<= media <=6.9:
    print(f'A média do aluno é {media}, o aluno está de RECUPERAÇÃO!')
else:
    print(f'A media do aluno é {media}, o aluno está APROVADO!')
print(f'Tenha uma boa noite {nome}!')

'''
Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atigida:
Média abaixo de 5.0:REPROVADO
Média entre 5.0 e 6.9 RECUPERAÇÃO
Média entre 7.0 ou superior:APROVADO
'''
