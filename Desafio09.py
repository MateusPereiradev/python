reta_1= float(input('Digite aqui o comprimento da primeira reta:'))
reta_2= float(input('Digite aqui o comprimento da segunda reta:'))
reta_3= float(input('Digite aqui o comprimento da terceira reta:'))
if reta_1+reta_2>reta_3 and reta_2+reta_3>reta_1 and reta_3+reta_1>reta_2:
    print(f'Referente a retas {reta_1}, {reta_2} e {reta_3} as mesmas formam um triângulo!')
    if reta_1==reta_2==reta_3:
        print(f'Referente as retas informadas as mesmas formam um triângulo EQUILÁTERO!')
    elif reta_1!=reta_2!=reta_3!=reta_1:
        print(f'Referente as retas informadas as mesmas formam um triângulo ESCALENO!')
    else:
        print('Referente as retas informadas as mesmas formam um triângulo ISÓSCELES!')

'''
Refaça o Desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:todos os lados são iguais
Isósceles: dois lados iguais
Escaleno:Todos os lados diferentes
'''