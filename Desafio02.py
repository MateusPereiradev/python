num=int(input('Digite aqui um número inteiro para ser feita a conversão:'))
print('''Escolha aqui sua base de conversão:
      [1] Binário
      [2] Octal
      [3] Hexadecimal''')
escolha_usuario= int(input('Digite aqui a sua escolha para conversão do número inteiro:'))
if escolha_usuario==1:
    print(f'Referente ao número inteiro {num}, sua base convertida para Binário é {bin(num)[2:]}')

'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
