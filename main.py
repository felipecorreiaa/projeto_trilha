from database.criar_banco import criar_tabelas
from controllers.usuario_controller import UsuarioController
from controllers.organizacoes_controller import OrganizacoesController
from views.auth import tela_cadastro, tela_login
from views.conta import minha_conta, excluir_conta
from views.organizacoes import (
    buscar_organizacao_por_palavra_chave,
    tela_minhas_organizacoes,
    tela_organizacoes
    )
from time import sleep

usuario_controller = UsuarioController()
organizacoes_controller = OrganizacoesController()



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
        print("2 - Buscar organização por nome")
        print("3 - Minha conta")
        print("4 - Excluir conta")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sleep(0.5)
            tela_organizacoes()

        elif opcao == "2":
            sleep(0.5)
            buscar_organizacao_por_palavra_chave()

        elif opcao == "3":
            sleep(0.5)
            usuario = minha_conta(usuario)  

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

def menu_gestor(usuario):
    while True:
        print("\n\n\033[44m ===== MENU GESTOR ===== \033[0m")
        print("1 - Ver organizações")
        print("2 - Buscar organização por nome")
        print("3 - Minhas organizações")
        print("4 - Minha conta")
        print("5 - Excluir conta")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sleep(0.5)
            tela_organizacoes()
            sleep(0.5)

        elif opcao == "2":
            sleep(0.5)
            buscar_organizacao_por_palavra_chave()

        elif opcao == "3":
            sleep(0.5)
            tela_minhas_organizacoes(usuario)

        elif opcao == "4":
            sleep(0.5)
            usuario = minha_conta(usuario)

        elif opcao == "5":
            sleep(0.5)
            if excluir_conta(usuario):
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
