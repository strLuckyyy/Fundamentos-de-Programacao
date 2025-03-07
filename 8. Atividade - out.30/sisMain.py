'''
Criar um acesso de conta de usuário
    Deve conter:
        - Login
        - Senha
        - Cadastro
'''
import os
import sisDef, sisInterface

while True:
    os.system('cls' if os.name == 'nt' else 'clean')

    resposta = sisInterface.opcoes(['Login', 'Cadastro', 'Sair', 'Logs'])

    if resposta == '1':
        sisDef.loginUsuario()

    elif resposta == '2':
        sisDef.cadastroUsuário()

    elif resposta == '3':
        sisInterface.mensage(2)

    elif resposta == '4':
        with open('login.txt', 'r') as logfile:
            loginlist = logfile.readlines()
        
        with open('senha.txt', 'r') as senhafile:
            senhalist = senhafile.readlines()

        for i in range(len(loginlist)):
            print(f'{loginlist[i]} | {senhalist[i]}')
        
        input()

    else:
        sisInterface.mensage(1)