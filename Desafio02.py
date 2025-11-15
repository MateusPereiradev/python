num= int(input('Digite aqui um número inteiro qualquer:'))
print('''Escolha a base de conversão:
      [1] para binário
      [2] para octal
      [3] para hexadecimal''')
escolha_base= int(input('Escolha aqui a base de conversão de 1 a 3:'))
if escolha_base==1:
    print(f'Referente ao número {num}, em binário será {bin(num)[2:]}')
elif escolha_base==2:
    print(f'Referente ao número {num}, em octal será {oct(num)[2:]}')
elif escolha_base==3:
    print(f'Referente ao número {num}, em hexadecimal será {hex(num)[2:]}')
print('Fim do programa')

'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
