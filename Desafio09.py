from time import sleep
reta_1= float(input('Digite aqui o comprimento da reta:'))
reta_2= float(input('Digite aqui o comprimento da reta:'))
reta_3= float(input('Digite aqui o comprimento da reta:'))
print('Calculando as retas...')
sleep(3)
if reta_1+reta_2>reta_3 and reta_2+reta_3>reta_1 and reta_1+reta_3>reta_2:
    print(f'Referente as retas {reta_1}, {reta_2} e {reta_3}, as mesmas formam um triângulo')
    if reta_1==reta_2==reta_3:
        print(f'Referente as retas {reta_1}, {reta_2} e {reta_3} as mesmas formam um triângulo EQUILÁTERO!')
    elif reta_1!=reta_2!=reta_3!=reta_1:
        print(f'Referente as reta {reta_1}, {reta_2} e {reta_3} as mesmas formam um triângulo ESCALENO!')
    else:
        print(f'Referente as retas {reta_1}, {reta_2} e {reta_3} as mesmas formam um triângulo ISÓSCELES!')
print('Fim do programa')

'''
Refaça o Desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:todos os lados são iguais
Isósceles: dois lados iguais
Escaleno:Todos os lados diferentes
'''