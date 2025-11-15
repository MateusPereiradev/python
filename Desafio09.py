reta_1= float(input('Digite aqui o comprimento da primeira reta:'))
reta_2= float(input('Digite aqui o comprimento da segunda reta:'))
reta_3= float(input('Digite aqui o comprimento da terceira reta:'))
if reta_1+reta_2>reta_3 and reta_3+reta_1>reta_2 and reta_2+reta_3>reta_1:
    print('As medidas acima formam um triângulo!')
    if reta_1==reta_2==reta_3:
        print('As reta são iguais e formam um triângulo Equilátero!')
    if reta_1!=reta_2!=reta_3!=reta_1:
        print('Todos os lados são diferentes, formando um triângulo Escaleno!')
    else:
        print('As medidas formam um triângulo Isósceles, pois dois lados são iguais!')
print('Tenha um bom dia!')




'''
Refaça o Desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:todos os lados são iguais
Isósceles: dois lados iguais
Escaleno:Todos os lados diferentes
'''