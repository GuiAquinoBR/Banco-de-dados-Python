import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='My44e7!s$ql'
)

cursor = conexao.cursor()
cursor.execute(
    'SHOW DATABASES'
)

for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')
