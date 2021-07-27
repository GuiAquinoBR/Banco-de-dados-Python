import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='My44e7!s$ql'
)

cursor = conexao.cursor()

cursor.execute(
    'CREATE DATABASE IF NOT EXISTS agenda'
)
