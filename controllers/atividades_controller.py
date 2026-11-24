from datetime import datetime
from repositories.atividade_repository import AtividadeRepository
from repositories.organizacoes_repository import OrganizacoesRepository


class AtividadesController:
    def __init__(self):
        self.repository = AtividadeRepository()
        self.organizacoes_repository = OrganizacoesRepository()

    def _validar(self, nome, dia, horario, descricao):
        """Retorna (mensagem_de_erro, dia_no_formato_do_banco)"""
        if not nome.strip() or not dia.strip() or not horario.strip() or not descricao.strip():
            return "Preencha todos os campos obrigatórios.", None
        try:
            dia_iso = datetime.strptime(dia.strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            return "Dia inválido. Use dd/mm/aaaa", None
        try:
            datetime.strptime(horario.strip(), "%H:%M")
        except ValueError:
            return "Horário inválido. Use HH:MM.", None
        return None, dia_iso

    def _e_gestor_da_organizacao(self, organizacao_id, usuario_id):
        organizacao = self.organizacoes_repository.buscar_por_id(organizacao_id)
        return organizacao is not None and organizacao['gestor_id'] == usuario_id

    def cadastrar(self, organizacao_id, gestor_id, nome, dia, horario, descricao, link):
        if not self._e_gestor_da_organizacao(organizacao_id, gestor_id):
            return False, "Você não pode adicionar atividades nesta organização."
        erro, dia_iso = self._validar(nome, dia, horario, descricao)
        if erro:
            return False, erro
        self.repository.inserir(nome.strip(), organizacao_id, dia_iso, horario.strip(), descricao.strip(), link.strip())
        return True, "Atividade adicionada com sucesso."

    def listar_por_organizacao(self, organizacao_id):
        return self.repository.listar_por_organizacao(organizacao_id)

    def atualizar(self, atividade_id, gestor_id, nome, dia, horario, descricao, link):
        atividade = self.repository.buscar_por_id(atividade_id)
        if not atividade:
            return False, "Atividade não encontrada."
        if not self._e_gestor_da_organizacao(atividade['organizacao_id'], gestor_id):
            return False, "Você não pode editar essa atividade."
        erro, dia_iso = self._validar(nome, dia, horario, descricao)
        if erro:
            return False, erro
        self.repository.atualizar(atividade_id, nome.strip(), dia_iso, horario.strip(), descricao.strip(), link.strip())
        return True, "Atividade atualizada com sucesso."

    def excluir(self, atividade_id, gestor_id):
        atividade = self.repository.buscar_por_id(atividade_id)
        if not atividade:
            return False, "Atividade não encontrada"
        if not self._e_gestor_da_organizacao(atividade['organizacao_id'], gestor_id):
            return False, "Você não pode excluir essa atividade"
        self.repository.excluir(atividade_id)
        return True, "Atividade excluída com sucesso."
