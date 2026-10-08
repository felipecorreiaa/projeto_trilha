from repositories.usuario_repository import UsuarioRepository

class UsuarioController:
    def __init__(self):
        self.repository = UsuarioRepository()

    def cadastrar(self, nome, email, senha, tipo):
        if '@' not in email or '.' not in email:
            return False, 'Email inválido.'
        if len(senha) < 6:
            return False, "Senha inválida."
        if self.repository.buscar_por_email(email):
            return False, "Email já cadastrado."

        self.repository.inserir(nome, email, senha, tipo)
        return True, "Cadastro realizado com sucesso."

    def login(self, email, senha):
        usuario = self.repository.buscar_por_email(email)
        if not usuario:
            return False, "Usuário não encontrado.", None
        if not senha:
            return False, "Senha incorreta.", None
        return True, "Login realizado.", usuario
