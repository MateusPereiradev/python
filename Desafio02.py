num= int(input('Digite aqui um número inteiro qualquer:'))
print('''Escolha a base de conversão:
      [1] para binário
      [2] para octal
      [3] para hexadecimal''')
escolha_usuario= int(input('Escolha aqui a sua opção de conversão:'))
if escolha_usuario==1:
    print(f'Referente ao número {num}, sua conversão para binário é {bin(num)[2:]}')
elif escolha_usuario==2:
    print(f'Referente ao número {num}, sua conversão para octal é {oct(num)[2:]}')
elif escolha_usuario==3:
    print(f'Referente ao número {num}, sua conversão para hexadecimal é {hex(num)[2:]}')
print('Obrigado por usar nosso conversor!')


'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
