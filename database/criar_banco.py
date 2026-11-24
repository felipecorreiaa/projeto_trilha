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
        tipo TEXT NOT NULL CHECK(tipo IN ('membro', 'gestor')))
    ''')

#criar tabela orgs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS organizacoes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        gestor_id INTEGER REFERENCES usuarios(id))
    ''')

#criar tabela de atividades
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS atividades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        organizacao_id INTEGER NOT NULL REFERENCES organizacoes(id),
        nome TEXT NOT NULL,
        dia TEXT NOT NULL,
        horario TEXT NOT NULL,
        descricao TEXT NOT NULL,
        link_inscricao TEXT)
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inscricoes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        atividade_id INTEGER NOT NULL REFERENCES atividades(id),
        usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
        presente INTEGER DEFAULT 0,
        UNIQUE(atividade_id, usuario_id))
    ''')

    conn.commit()
    conn.close()


