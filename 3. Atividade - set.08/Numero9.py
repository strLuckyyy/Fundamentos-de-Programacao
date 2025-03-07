'''9. Utilizando a equação do MRU (distância = velocidade * tempo), desenvolva um programa que solicite os 3
dados, mas receba apenas 2 e calcule o terceiro. Os dados devem ser números fracionários, e o dado a ser
calculado deve ser informado como vazio, apenas pressionando ENTER.'''


x = input('Digite a velocidade: ')
y = input('Digite o tempo: ')
z = input('Digite a distância: ')


if x == '':
    z = float(z)
    y = float(y)

    calculoX = float(z / y)
    print('A velocidade é: ', calculoX)

if y == '':
    z = float(z)
    y = float(x)

    calculoY = float(x / z)
    print('O tempo é: ', calculoY)

if z == '':
    z = float(x)
    y = float(y)

    calculoZ = float(x * y)
    print('A distância é: ', calculoZ)
