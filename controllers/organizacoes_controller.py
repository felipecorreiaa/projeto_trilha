from repositories.organizacoes_repository import OrganizacoesRepository

class OrganizacoesController:
    def __init__(self):
        self.repository = OrganizacoesRepository()

    def cadastrar(self, nome, gestor_id):
        if self.repository.buscar_por_nome(nome):
            return False, "Organização já cadastrada."
        self.repository.inserir(nome, gestor_id)
        return True, "Organização cadastrada com sucesso."

    def listar_organizacoes(self):
        return self.repository.listar_organizacoes()

    def listar_organizacoes_por_gestor(self, gestor_id):
        return self.repository.listar_por_gestor(gestor_id)

    def atualizar(self, organizacao_id, novo_nome):
        organizacao = self.repository.buscar_por_id(organizacao_id)
        if not organizacao:
            return False, "Organização não encontrada."
        if self.repository.buscar_por_nome(novo_nome):
            return False, "Já existe uma organização com esse nome."
        self.repository.atualizar(organizacao_id, novo_nome)
        return True, "Nome da organização atualizado com sucesso."

    def excluir(self, organizacao_id):
        organizacao = self.repository.buscar_por_id(organizacao_id)
        if not organizacao:
            return False, "Organização não encontrada."
        self.repository.excluir(organizacao_id)
        return True, "Organização excluída com sucesso."

    def buscar_por_nome(self, nome):
        return self.repository.buscar_por_nome(nome)
    
