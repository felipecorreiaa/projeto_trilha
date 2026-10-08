import sqlite3


def criar_tabelas():
#conectar sqlite
    conn = sqlite3.connect('database/trilha.db')
    cursor = conn.cursor()

#criar tabela usuario
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL,
        tipo TEXT NOT NULL CHECK(tipo IN ('membro', 'gestor')),
        confirmado INTEGER DEFAULT 0) 
    ''')

#criar tabela orgs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS organizacoes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        gestor_id INTEGER REFERENCES users(id))
    ''')

#criar tabela de atividades
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS atividades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        organizacao_id INTEGER NOT NULL REFERENCES organizacoes(id),
        dia TEXT NOT NULL,
        horario TEXT NOT NULL,
        descricao TEXT NOT NULL,
        link_inscricao TEXT)
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabelas()

