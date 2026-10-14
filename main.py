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

def tela_cadastro_organizacao(usuario):
    print("\n\n\033[44m ----- CADASTRO DE ORGANIZAÇÃO ----- \033[0m")
    print("Digite 0 para voltar ao menu")
    nome = input("Nome da organização: ")
    if nome == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return

    sucesso, mensagem = organizacoes_controller.cadastrar(nome, usuario['id'])
    print(mensagem)

def buscar_organizacao_por_palavra_chave():
    print("\n\n\033[44m ----- BUSCA POR NOME ----- \033[0m")
    palavra_chave = input("Digite o nome da organização: ")
    organizacoes = organizacoes_controller.buscar_por_palavra_chave(palavra_chave)
    if organizacoes:
        sleep(0.5)
        print("\nOrganizações encontradas:")
        for organizacao in organizacoes:
            print(f" - {organizacao['nome']}")
    else:
        print("Organização não encontrada.")


def tela_minhas_organizacoes(usuario):
    print("\n\n\033[44m ----- MINHAS ORGANIZAÇÕES ----- \033[0m")
    organizacoes = organizacoes_controller.listar_organizacoes_por_gestor(usuario['id'])

    if not organizacoes:
        print("Você não possui organizações cadastradas.")
        sleep(0.5)
        deseja_cadastrar = input("Deseja cadastrar uma organização? (s/n): ")
        if deseja_cadastrar.lower() == "s":
            sleep(0.5)
            tela_cadastro_organizacao(usuario)
        return
    
    for i, organizacao in enumerate(organizacoes, start=1):
        print(f"{i}- {organizacao['nome']}")
    editar = input("\nDeseja editar o nome da organização? (s/n): ")
    if editar.lower() == "s":
        sleep(0.5)
        org_numero = input("Digite o número da organização que deseja editar: ")
        if not org_numero.isdigit():
            print("Digite apenas o número.")
            return
        org_numero = int(org_numero) - 1
        if 0 <= org_numero < len(organizacoes):
            sleep(0.5)
            novo_nome = input("Digite o novo nome da organização: ")
            sucesso, mensagem = organizacoes_controller.atualizar(organizacoes[org_numero]['id'], novo_nome)
            print(mensagem)
        else:
            print("Organização inválida.")

    elif editar.lower() == "n":
        sleep(0.5)
        deseja_cadastrar = input("Deseja cadastrar outra organização? (s/n): ")
        if deseja_cadastrar.lower() == "s":
            sleep(0.5)
            tela_cadastro_organizacao(usuario)
        elif deseja_cadastrar.lower() == "n":
            sleep(0.5)
            excluir = input("Deseja excluir alguma organização? (s/n): ")
            if excluir.lower() == "s":
                org_numero = input("Digite o número da organização que deseja excluir: ")
                if not org_numero.isdigit():
                    print("Digite apenas o número.")
                    return
                org_numero = int(org_numero) - 1
                if 0 <= org_numero < len(organizacoes):
                    sucesso, mensagem = organizacoes_controller.excluir(organizacoes[org_numero]['id'])
                    print(mensagem)
                else:
                    print("Organização inválida.")
            return

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
    buscar = input("\nDeseja buscar uma organização? (s/n): ")
    if buscar.lower() == "s":
        buscar_organizacao_por_palavra_chave()

    input("Pressione Enter para voltar ao menu...")
    sleep(0.5)

def minha_conta(usuario):
    print("\n\n\033[44m ----- MINHA CONTA ----- \033[0m")
    print(f"Nome: {usuario['nome']}")
    print(f"Email: {usuario['email']}")
    print(f"Tipo: {usuario['tipo']}")

    while True:
        sleep(0.5)
        alterar = input("\nDeseja alterar os dados da conta? (s/n): ")
        if alterar.lower() == "s":
            novo_nome = input("Digite o novo nome: ")
            novo_email = input("Digite o novo email: ")
            nova_senha = input("Digite a nova senha: ")
            sucesso, mensagem = usuario_controller.editar_usuario(usuario['id'], novo_nome, novo_email, nova_senha)
            print(mensagem)
            if sucesso:
                usuario = usuario_controller.buscar_por_id(usuario['id'])
            return usuario
        elif alterar.lower() == "n":
            return usuario
        else:
            print("Opção inválida. Tente novamente.")

def excluir_conta(usuario):
    while True:
        excluir = input("Deseja excluir a conta? (s/n): ")
        if excluir.lower() == "s":
            sucesso, mensagem = usuario_controller.excluir_conta(usuario['id'])
            print(mensagem)
            return sucesso
        elif excluir.lower() == "n":
            return False
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\n\n\033[46m ===== TRILHA ===== \033[0m")
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
        print("3 - Excluir conta")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sleep(0.5)
            tela_organizacoes()

        elif opcao == "2":
            sleep(0.5)
            usuario =minha_conta(usuario)

        elif opcao == "3":
            sleep(0.5)
            if excluir_conta(usuario):
                break

        elif opcao == "4":
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
        print("4 - Excluir conta")
        print("5 - Sair")
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
            usuario = minha_conta(usuario)
            sleep(0.5)

        elif opcao == "4":
            sleep(0.5)
            if excluir_conta(usuario):
                break
            sleep(0.5)

        elif opcao == "5":
            print("Saindo...")
            sleep(0.5)
            break

        else:
            print("Opção inválida. Tente novamente.")
            sleep(0.5)

if __name__ == "__main__":
    criar_tabelas()
    menu_principal()
