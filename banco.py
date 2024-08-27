import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_usuarios(
        idusuario integer primary key autoincrement,
        nome text,
        telefone text,
        email text,
        usuario text,
        senha text)""")
        ("""create table if not exists tbl_cidades(
                idcidades integer primary key autoincrement,
                nome_cidades text,
                uf text)""")
        self.conexao.commit()
        c.close()