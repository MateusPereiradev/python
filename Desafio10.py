from random import choice
from time import sleep
print('===== Jokenpô=====')
print('''Escolha aqui sua jogada:
      [1] Pedra
      [2] Papel
      [3] Tesoura''')
escolha_jogador= str(input('Digite aqui sua escolha: Pedra, Papel ou Tesoura:')).strip().capitalize()
computador= ['Pedra', 'Papel', 'Tesoura']
escolha_computador= choice(computador)
if escolha_jogador==escolha_computador:
    print(f'A escolha do jogador foi {escolha_jogador} e a escolha do computador foi {escolha_computador}, sendo assim houve um EMPATE.')
elif escolha_jogador=='Pedra' and escolha_computador=='Tesoura' or escolha_jogador=='Papel' and escolha_computador=='Pedra' or escolha_jogador=='Tesoura' and escolha_computador=='Papel':
    print(f'A escolha do jogador foi {escolha_jogador} e a escolha do computador foi {escolha_computador}, sendo assim o JOGADOR GANHOU!!')
elif escolha_computador=='Pedra' and escolha_jogador=='Tesoura' or escolha_computador=='Papel' and escolha_jogador=='Pedra' or escolha_computador=='Tesoura' and escolha_computador=='Papel':
    print(f'A escolha do jogador foi {escolha_jogador} e a escolha do computador foi {escolha_computador}, sendo assim o COMPUTADOR GANHOU!')
print('Obrigado por jogar nosso jogo!')


'''
Crie um programa que faça o computador jogar jokenpô com você.
'''