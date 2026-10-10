import sqlite3


class OrganizacoesRepository:
    def inserir(self, nome, gestor_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'INSERT INTO organizacoes (nome, gestor_id) VALUES (?, ?)',
            (nome, gestor_id)
        )
        conn.commit()
        conn.close()

    def buscar_por_nome(self, nome):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        organizacao = conn.execute(
            'SELECT * FROM organizacoes WHERE nome = ?', (nome,)
        ).fetchone()
        conn.close()
        return organizacao

    def buscar_por_id(self, organizacao_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        organizacao = conn.execute(
            'SELECT * FROM organizacoes WHERE id = ?', (organizacao_id,)
        ).fetchone()
        conn.close()
        return organizacao

    def listar_organizacoes(self):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        organizacoes = conn.execute(
            'SELECT * FROM organizacoes'
        ).fetchall()
        conn.close()
        return organizacoes

    def listar_por_gestor(self, gestor_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        organizacoes = conn.execute(
            'SELECT * FROM organizacoes WHERE gestor_id = ?', (gestor_id,)
        ).fetchall()
        conn.close()
        return organizacoes

    def atualizar(self, organizacao_id, nome):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'UPDATE organizacoes SET nome = ? WHERE id = ?',
            (nome, organizacao_id)
        )
        conn.commit()
        conn.close()

    def excluir(self, organizacao_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'DELETE FROM organizacoes WHERE id = ?',
            (organizacao_id,)
        )
        conn.commit()
        conn.close()
