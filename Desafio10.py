from random import choice
from time import sleep
nome= str(input('Digite aqui seu nome:')).strip().capitalize()
print('====== JOKENPô ======')
print('''Escolha aqui sua jogada:
      Pedra
      Papel
      Tesoura''')
jogador= str(input('Escolha entre Pedra, Papel ou Tesoura:')).strip().capitalize()
itens= ['Pedra', 'Papel', 'Tesoura']
computador= choice(itens)
print('Calculando jogada do computador e do jogador...')
sleep(3)
if jogador==computador:
    print(f'Referente a sua jogada {jogador} e a do computador {computador} deu EMPATE!')
elif jogador=='Pedra' and computador=='Tesoura' or jogador=='Papel' and computador=='Pedra' or jogador=='Tesoura' and computador=='Papel':
    print(f'Referete a jogada do jogador {jogador} e a do computador {computador} o jogador VENCEU!')
elif computador=='Pedra' and jogador=='Tesoura'or computador=='Papel' and jogador=='Pedra' or computador=='Tesoura' and jogador=='Papel':
    print(f'Referente a jogada do jogador {jogador} e a do computador {computador} o computador VENCEU!')
print(f'Muito obrigado por jogar JOKENPÔ! Volte Sempre {nome}!')


'''
Crie um programa que faça o computador jogar jokenpô com você.
'''