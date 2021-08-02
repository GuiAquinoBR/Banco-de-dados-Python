from pymysql import Error
from db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
dados = ('Guilherme', '98765-4321')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, dados)
        conexao.commit()
    except Error as e:
        print(f'Erro ocorrido: {e}')
    else:
        print('1 registro incluído, ID:', cursor.lastrowid)
