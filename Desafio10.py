from random import choice
from time import sleep
print('''Escolha sua jogada:
      Pedra
      Papel
      Tesoura''')
jogador= str(input('Digite aqui sua jogada Pedra, Papel ou Tesoura:')).strip().capitalize()
lista_opções= ['Pedra', 'Papel', 'Tesoura']
computador= choice(lista_opções)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
if jogador==computador:
    print(f'Computador jogou {computador} e você jogou {jogador}, houve um EMPATE!')
elif jogador=='Pedra' and computador=='Tesoura' or jogador=='Papel' and computador=='Pedra' or jogador=='Tesoura' and computador=='Papel':
    print(f'Computador jogou {computador} e você jogou {jogador}, VOCÊ VENCEU!')
elif computador=='Pedra' and jogador=='Tesoura' or computador=='Papel' and jogador=='Pedra' or computador=='Tesoura' and jogador=='Papel':
    print(f'Computador jogou {computador} e você jogou {jogador}, COMPUTADOR VENCEU!')
else:
    print('Jogoda inválida, tente novamente!')
print('Fim do programa de Jokenpô!')

'''
Crie um programa que faça o computador jogar jokenpô com você.
'''