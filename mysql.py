import pymysql
conn = pymysql.connect(
    host = "localhost",
    user="root",
    password="Matheus21",
    database="cadastro"
)
cursor = conn.cursor()
cursor.execute("select * from usuarios")
for p in cursor.fetchall():
    print(p)