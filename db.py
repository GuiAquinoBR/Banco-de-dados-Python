import pymysql
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    password='My44e7!s$ql',
    database='agenda'
)

@contextmanager
def nova_conexao():
    conexao = pymysql.connect(**parametros)
    try:
        yield conexao
    finally:
        conexao.close()
