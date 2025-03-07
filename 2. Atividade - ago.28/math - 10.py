import math

print("10.Desenvolva um programa que solicite dois números ao usuário. Estes números são os catetos de um"
" triângulo retângulo. Sendo assim, apresente ao usuário:")

print("----")

c1 = float(input("Digite um número que represente o cateto 1 de um triângulo retângulo: "))
c2 = float(input("Digite outro número para representar outro cateto: "))

print("------------------------------------")
print("___a) Hipotenusa")

h = math.sqrt(c1 ** 2 + c2 **2)
print("A Hipotenusa desse triângulo é: ", h)

print("------------------------------------")
print("___b)Perímetro")

print("O perímetro desse triângulo é: ", h + c1 + c2)

print("------------------------------------")
print("___c) Área")

print("A área desse triângulo é: ", (c1 * c2) / 2)

print("------------------------------------")
print("___d)Seno")

s = c1 / h
print("O seno do ângulo é: ", math.degrees(c1 / h))

print("------------------------------------")
print("___e)Cosseno")

print("O cosseno do ângulo é: ", math.degrees(c2 / h))

print("------------------------------------")
print("___f) Tangente")

print("A tangente do triângulo é: ", math.degrees(c1 / c2))