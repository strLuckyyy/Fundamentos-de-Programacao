import os
import sisInterface

def cadastroUsuário():
    listLog = sisInterface.cadastro()
    login = listLog[0]
    senha = listLog[1]

    with open('login.txt', 'a') as loginfile:
        loginfile.write(f'{login}\n')

    with open('senha.txt', 'a') as senhafile:
        senhafile.write(f'{senha}\n')


def loginUsuario():
    while True:
        os.system('cls' if os.name == 'nt' else 'clean')
        senhaLogin = []

        listLog = sisInterface.login()
        nameLogin = listLog[0]
        senhaLogin.append(listLog[1])

        print(f'nameLogin {nameLogin}, senhaLogin {senhaLogin}')

        with open('login.txt', 'r') as loginfile:
            login = loginfile.readlines()
            
        print(f'lenLogin {len(login)}')
        print('arquivo aberto')

        if len(login) == 0: input('\nNão há usuários cadastrados.'); return

        for linha in range(len(login)):
            print(f'linha {linha}, login[linha] {login[linha]}')
            if nameLogin in login[linha]: 

                print(f'linha {linha}')

                with open('senha.txt', 'r') as senhafile:
                    senha = senhafile.readlines(linha)
                    print(senha)
    
                print(f'senha {senha}, senhaLogin {senhaLogin}')
                        
                if senha == senhaLogin:
                    input('logado?')
                    software()

                else: 
                    print('\nSenha incorreta.')
                    sisInterface.mensage(0)
                    break          
        
        print('\nUsuário não encontrado. Cadastre-se primeiro.')
        sisInterface.mensage(0)
        return


def software():
    os.system('cls' if os.name == 'nt' else 'clean')

    print('\nVocê logou com sucesso!')
    input('\nInfelizmente não há nada aqui. Aperte ENTER para sair...')
    sisInterface.mensage(2)