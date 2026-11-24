from time import sleep
from datetime import datetime
from controllers.usuario_controller import UsuarioController
from controllers.organizacoes_controller import OrganizacoesController
from controllers.atividades_controller import AtividadesController
from controllers.inscricao_controller import InscricaoController


atividades_controller = AtividadesController()
inscricao_controller = InscricaoController()
usuario_controller = UsuarioController()
organizacoes_controller = OrganizacoesController()


def formatar_dia(dia_iso):
    return datetime.strptime(dia_iso, "%Y-%m-%d").strftime("%d/%m/%Y")

def mostrar_atividades(atividades):
    if not atividades:
        print("Nenhuma atividade cadastrada.")
        return
    for i, a in enumerate(atividades, start=1):
        print(f"{i} - {formatar_dia(a['dia'])} | {a['horario']} | {a['nome']}")
        print(f"    {a['descricao']}")
        if a['link_inscricao']:
            print(f"    Link: {a['link_inscricao']}")

def escolher_atividade(atividades, acao):
    """Pede um número e devolve a atividade escolhida, ou None se inválido"""
    numero = input(f"Digite o número da atividade que deseja {acao}: ")
    if not numero.isdigit():
        print("\nDigite apenas o número.")
        return None
    numero = int(numero) - 1
    if 0 <= numero < len(atividades):
        return atividades[numero]
    print("Atividade inválida.")
    return None

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

def tela_adicionar_atividade(organizacao, usuario):
    sleep(0.5)
    print("\n\n\033[44m ----- ADICIONAR ATIVIDADE ----- \033[0m")
    print("\nDigite 0 para voltar ao menu")
    nome = input("Nome da atividade: ")
    if nome == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return
    dia = input("Dia (dd/mm/aaaa): ")
    if dia == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return
    horario = input("Horário (HH:MM): ")
    if horario == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return
    descricao = input("Descrição: ")
    if descricao == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return
    link = input("Link de inscrição (opcional, Enter para pular): ")
    if link == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return

    sucesso, mensagem = atividades_controller.cadastrar(
        organizacao['id'], usuario['id'], nome, dia, horario, descricao, link
    )
    print(mensagem)

def tela_editar_atividade(atividades, usuario):
    atividade = escolher_atividade(atividades, "editar")
    if not atividade:
        return

    print("Deixe em branco para manter.")
    dia_atual = formatar_dia(atividade['dia'])
    link_atual = atividade['link_inscricao'] or ""

    nome = input(f"Nome [{atividade['nome']}]: ") or atividade['nome']
    dia = input(f"Dia [{dia_atual}]: ") or dia_atual
    horario = input(f"Horário [{atividade['horario']}]: ") or atividade['horario']
    descricao = input(f"Descrição [{atividade['descricao']}]: ") or atividade['descricao']
    link = input(f"Link [{link_atual}]: ") or link_atual

    sucesso, mensagem = atividades_controller.atualizar(
        atividade['id'], usuario['id'], nome, dia, horario, descricao, link
    )
    print(mensagem)

def tela_excluir_atividade(atividades, usuario):
    atividade = escolher_atividade(atividades, "excluir")
    if not atividade:
        return

    confirmar = input(f"Deseja excluir '{atividade['nome']}' mesmo? (s/n): ")
    if confirmar.lower() == "s":
        sucesso, mensagem = atividades_controller.excluir(atividade['id'], usuario['id'])
        print(mensagem)
    else:
        print("Atividade não foi excluída.")

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

def entrar_organizacao(organizacao, usuario):
    gestor = usuario_controller.buscar_por_id(organizacao['gestor_id'])
    if not gestor:
        nome_gestor = "Gestor não encontrado"
    else:
        nome_gestor = gestor['nome']
    dono = organizacao['gestor_id'] == usuario['id']
    
    sleep(0.5)
    print(f"\n\n\033[44m ----- {organizacao['nome']} ----- \033[0m")
    print(f"Gestor: {nome_gestor}")

    while True:
        atividades = atividades_controller.listar_por_organizacao(organizacao['id'])
        print("\n\033[44m ----- ATIVIDADES ----- \033[0m")
        mostrar_atividades(atividades)

        if dono:
            print("\n[1] - Adicionar atividade\n[2] - Editar atividade\n[3] - Excluir atividade\n[4] - Voltar")
        else:
            print("\n[1] - Inscrever-se\n[2] - Cancelar inscrição\n[3] - Voltar")
        opcao = input("Escolha uma opção: ")

        if dono and opcao == "1":
            tela_adicionar_atividade(organizacao, usuario)
        elif dono and opcao == "2":
            tela_editar_atividade(atividades, usuario)
        elif dono and opcao == "3":
            tela_excluir_atividade(atividades, usuario)
        elif not dono and opcao == "1":
            atividade = escolher_atividade(atividades, "se inscrever")
            if atividade:
                print(inscricao_controller.inscrever(atividade['id'], usuario['id'])[1])
        elif not dono and opcao == "2":
            atividade = escolher_atividade(atividades, "cancelar")
            if atividade:
                print(inscricao_controller.cancelar(atividade['id'], usuario['id'])[1])
        elif dono and opcao == "4" or not dono and opcao == "3":
            return
        else:
            print("Opção inválida. Tente novamente\n")
            


def tela_organizacoes(usuario):
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
            entrar_organizacao(organizacoes[org_numero], usuario)
        else:
            print("Organização inválida.")
    else:
        return

    input("\nPressione Enter para voltar ao menu...")
    sleep(0.5)