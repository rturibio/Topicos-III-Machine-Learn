import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "teste"
)

cursor = db.cursor()

#cursor.execute("CREATE TABLE pessoas (nome VARCHAR(255), idade INT(3), cidade VARCHAR(255))")
#comando_SQL = "INSERT INTO pessoas (nome, idade,cidade) VALUES(%s,%s,%s)"
#dados = ("Jose","20","Sao Paulo")
#dados = ("Joao","25","Laguna")
#dados = ("Maria","30","Rio Grande")
#cursor.execute(comando_SQL,dados)
#db.commit()

#cursor.execute("CREATE TABLE jogos (nome VARCHAR(255), score INT(3), desenvolvedor VARCHAR(255))")
comando_SQL = "INSERT INTO jogos (nome,score,desenvolvedor) VALUES(%s,%s,%s)"
#dados = ("Mario","97","Nintendo")
#dados = ("Final Fantasy","99","SquareSoft")
dados = ("Sonic","92","Sega")
cursor.execute(comando_SQL,dados)
db.commit()