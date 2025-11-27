from random import choice
from time import sleep
print('''Escolha sua jogada:
      Pedra
      Papel
      Tesoura''')
jogador= str(input('Digite aqui a sua jogada Pedra, Papel ou Tesoura:')).strip().capitalize()
computador= ['Pedra', 'Papel', 'Tesoura']
jogada_computador= choice(computador)
if jogador==jogada_computador:
    print(f'Referente a jogada do jogador {jogador} e a do computador {jogada_computador} houve um EMPATE!')
if jogador=='Pedra' and jogada_computador=='Tesoura' or jogador=='Papel' and jogada_computador=='Pedra' or jogador=='Tesoura' and jogada_computador=='Papel':
    print(f'Referente a jogada do jogador {jogador} e a jogada do computador {jogada_computador} o JOGADOR VENCEU!')
if jogada_computador=='Pedra' and jogador=='Tesoura' or jogada_computador=='Papel' and jogador=='Pedra' or jogada_computador=='Tesoura' and jogador=='Papel':
    print(f'Referente a jogada do jogador {jogador} e a jogada do computador {jogada_computador} o COMPUTADOR VENCEU! ')
print('Obrigado por jogar nosso game!')


'''
Crie um programa que faça o computador jogar jokenpô com você.
'''