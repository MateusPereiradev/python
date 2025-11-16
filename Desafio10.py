from random import choice
from time import sleep
from emoji importe emojize
nome= str(input('Digite aqui seu nome:')).strip().capitalize()
print('======Jokenpô======')
print('''Escolha sua jogada:
      [1] Pedra
      [2] Papel
      [3] Tesoura''')
jogador= str(input('Digite aqui sua jogada de Pedra, Papel ou Tesoura:')).strip().capitalize()
itens=['Pedra', 'Papel', 'Tesoura']
computador= choice(itens)
if jogador=='Pedra' and computador=='Pedra' or jogador=='Papel' and computador=='Papel' or jogador=='Tesoura' and computador=='Tesoura':
    print(f'O jogador escolheu {jogador} e o computador escolheu {computador}, sendo assim deu EMPATE!')
elif jogador=='Pedra' and computador=='Tesoura' or jogador=='Papel' and computador=='Pedra' or jogador=='Tesoura' and computador=='Papel':
    print(f'O jogador escolheu {jogador} e o computador escolheu {computador}, sendo assim o JOGADOR VENCEU!')
elif computador=='Pedra' and jogador=='Tesoura' or computador=='Papel' and jogador=='Pedra' or computador=='Tesoura' and jogador=='Papel':
    print(f'O jogador escolheu {jogador} e o comptuador escolheu {computador}, sendo assim o COMPUTADOR VENCEU!')
print(f'Obigado por jogar nosso jogo {nome}')





'''
Crie um programa que faça o computador jogar jokenpô com você.
'''