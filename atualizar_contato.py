from pymysql import Error
from db import nova_conexao

sql = 'UPDATE contatos\
       SET nome = %s  \
       WHERE id = %s'
dados = ('Daiane','9')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, dados)
        conexao.commit()
    except Error as e:
        print(f'Erro ocorrido: {e}')
    else:
        if cursor.rowcount >= 1:
            print('Atualização realizada com sucesso!')
        else:
            print('Não houve atualização.')
