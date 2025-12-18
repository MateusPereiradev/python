reta_1= float(input('Digite o comprimento da primeira reta:'))
reta_2= float(input('Digite o comprimento da segunda reta:'))
reta_3= float(input('Digite o comprimento da terceira reta:'))
if reta_1+reta_2>reta_3 and reta_1+reta_3>reta_2 and reta_2+reta_3>reta_1:
    print('As retas formam um triângulo!')
    if reta_1==reta_2==reta_3:
        print('O triângulo formado é do tipo EQUILÁTERO!')
    elif reta_1!=reta_2!=reta_3!=reta_1:
        print('O triângulo formado é do tipo ESCALENO!')
    else:
        print('O triângulo formado é do tipo ISÓSCELES!')
print('Fim do programa de verificação de triângulos!')


'''
Refaça o Desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:todos os lados são iguais
Isósceles: dois lados iguais
Escaleno:Todos os lados diferentes
'''