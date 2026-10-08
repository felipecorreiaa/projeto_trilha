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
