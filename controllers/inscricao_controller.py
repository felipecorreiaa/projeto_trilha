from repositories.inscricao_repository import InscricaoRepository
from repositories.atividade_repository import AtividadeRepository
from repositories.usuario_repository import UsuarioRepository
from datetime import datetime


class InscricaoController:
    def __init__(self):
        self.repository = InscricaoRepository()
        self.atividades_repository = AtividadeRepository()
        self.usuario_repository = UsuarioRepository()

    def inscrever(self, atividade_id, usuario_id):
        if not self.usuario_repository.buscar_por_id(usuario_id):
            return False, "Usuário não encontrado."
        atividade = self.atividades_repository.buscar_por_id(atividade_id)
        if not atividade:
            return False, "Atividade não encontrada."
        inicio = datetime.strptime(f"{atividade['dia']} {atividade['horario']}", "%Y-%m-%d %H:%M")
        if inicio < datetime.now():
            return False, "Essa atividade já aconteceu. Não é possível se inscrever."
        if self.repository.buscar(atividade_id, usuario_id):
            return False, "Você já está inscrito nessa atividade."
        self.repository.inserir(atividade_id, usuario_id)
        return True, "Inscrição realizada com sucesso."

    def cancelar(self, atividade_id, usuario_id):
        if not self.repository.buscar(atividade_id, usuario_id):
            return False, "Você não está inscrito nessa atividade."
        self.repository.excluir(atividade_id, usuario_id)
        return True, "Inscrição cancelada com sucesso."

    def listar_por_usuario(self, usuario_id):
        return self.repository.listar_por_usuario(usuario_id)