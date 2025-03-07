'''10.Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer no plano, P1(x1,y1) e 
P2(x2,y2), calcule e escreva na tela a distância “d” entre eles. A fórmula que efetua tal cálculo é:
d=√( ( x2 - x1 ) 2 + ( y2 - y1) 2 )'''

import math

print('\nInforme as coordenadas x1, x2:')

x1 = int(input('X1: '))
x2 = int(input('X2: '))

print('\nInforme as coordenadas y1, y2:')

y1 = int(input('Y1: '))
y2 = int(input('Y2: '))

d = math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)
print(f'\n\n A distância entre eles é: {d}')