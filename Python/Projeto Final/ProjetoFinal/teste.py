import sqlite3


def db_verificar_email(self):
        con = sqlite3.connect('database/dados_informacoes.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios")
        emails = cursor.fetchall()
        con.close()
        return emails

dados_database = "SELECT email FROM usuarios"
verificado_email = db_verificar_email(dados_database)
for i in verificado_email:
    print(i)
print(verificado_email[0][0])