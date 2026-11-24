from time import sleep
from utils.senha import input_senha
from controllers.usuario_controller import UsuarioController

usuario_controller = UsuarioController()


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
            nova_senha = input_senha("Digite a nova senha: ")
            sucesso, mensagem = usuario_controller.editar_usuario(usuario['id'], novo_nome, novo_email, nova_senha)
            print(mensagem)
            if sucesso:
                usuario = usuario_controller.buscar_por_id(usuario['id'])
            return usuario
        elif alterar.lower() == "n":
            return usuario
        else:
            print("Opção inválida. Tente novamente.")
            sleep(0.5)

def excluir_conta(usuario):
    while True:
        excluir = input("\nDeseja excluir a conta mesmo? (s/n): ")
        if excluir.lower() == "s":
            sucesso, mensagem = usuario_controller.excluir_conta(usuario['id'])
            print(mensagem)
            return sucesso
        elif excluir.lower() == "n":
            return False
        else:
            print("Opção inválida. Tente novamente.")
            sleep(0.5)