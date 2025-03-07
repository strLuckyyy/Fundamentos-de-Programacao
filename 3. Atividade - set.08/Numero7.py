'''7. Solicite duas letras "a" e "b" e imprima na tela se a letra "a" é igual, antecessora ou sucessora da letra "b";'''

a = input('Digite uma letra: ')
b = input('Digite outra letra: ')

if a == b:
    print(a, 'é igual a ', b)
elif a < b:
    print(a, 'é antecessora a letra ', b)
elif a > b:
    print(a, 'é sucessora a letra ', b)