import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "teste"
)

cursor = db.cursor()

comando_SQL = "SELECT * FROM pessoas INNER JOIN jogos WHERE idade > 20 AND score > 95" 

cursor.execute(comando_SQL)

valores_lidos = cursor.fetchall()

print(valores_lidos)