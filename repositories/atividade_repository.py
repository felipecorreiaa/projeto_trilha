import sqlite3


class AtividadeRepository:
    def inserir(self, nome, organizacao_id, dia, horario, descricao, link_inscricao):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'INSERT INTO atividades (nome, organizacao_id, dia, horario, descricao, link_inscricao) VALUES (?, ?, ?, ?, ?, ?)',
            (nome, organizacao_id, dia, horario, descricao, link_inscricao)
        )
        conn.commit()
        conn.close()

    def listar_por_organizacao(self, organizacao_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        atividades = conn.execute(
            'SELECT * FROM atividades WHERE organizacao_id = ? ORDER BY dia, horario', 
            (organizacao_id,)
        ).fetchall()
        conn.close()
        return atividades

    def buscar_por_id(self, atividade_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        atividade = conn.execute(
            'SELECT * FROM atividades WHERE id = ?', (atividade_id,)
        ).fetchone()
        conn.close()
        return atividade

    def atualizar(self, atividade_id, nome, dia, horario, descricao, link_inscricao):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'UPDATE atividades SET nome = ?, dia = ?, horario = ?, descricao = ?, link_inscricao = ?'
            'WHERE id = ?'
            (nome, dia, horario, descricao, link_inscricao, atividade_id)
        )
        conn.commit()
        conn.close()

    def excluir(self, atividade_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute('DELETE FROM inscricoes WHERE atividade_id = ?', (atividade_id,))
        conn.execute('DELETE FROM atividades WHERE id = ?', (atividade_id,))
        conn.commit()
        conn.close()