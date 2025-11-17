from random import choice
from time import sleep
print('===== JOKENPÔ =====')
print('''Escolha sua jogada:
      Pedra
      Papel
      Tesoura''')
jogador= str(input('Qual é a sua jogada?')).strip().capitalize()
itens= ['Pedra','Papel', 'Tesoura' ]
computador= choice(itens)
print('Calculando jogada...')
sleep(3)
if computador==jogador:
    print(f'A escolha do jogador foi {jogador} e a escolha do computador foi {computador}, sendo assim houve um EMPATE!')
elif computador=='Pedra' and jogador== 'Tesoura' or computador== 'Papel' and jogador== 'Pedra' or computador=='Tesoura' and jogador=='Papel':
    print(f'Referente a jogada do computador {computador} e a do jogador {jogador}, o computador VENCEU!')
elif jogador== 'Pedra' and computador=='Tesoura' or jogador=='Papel' and computador=='Pedra' or jogador== 'Tesoura' and computador=='Papel':
    print(f'Referente a jogada do computador {computador}, e a jogada do jogador {jogador}, o jogador VENCEU!')
else:
    print('Jogada inválida! Tente novamente.')
print('Obrigado por jogar nosso jogo JOKENPÔ!')

'''
Crie um programa que faça o computador jogar jokenpô com você.
'''