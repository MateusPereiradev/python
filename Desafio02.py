num= int(input('Digite aqui um número inteiro:'))
nome= str(input('Digite aqui seu nome:')).strip()
print('''Qual será a base de conversão?
      [1] para binário
      [2] para octal
      [3] para hexadecimal''')
conversao= int(input('Digite aqui a opção que você deseja:'))
if conversao==1:
    print(f'A conversão do número {num} para binário é {bin(num)[2:]}')
if conversao==2:
    print(f'A conversão do número {num} para octal é {oct(num)[2:]}')
if conversao==3:
    print(f'A conversão do número {num} para hexadecimal é {hex(num)[2:]}')
print(f'Tenha uma boa noite {nome}')


'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
