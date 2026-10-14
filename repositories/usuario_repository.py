import sqlite3


class UsuarioRepository:
    def inserir(self, nome, email, senha, tipo):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'INSERT INTO usuarios (nome, email, senha, tipo) VALUES (?, ?, ?, ?)',
            (nome, email, senha, tipo)
        )
        conn.commit()
        conn.close()

    def buscar_por_email(self, email):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        usuario = conn.execute(
            'SELECT * FROM usuarios WHERE email = ?', (email,)
        ).fetchone()
        conn.close()
        return usuario

    def buscar_por_id(self, usuario_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.row_factory = sqlite3.Row
        usuario = conn.execute(
            'SELECT * FROM usuarios WHERE id = ?', (usuario_id,)
        ).fetchone()
        conn.close()
        return usuario

    def atualizar(self, usuario_id, nome, email, senha):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?',
            (nome, email, senha, usuario_id)
        )
        conn.commit()
        conn.close()

    def deletar(self, usuario_id):
        conn = sqlite3.connect('database/trilha.db')
        conn.execute(
            'DELETE FROM usuarios WHERE id = ?',
            (usuario_id,)
        )
        conn.commit()
        conn.close()
        
