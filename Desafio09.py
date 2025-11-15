r1= float(input('Digite aqui o comprimento da primeira reta:'))
r2= float(input('Digite aqui o comprimento da segunda reta:'))
r3= float(input('Digite aqui o comprimento da terceira reta:'))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('As retas podem formar um triângulo')
    if r1==r2==r3:
        print('Equilátero: todos os lados são iguais')
    elif r1!=r2!=r3!=r1:
        print('Escaleno: todos os lados são diferentes')
    else:
        print('Isósceles: dois lados são iguais')
print('Fim do programa')
'''
Refaça o Desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:todos os lados são iguais4
Isósceles: dois lados iguais
Escaleno:Todos os lados diferentes
'''