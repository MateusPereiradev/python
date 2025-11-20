num= int(input('Digite aqui um número inteiro:'))
for leia in range(2,12):
    if num%leia==0:
        print(f'{num} é um número primo!')
    else:
        print(f'{num} não é um número primo!')

'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''