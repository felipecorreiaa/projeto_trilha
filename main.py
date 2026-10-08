from database.criar_banco import criar_tabelas
from controllers.usuario_controller import UsuarioController
from time import sleep

usuario_controller = UsuarioController()


def tela_cadastro():
    sleep(0.5)
    print('\n\n----- CADASTRO -----')
    print('Digite 0 para voltar ao menu')
    nome = input('Nome: ')
    if nome == '0':
        print('Voltando ao menu...')
        sleep(0.5)
        return
    email = input('Email: ')
    senha = input('Senha: ')

    while True:
        tipo_opcao = input('Tipo (1 - Membro, 2 - Gestor): ')
        if tipo_opcao in ('1', '2'):
            break
        sleep(0.5)
        print('Opção inválida. Tente novamente.')
    if tipo_opcao == '1':
        tipo = 'membro'
    else:
        tipo = 'gestor'

    sucesso, mensagem = usuario_controller.cadastrar(nome, email, senha, tipo)
    print(mensagem)

def tela_login():
    print('\n\n ----- LOGIN -----')
    print('Digite 0 para voltar ao menu')
    email = input('Email: ')
    if email == '0':
        print('Voltando ao menu...')
        sleep(0.5)
        return
    senha = input('Senha: ')

    sucesso, mensagem, usuario = usuario_controller.login(email, senha)
    print(mensagem)
    if sucesso:
        sleep(0.5)
        print(f'Bem vindo! Tipo de conta: {usuario['tipo']}')


def menu_principal():
    while True:
        print('\n\n ===== TRILHA =====')
        print('1 - Login')
        print('2 - Cadastro')
        print('3 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            tela_login()

        elif opcao == '2':
            tela_cadastro()

        elif opcao == '3':
            print('Saindo...')
            sleep(0.5)
            break

        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    criar_tabelas()
    menu_principal()