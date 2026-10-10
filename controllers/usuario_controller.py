from repositories.usuario_repository import UsuarioRepository

class UsuarioController:
    def __init__(self):
        self.repository = UsuarioRepository()

    def cadastrar(self, nome, email, senha, tipo):
        if '@' not in email or '.' not in email:
            return False, 'Email inválido.'
        if len(senha) < 6:
            return False, "A senha precisa ter pelo menos 6 caracteres."
        if any(c.isupper() for c in senha) == False:
            return False, "A senha precisa ter pelo menos uma letra maiúscula."
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

    def editar_usuario(self, usuario_id, nome, email, senha, tipo):
        usuario = self.repository.buscar_por_id(usuario_id)
        if not usuario:
            return False, "Usuário não encontrado."
        if '@' not in email or '.' not in email:
            return False, 'Email inválido.'
        if len(senha) < 6:
            return False, "A senha precisa ter pelo menos 6 caracteres."
        if any(c.isupper() for c in senha) == False:
            return False, "A senha precisa ter pelo menos uma letra maiúscula."
        self.repository.atualizar(usuario_id, nome, email, senha, tipo)
        return True, "Usuário atualizado com sucesso."

    def alterar_senha(self, usuario_id, nova_senha):
        usuario = self.repository.buscar_por_id(usuario_id)
        if not usuario:
            return False, "Usuário não encontrado."
        if len(nova_senha) < 6:
            return False, "A senha precisa ter pelo menos 6 caracteres."
        if any(c.isupper() for c in nova_senha) == False:
            return False, "A senha precisa ter pelo menos uma letra maiúscula."
        self.repository.atualizar_senha(usuario_id, nova_senha)
        return True, "Senha atualizada com sucesso."

    def excluir_conta(self, usuario_id):
        usuario = self.repository.buscar_por_id(usuario_id)
        if not usuario:
            return False, "Usuário não encontrado."
        self.repository.deletar(usuario_id)
        return True, "Conta excluída com sucesso."
