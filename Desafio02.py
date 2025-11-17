from time import sleep

nome= str(input('Digite aqui seu nome:')).strip().capitalize()
num= int(input('Digite aqui um número inteiro qualquer:'))
print('''Escolha a base de conversão:
      [1] Para binário
      [2] para octal
      [3] para hexadecimal''')
escolher_base= int(input('Digite aqui a sua escolha de 1 a 3:'))
print('Calculando a base escolhida...')
sleep(3)
if escolher_base==1:
    print(f'Referente ao número {num}, o mesmo convertido para BINÁRIO é: {bin(num)[2:]}')
elif escolher_base==2:
    print(f'Referente ao número {num}, o mesmo convertido para OCTAL é: {oct(num)[2:]}')
elif escolher_base==3:
    print(f'Referente ao número {num}, o mesmo convertido para HEXADECIMAL é: {hex(num)[2:]}')
print(f'Tenha uma bom dia {nome}!!')


'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''
