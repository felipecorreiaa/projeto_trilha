from repositories.usuario_repository import UsuarioRepository

class UsuarioController:
    def __init__(self):
        self.repository = UsuarioRepository()

    def cadastrar(self, nome, email, senha, tipo):
        if '@' not in email or '.' not in email:
            return False, 'Email inválido. Tente novamente.'
        if len(senha) < 6:
            return False, "A senha precisa ter pelo menos 6 caracteres. Tente novamente."
        if any(c.isupper() for c in senha) == False:
            return False, "A senha precisa ter pelo menos uma letra maiúscula. Tente novamente."
        if self.repository.buscar_por_email(email):
            return False, "Email já cadastrado. Tente usar outro."
        if not nome.strip() or not email.strip() or not senha.strip() or not tipo.strip():
            return False, "Preencha todos os campos."

        self.repository.inserir(nome, email, senha, tipo)
        return True, "Cadastro realizado com sucesso."

    def login(self, email, senha):
        usuario = self.repository.buscar_por_email(email)
        if not usuario:
            return False, "Usuário não encontrado.", None
        if senha != usuario['senha']:
            return False, "Senha incorreta.", None
        return True, "Login realizado.", usuario

    def editar_usuario(self, usuario_id, nome, email, senha):
        usuario = self.repository.buscar_por_id(usuario_id)
        if not usuario:
            return False, "Usuário não encontrado."
        if not nome.strip() or not email.strip() or not senha.strip():
            return False, "Preencha todos os campos."
        nome = nome.strip()
        email = email.strip()
        if '@' not in email or '.' not in email:
            return False, 'Email inválido.'
        existente = self.repository.buscar_por_email(email)
        if existente and existente['id'] != usuario_id:
            return False, "Email já cadastrado."
        if len(senha) < 6:
            return False, "A senha precisa ter pelo menos 6 caracteres."
        if any(c.isupper() for c in senha) == False:
            return False, "A senha precisa ter pelo menos uma letra maiúscula."
        self.repository.atualizar(usuario_id, nome, email, senha)
        return True, "Usuário atualizado com sucesso."

    def excluir_conta(self, usuario_id):
        usuario = self.repository.buscar_por_id(usuario_id)
        if not usuario:
            return False, "Usuário não encontrado."
        self.repository.deletar(usuario_id)
        return True, "Conta excluída com sucesso."

    def buscar_por_id(self, usuario_id):
        return self.repository.buscar_por_id(usuario_id)
