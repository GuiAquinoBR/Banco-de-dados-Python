from pymysql import Error
from db import nova_conexao

sql = 'DELETE FROM contatos WHERE nome = %s'
args = ('Guilherme',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except Error as e:
        print(f'Erro ocorrido: {e}')
    else:
        print(f'{cursor.rowcount} registro(s) deletado(s).')
