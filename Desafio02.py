num= int(input('Digite aqui um número inteiro qualquer:'))
print('''Escolha sua base de conversão:
      [1] Binário
      [2] Octal
      [3] Hexadecimal''')
escolha_usuário= int(input('Digite aqui sua escolha para conversão:'))
if escolha_usuário==1:
    print(f'Referente ao número {num}, a base convertida para binário é {bin(num)[2:]}')
elif escolha_usuário==2:
    print(f'Referente ao número {num}, a base convertida para octal é {oct(num)[2:]}')
elif escolha_usuário==3:
    print(f'Referente ao número {num}, sua base convertida para hexadecimal é {hex(num)[2:]}')
print('Obrigado por usar nosso programa de base de conversões!')


'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
