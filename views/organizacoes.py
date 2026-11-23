from time import sleep
from controllers.usuario_controller import UsuarioController
from controllers.organizacoes_controller import OrganizacoesController

usuario_controller = UsuarioController()
organizacoes_controller = OrganizacoesController()


def tela_cadastro_organizacao(usuario):
    sleep(0.5)
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
    sleep(0.5)
    input("\nPressione Enter para voltar ao menu...")

def tela_minhas_organizacoes(usuario):
    sleep(0.5)
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
            print("\nDigite apenas o número.\n")
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
                    print("\nDigite apenas o número.\n")
                    return
                org_numero = int(org_numero) - 1
                if 0 <= org_numero < len(organizacoes):
                    sucesso, mensagem = organizacoes_controller.excluir(organizacoes[org_numero]['id'])
                    print(mensagem)
                else:
                    print("Organização inválida.")
            return

    input("\nPressione Enter para voltar ao menu...")
    sleep(0.5)

def entrar_organizacao(organizacao):
    gestor = usuario_controller.buscar_por_id(organizacao['gestor_id'])
    if not gestor:
        nome_gestor = "Gestor não encontrado"
    else:
        nome_gestor = gestor['nome']
    sleep(0.5)
    print(f"\n\n\033[44m ----- {organizacao['nome']} ----- \033[0m")
    print(f"Gestor: {nome_gestor}")
    print("Atividades ainda vão ser adicionadas...")
    return

def tela_organizacoes():
    print("\n\n\033[44m ----- ORGANIZAÇÕES ----- \033[0m")
    organizacoes = organizacoes_controller.listar_organizacoes()

    if not organizacoes:
        print("Nenhuma organização cadastrada.")
        return
    
    for i, organizacao in enumerate(organizacoes, start=1):
        print(f"{i}- {organizacao['nome']}")
    entrar = input("\nDeseja visualizar alguma organização? (s/n): ")
    if entrar.lower() == "s":
        sleep(0.5)
        org_numero = input("Digite o número da organização que deseja visualizar: ")
        if not org_numero.isdigit():
            print("\nDigite apenas o número.\n")
            return
        org_numero = int(org_numero) - 1
        if 0 <= org_numero < len(organizacoes):
            entrar_organizacao(organizacoes[org_numero])
        else:
            print("Organização inválida.")
    else:
        return

    input("\nPressione Enter para voltar ao menu...")
    sleep(0.5)