import mysql.connector

def conexao():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='barbearia'
    )
    return mydb