print('===== Analisador de Triângulos =====')
nome= str(input('Digite aqui o seu nome:')).strip()
r1= float(input('Digite aqui a primeira reta:'))
r2= float(input('Digite aqui a segunda reta:'))
r3= float(input('Digite aqui a terceira reta:'))
if r1+r2>r3 and r1+r3>r3 and r2+r3>r1:
    print(f'Referente as retas {r1}m {r2} e {r3}, é possível formar um triângulo!')
    if r1==r2==r3:
        print(f'Referente as retas {r1}, {r2} e {r3}, é possível formar um triângulo EQUILÁTERO!')
    elif r1!=r2!=r3!=r1:
        print(f'Referente as retas {r1}, {r2} e {r3}, é possível formar um triângulo ESCALENO!')
    else:
        print(f'Referente as retas {r1}, {r1} e {r3}, é possível formar um triângulo ISÓSCELES!')
print(f'Muito obrigado por utilizar o Analisador de Triângulos, {nome}! Volte Sempre!')

'''
Refaça o Desafio 035 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero:todos os lados são iguais
Isósceles: dois lados iguais
Escaleno:Todos os lados diferentes
'''