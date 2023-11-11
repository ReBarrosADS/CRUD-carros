import sqlite3

#Classe para lider com o banco de dados
class BD:
    #Contrutor
    def __init__(self, banco_dados):
        self.conectarBanco(banco_dados)


    def conectarBanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)
        self.cursor = self.banco.cursor()


        self.criarTabelaCarros()

    def criarTabelaCarros(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS carros(
                id INTEGER PRiMARY KEY AUTOINCREMENT,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                ano_fabricacao DATE NOT NULL,
                ano_modelo DATE NOT NULL,
                tipo_carro TEXT NULL,
                versao_modelo TEXT NOT NULL,
                cor TEXT NULL                     
            )
        """)
    def inserir(self, tabela, valores):
        colunas = ', '.join(valores.keys())
        placeholders = ', '.join(['?'] *len(valores))


        #criar o sql do banco de dados
        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})" 


        self.cursor.execute(sql, tuple(valores.values()))

        #Confirma as alterações do banco
        self.banco.commit()

        #Verifica se deu certo o armazenamento
        if self.cursor.lastrowid:
            print(f"{tabela} salvo com sucesso!")
            return False
        
    def buscarDados(self, tabela, campos = '*'):
        sql = f"SELECT {campos} FROM {tabela}"
        self.cursor.execute(sql)


        dados = self.cursor.fetchall()
        return dados



