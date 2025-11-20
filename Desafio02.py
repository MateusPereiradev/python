num= int(input('Digite um número inteiro qualquer:'))
print('''Escolha uma das bases para conversão
      [1] Converter para BINÁRIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL''')
escolha= int(input('Digite aqui a sua escolha:'))
if escolha==1:
    print(f'O número {num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif escolha==2:
    print(f'O número {num} convertido para OCTAL é igual {oct(num)[2:]}')
elif escolha==3:
    print(f'O número {num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
print('Obrigado por utilizar nosso sistema de conversão de bases numéricas!')

'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
