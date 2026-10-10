from database.criar_banco import criar_tabelas
from controllers.usuario_controller import UsuarioController
from controllers.organizacoes_controller import OrganizacoesController
from time import sleep

usuario_controller = UsuarioController()
organizacoes_controller = OrganizacoesController()


def tela_cadastro():
    print("\n\n\033[44m ----- CADASTRO ----- \033[0m")
    print("Digite 0 para voltar ao menu")
    nome = input("Nome: ")
    if nome == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return
    email = input("Email: ")
    senha = input("Senha: ")

    while True:
        tipo_opcao = input("Tipo (1 - Membro, 2 - Gestor): ")
        if tipo_opcao in ("1", "2"):
            break
        sleep(0.5)
        print("Opção inválida. Tente novamente.")
    if tipo_opcao == "1":
        tipo = "membro"
    else:
        tipo = "gestor"

    sucesso, mensagem = usuario_controller.cadastrar(nome, email, senha, tipo)
    print(mensagem)

def tela_login(menu_principal, menu_membro, menu_gestor):
    print("\n\n\033[44m ----- LOGIN ----- \033[0m")
    print("Digite 0 para voltar ao menu")
    email = input("Email: ")
    if email == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return
    senha = input("Senha: ")

    sucesso, mensagem, usuario = usuario_controller.login(email, senha)
    print(mensagem)
    if sucesso:
        sleep(0.5)
        print(f"Bem vindo! Tipo de conta: {usuario['tipo']}")
        if usuario['tipo'] == "membro":
            menu_membro(usuario)
        else:
            menu_gestor(usuario)
        return

def tela_cadastro_organizacao(usuario, gestor_id):
    print("\n\n\033[44m ----- CADASTRO DE ORGANIZAÇÃO ----- \033[0m")
    print("Digite 0 para voltar ao menu")
    nome = input("Nome da organização: ")
    if nome == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return

    sucesso, mensagem = organizacoes_controller.cadastrar(nome, gestor_id)
    print(mensagem)

def buscar_organizacao_por_nome():
    print("\n\n\033[44m ----- BUSCA POR NOME ----- \033[0m")
    nome = input("Digite o nome da organização: ")
    organizacao = organizacoes_controller.buscar_por_nome(nome)
    if organizacao:
        print(f"Organização encontrada: {organizacao['nome']}")
    else:
        print("Organização não encontrada.")


def tela_minhas_organizacoes(usuario):
    print("\n\n\033[44m ----- MINHAS ORGANIZAÇÕES ----- \033[0m")
    organizacoes = organizacoes_controller.listar_organizacoes_por_gestor(usuario['id'])

    if not organizacoes:
        print("Você não possui organizações cadastradas.")
        deseja_cadastrar = input("Deseja cadastrar uma organização? (s/n): ")
        if deseja_cadastrar.lower() == "s":
            tela_cadastro_organizacao(usuario, gestor_id=usuario['id'])
        return
    
    for i, organizacao in enumerate(organizacoes, start=1):
        print(f"{i}- {organizacao['nome']}")
    editar = input("Deseja editar o nome da organização? (s/n): ")
    if editar.lower() == "s":
        org_numero = int(input("Digite o número da organização que deseja editar: ")) - 1
        if 0 <= org_numero < len(organizacoes):
            novo_nome = input("Digite o novo nome da organização: ")
            sucesso, mensagem = organizacoes_controller.atualizar(organizacoes[org_numero]['id'], novo_nome)
            print(mensagem)
        else:
            print("Organização inválida.")

    input("Pressione Enter para voltar ao menu...")
    sleep(0.5)

def tela_organizacoes():
    print("\n\n\033[44m ----- ORGANIZAÇÕES ----- \033[0m")
    organizacoes = organizacoes_controller.listar_organizacoes()

    if not organizacoes:
        print("Nenhuma organização cadastrada.")
        return
    
    for i, organizacao in enumerate(organizacoes, start=1):
        print(f"{i}- {organizacao['nome']}")
    buscar = input("\nDeseja buscar uma organização por nome? (s/n): ")
    if buscar.lower() == "s":
        buscar_organizacao_por_nome()

    input("Pressione Enter para voltar ao menu...")
    sleep(0.5)

def minha_conta(usuario):
    print("\n\n\033[44m ----- MINHA CONTA ----- \033[0m")
    print(f"Nome: {usuario['nome']}")
    print(f"Email: {usuario['email']}")
    print(f"Tipo: {usuario['tipo']}")

    input("Pressione Enter para voltar ao menu...")
    sleep(0.5)

def alterar_senha(usuario):
    print("\n\n\033[44m ----- ALTERAR SENHA ----- \033[0m")
    while True:
        alterar = input("Deseja alterar a senha? (s/n): ")
        if alterar.lower() == "s":
            nova_senha = input("Digite a nova senha: ")
            sucesso, mensagem = usuario_controller.alterar_senha(usuario['id'], nova_senha)
            print(mensagem)
            break
        elif alterar.lower() == "n":
            break
        else:
            print("Opção inválida. Tente novamente.")

def excluir_conta(usuario):
    while True:
        excluir = input("Deseja excluir a conta? (s/n): ")
        if excluir.lower() == "s":
            sucesso, mensagem = usuario_controller.excluir_conta(usuario['id'])
            print(mensagem)
            break
        elif excluir.lower() == "n":
            return
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\n\n\033[44m ===== TRILHA ===== \033[0m")
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sleep(0.5)
            tela_login(menu_principal, menu_membro, menu_gestor)

        elif opcao == "2":
            sleep(0.5)
            tela_cadastro()

        elif opcao == "3":
            print("Saindo...")
            sleep(0.5)
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_membro(usuario):
    while True:
        print("\n\n\033[44m ===== MENU MEMBRO ===== \033[0m")
        print("1 - Ver organizações")
        print("2 - Minha conta")
        print("3 - Alterar senha")
        print("4 - Excluir conta")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sleep(0.5)
            tela_organizacoes()

        elif opcao == "2":
            sleep(0.5)
            minha_conta(usuario)

        elif opcao == "3":
            sleep(0.5)
            alterar_senha(usuario)

        elif opcao == "4":
            sleep(0.5)
            excluir_conta(usuario)
            break

        elif opcao == "5":
            print("Saindo...")
            sleep(0.5)
            break

        else:
            print("Opção inválida. Tente novamente.")
            sleep(0.5)

def menu_gestor(usuario):
    while True:
        print("\n\n\033[44m ===== MENU GESTOR ===== \033[0m")
        print("1 - Ver organizações")
        print("2 - Minhas organizações")
        print("3 - Minha conta")
        print("4 - Alterar senha")
        print("5 - Excluir conta")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sleep(0.5)
            tela_organizacoes()
            sleep(0.5)

        elif opcao == "2":
            sleep(0.5)
            tela_minhas_organizacoes(usuario)
            sleep(0.5)

        elif opcao == "3":
            sleep(0.5)
            minha_conta(usuario)
            sleep(0.5)

        elif opcao == "4":
            sleep(0.5)
            alterar_senha(usuario)
            sleep(0.5)

        elif opcao == "5":
            sleep(0.5)
            excluir_conta(usuario)
            sleep(0.5)
            break

        elif opcao == "6":
            print("Saindo...")
            sleep(0.5)
            break

        else:
            print("Opção inválida. Tente novamente.")
            sleep(0.5)

if __name__ == "__main__":
    criar_tabelas()
    menu_principal()
