reta_1= float(input('Digite aqui o comprimento da primeira reta:'))
reta_2= float(input('Digite aqui o comprimeiro da segunda reta:'))
reta_3= float(input('Digite aqui o comprimeiro da terceira reta:'))
if reta_1+reta_2>reta_3 and reta_2+reta_3>reta_1 and reta_1+reta_3>reta_1:
    print('As retas formam um triângulo!')
    if reta_1==reta_2==reta_3:
        print('Referente as retas informadas, as mesmas formam um triângulo Equilátero!')
    elif reta_1!=reta_2!=reta_3!=reta_1:
        print('Referente as reta informadas, as mesmas formam um triângulo Escaleno!')
    else:
        print('Referente as reta informadas, as mesmas formam um triângulo Isósceles!')
print('Fim do programa de triângulos!')

'''
Refaça o Desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:todos os lados são iguais
Isósceles: dois lados iguais
Escaleno:Todos os lados diferentes
'''