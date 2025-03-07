'''6. Solicite um número inteiro "n" representando uma temperatura em graus Celsius. Imprima na tela se nessa
temperatura a água se encontra em estado sólido (abaixo de zero), líquido (entre zero e 100) ou gasoso
(acima de 100);'''

n = float(input('Digite uma temperatura em graus Celsius(Sem o Cº): '))

if n < 0:
    print('A água está no estado sólido.')
elif n >= 0 and n < 100:
    print('A água está no estado líquido.')
elif n >= 100:
    print('A água está no estado gásoso.')