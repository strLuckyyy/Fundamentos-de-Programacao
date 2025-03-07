'''1. Modifique o primeiro exemplo da página anterior para identificar corretamente letras maiúsculas,
minúsculas, números e símbolos;
'''

x = input('Informe um caractere: ')

if x >= '0' and x <= '9':
    print('É um número')

elif x >= 'a' and x <= 'z':
    print('Letra minúscula')

elif x >= 'A' and x <= 'Z':
    print('Letra maiúscula')

else:
    print('É um simbolo')

