'''8. Faça um algoritmo que receba como entrada um horário inicial e um horário final, contendo horas, minutos e
segundos. Calcule o intervalo de tempo entre essas duas horas e apresente na tela no formato “hh:mm:ss”;'''

hInicial = int(input('Digite um valor em horas: '))
minInicial = int(input('Digite um valor em minutos: '))
segInicial = int(input('Digite um valor em segundos: '))
hFinal = int(input('Digite outro valor em horas: '))
minFinal = int(input('Digite outro valor em minutos: '))
segFinal = int(input('Digite outro valor em segundos: '))

vSeg1 = hInicial * 3600 + minInicial * 60 + segInicial
vSeg2 = hFinal * 3600 + minFinal * 60 + segFinal

Intervalo = vSeg1 - vSeg2

min = Intervalo // 60 
horas = Intervalo // 3600
seg = (Intervalo + Intervalo) / 2

i = 0
while Intervalo >= i:
    if seg >= 60:
        seg = seg - 60
        min = min + 1
    
    if min >= 60:
        min = min - 60
        horas = horas + 1

    i += 1

print(horas, ':', min, ':', seg)