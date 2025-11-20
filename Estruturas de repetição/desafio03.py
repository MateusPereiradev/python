soma=0
for multiplos in range(1,501):
    if multiplos%3==0 and multiplos%2!=0:
        soma+=multiplos
        print(multiplos)
print(soma)
print('Fim do programa')

'''Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram
no intervalo de 1 até 500'''