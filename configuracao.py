import pymysql

conexao = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='My44e7!s$ql',
)

print(conexao)
