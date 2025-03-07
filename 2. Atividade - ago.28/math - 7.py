
print("7. Desenvolva um programa que solicite ao usuário a altura e a largura de um retângulo e exiba o"
" perímetro e a área deste retângulo na tela")

print("----")
aRetangulo = float(input("Qual a altura do retângulo? "))
lRetangulo = float(input("Qual a largura do retângulo? "))

pRetangulo = aRetangulo + lRetangulo
aRetangulo = aRetangulo * lRetangulo

print("O perímetro e a área desse retângulo é, respectivamente: ", pRetangulo, ", ", aRetangulo)
