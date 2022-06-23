import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "teste"
)

cursor = db.cursor()

#comando_SQL = "INSERT INTO jogos (nome,score,desenvolvedor) VALUES(%s,%s,%s)"
#inseri o dado para modificacao
#dados = ("MOH","60","EA")

#comando_SQL = "UPDATE jogos SET score = 70 WHERE nome = 'MOH'"

comando_SQL = " DELETE FROM jogos WHERE nome = 'MOH'"
cursor.execute(comando_SQL)
db.commit()