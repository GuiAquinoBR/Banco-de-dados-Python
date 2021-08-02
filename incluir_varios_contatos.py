from pymysql import Error
from db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
dados = (
    ('Guilherme',   '98765-1234'),
    ('Inês',        '98765-9876'),
    ('Nilton',      '98765-5432'),
    ('Daiane',      '98765-1234'),
    ('Leidiane',    '98765-5678'),
    ('Washington',  '98765-9000'),
    ('Arnaldo',     '98754-9195'),
    ('Bernardo',    '94132-4321'),
    ('Carlos',      '98765-5867'),
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
