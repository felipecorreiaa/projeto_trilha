import sqlite3


class InscricaoRepository:
    def inserir(self, atividade_id, usuario_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'INSERT INTO inscricoes (atividade_id, usuario_id) VALUES (?, ?)',
            (atividade_id, usuario_id)
        )
        conn.commit()
        conn.close()

    def buscar(self, atividade_id, usuario_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        inscricao = conn.execute(
            'SELECT * FROM inscricoes WHERE atividade_id = ? AND usuario_id = ?',
            (atividade_id, usuario_id)
        ).fetchone()
        conn.close()
        return inscricao

    def listar_por_usuario(self, usuario_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        inscricoes = conn.execute(
            '''SELECT a.* FROM atividades a
            JOIN inscricoes i ON i.atividade_id = a.id
            WHERE i.usuario_id = ?
            ORDER BY a.dia, a.horario''',
            (usuario_id,)
        ).fetchall()
        conn.close()
        return inscricoes

    def excluir(self, atividade_id, usuario_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'DELETE FROM inscricoes WHERE atividade_id = ? AND usuario_id = ?',
            (atividade_id, usuario_id)
        )
        conn.commit()
        conn.close()

    def listar_por_atividade(self, atividade_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        inscritos = conn.execute(
            '''SELECT u.id AS usuario_id, u.nome, i.presente
            FROM inscricoes i
            JOIN usuarios u ON u.id = i.usuario_id
            Where i.atividade_id = ?
            ORDER BY u.nome''',
            (atividade_id,)
        ).fetchall()
        conn.close()
        return inscritos

    def atualizar_presenca(self, atividade_id, usuario_id, presente):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'UPDATE inscricoes SET presente = ? WHERE atividade_id = ? AND usuario_id = ?',
            (presente, atividade_id, usuario_id)
        )
        conn.commit()
        conn.close()