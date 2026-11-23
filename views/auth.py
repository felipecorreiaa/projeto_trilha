from time import sleep
from controllers.usuario_controller import UsuarioController

usuario_controller = UsuarioController()


def tela_cadastro():
    print("\n\n\033[44m ----- CADASTRO ----- \033[0m")
    print("Digite 0 para voltar ao menu")
    nome = input("Nome: ")
    if nome == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return
    email = input("Email: ")
    if email == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return
    senha = input("Senha: ")
    if senha == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return

    while True:
        tipo_opcao = input("Tipo (1 - Membro, 2 - Gestor): ")
        if tipo_opcao in ("1", "2", "0"):
            break
        sleep(0.5)
        print("Opção inválida. Tente novamente.\n")
        sleep(0.5)
    if tipo_opcao == "1":
        tipo = "membro"
    elif tipo_opcao == "2":
        tipo = "gestor"
    else:
        print("Voltando ao menu...")
        sleep(0.5)
        return

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
    if senha == "0":
        print("Voltando ao menu...")
        sleep(0.5)
        return
    sucesso, mensagem, usuario = usuario_controller.login(email, senha)

    print(mensagem)
    if sucesso:
        sleep(0.5)
        print(f"Bem vindo, {usuario['nome']}! Tipo de conta: {usuario['tipo']}")
        if usuario['tipo'] == "membro":
            menu_membro(usuario)
        else:
            menu_gestor(usuario)