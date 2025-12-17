num= int(input('Digite aqui um número inteiro qualquer:'))
print('''Escolha uma das bases para conversão:
      [1] Converter para BINÁRIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL''')
opção= int(input('Escolha sua opção de conversão de 1 a 3:'))
if opção==1:
    print(f'O número {num} convertido para BINÁRIO é {bin(num)[2:]}!')
elif opção==2:
    print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}!')
elif opção==3:
    print(f'O número {num} convertido para HEXADECIMAL é {hex(num)[2:]}!')
    print('Fim do programa de conversão de bases numéricas!')
'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
