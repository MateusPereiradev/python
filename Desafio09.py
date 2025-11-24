from time import sleep
reta_1= float(input('Digite aqui o comprimeiro da primeira reta:'))
reta_2= float(input('Digite aqui o comprimento da segunda reta:'))
reta_3= float(input('Digite aqui o comprimento da terceira reta:'))
print('Calculando medidas...')
sleep(3)
if reta_1+reta_2>reta_3 and reta_2+reta_3>reta_1 and reta_1+reta_3>reta_2:
    print(f'As medidas de {reta_1}, {reta_2} e {reta_3} formam um triângulo')
    if reta_1==reta_2==reta_3:
        print('As medidas formam um triângulo Equilátero')
    elif reta_1!=reta_2!=reta_3!=reta_1:
        print('As medidas formam um triângulo Escaleno')
    else:
<<<<<<< HEAD
        print(f'Referente as medidas informadas, as retas {r1}, {r2} e {r3} formam um triângulo ISÓSCELES!')
print('Fim do código')
=======
        print('As medidas formam um triângulo Isósceles')
print('Tenha uma boa noite!')

>>>>>>> 4ec890497deb2e817b786e779d65e2bcb0d7ead3

'''
Refaça o Desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:todos os lados são iguais
Isósceles: dois lados iguais
Escaleno:Todos os lados diferentes
'''