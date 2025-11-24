num= int(input('Digite aqui um número inteiro qualquer:'))
print('''Escolha aqui sua base de conversão:
      [1] Para binário
      [2] Para OCTAL
      [3] Para Hexadecimal''')
escolha_usuario= int(input('Escolha sua opção para ser feita a base de conversão:'))
if escolha_usuario==1:
    print(f'A base de conversão do número {num} para Binário é {bin(num)[2:]}')
elif escolha_usuario==2:
    print(f'A base de conversão do número {num} para octal é {oct(num)[2:]}')
elif escolha_usuario==3:
    print(f'A base de conversão do número {num} para hexadecimal é {hex(num)[2:]}')
print('Obrigado por usuar nosso programa de conversão númerica!')

'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
