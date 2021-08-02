from pymysql import Error
from db import nova_conexao

sql = 'INSERT INTO grupos (descricao) VALUES (%s)'
dados = (
    ('Casa',),
    ('Trabalho',),
    ('Futebol',)
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, dados)
        conexao.commit()
    except Error as e:
        print(f'Erro ocorrido: {e}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
