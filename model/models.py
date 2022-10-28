import sqlite3


class ConectandoBD:
    def __init__(self):
        self.__conexao = None
        self.cursor = None
        self.criarTabelas()

    def conectar(self):
        self.__conexao = sqlite3.connect('../model/emails.db')
        self.cursor = self.__conexao.cursor()

    def desconectar(self):
        self.__conexao.commit()
        self.__conexao.close()

    def criarTabelas(self):
        self.conectar()
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS EMAIL(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT VARCHAR(255) NOT NULL 
        );
        ''')
        self.desconectar()

    def adicionarEmail(self, email: str):
        try:
            conn = sqlite3.connect('../model/emails.db')
            cursor = conn.cursor()
            # email = email.replace('@','')
            cursor.execute(f"""
            INSERT INTO EMAIL (email)
            VALUES ('{email}')""")

            # gravando no bd

            conn.commit()

            print('Dados inseridos com sucesso.')

            conn.close()
        except sqlite3.IntegrityError:
            print(f'Item {email} já cadastrado')

    def removerEmail(self, email: str):
        conn = sqlite3.connect('../model/emails.db')
        cursor = conn.cursor()
        # inserindo dados na tabela
        cursor.execute(f"""
        DELETE FROM EMAIL WHERE nomeProduto = '{email}'
        """)

        # gravando no bd
        conn.commit()

        print('Dados inseridos com sucesso.')

        conn.close()

    def obterListaDeEmail(self):
        conn = sqlite3.connect('../model/emails.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM EMAIL
        """)
        # lendo os dados
        conn.commit()

        listaDeEmail = cursor.fetchall()
        for linha in cursor.fetchall():
            print(linha)
        return listaDeEmail
