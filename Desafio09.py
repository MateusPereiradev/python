from time import sleep

r1= float(input('Digite aqui a medida da primeira reta:'))
r2= float(input('Digite aqui a medida da segunda reta:'))
r3= float(input('Digite aqui a medida da terceira reta:'))
print('Calculando medidas...')
sleep(3)
if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    print(f'Referente as medidas informadas, as retas {r1}, {r2} e {r3} formam um triângulo!')
    if r1==r2==r3:
        print(f'Referente as medidas informadas, as retas {r1}, {r2} e {r3} formam um triâgulo do tipo EQUILÁTERO!')
    elif r1!=r2!=r3!=r1:
        print(f'Referente as medidas informadas, as retas {r1}, {r2} e {r3} formam um triângulo do tipo ESCALENO!')
    else:
        print(f'Referente as medidas informadas, as retas {r1}, {r2} e {r3} formam um triângulo ISÓSCELES!')
print('Fim do código')
'''
Refaça o Desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:todos os lados são iguais
Isósceles: dois lados iguais
Escaleno:Todos os lados diferentes
'''