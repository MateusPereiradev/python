num= int(input('Digite aqui um número inteiro:'))
print('''Escolha a base de conversão:
      [1] Binário
      [2] Octal
      [3] Hexadecimal''')
escolha_usuário= int(input('Informe aqui sua escolha:'))
if escolha_usuário==1:
    print(f'Referente ao número {num}, o mesmo convertido para binário é {bin(num)[2:]}')
elif escolha_usuário==2:
    print(f'Referente ao número {num}, o mesmo convertido para octal é {oct(num)[2:]}')
elif escolha_usuário==3:
    print(f'Referente ao número {num}, o mesmo convertido para hexadecimal é {hex(num)[2:]}')
else:
    print('Escolha inválida!')
print('Fim do programa de conversão de números!')


'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
