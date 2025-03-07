'''
Fulano tem 1,50 metro e cresce 2 centímetros por ano, enquanto Beltrano tem 1,10 metro e cresce 3 centímetros por ano. 
Construa um algoritmo que calcule e imprima quantos anos serão necessários para que Beltrano seja maior que Fulano. 
Não utilize solução puramente matemática.
'''

fulanoAltura = 1.5
beltranoAltura = 1.1
i = 0

while beltranoAltura < fulanoAltura:
    print("\nFulano tem ", fulanoAltura, "M de altura", "\nBeltrano tem ", beltranoAltura, "M de altura\n")

    beltranoAltura += 0.03
    fulanoAltura += 0.02

    i += 1
    if beltranoAltura > fulanoAltura:
        print("\nSão necessários ", i, "anos para que o Beltrano seja maior que Fulano")