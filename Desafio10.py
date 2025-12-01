from random import choice
from time import sleep
print('''Escolha aqui sua jogada:
      Pedra
      Papel
      Tesoura''')
escolha_jogador= str(input('Digite aqui sua escolha Pedra, Papel ou Tesoura:')).strip().capitalize()
computador= ['Pedra', 'Papel', 'Tesoura']
escolha_computador= choice(computador)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
if escolha_jogador==escolha_computador:
    print(f'Referente a jogada do jogador de {escolha_jogador} e a do computador de {escolha_computador} houve um \033[32mEMPATE!')
elif escolha_jogador== 'Pedra' and escolha_computador== 'Tesoura' or escolha_jogador== 'Papel' and escolha_computador== 'Pedra' or escolha_jogador== 'Tesoura' and escolha_computador== 'Papel':
    print(f'Referente a escolha do jogador de {escolha_jogador} e a escolha do computador de {escolha_computador} o \033[32mJOGADOR VENCEU!')
elif escolha_computador== 'Pedra' and escolha_jogador== 'Tesoura' or escolha_computador== 'Papel' and escolha_jogador=='Pedra' or escolha_computador== 'Tesoura' and escolha_jogador=='Papel':
    print(f'Referente a escolha do jogador de {escolha_jogador} e a escola do computador de {escolha_computador} o \033[32mCOMPUTADOR VENCEU!')   
print('Obrigado por jogador nosso jogo de Jokenpô')

'''
Crie um programa que faça o computador jogar jokenpô com você.
'''