from pymysql import Error
from db import nova_conexao

sql = 'SELECT * FROM contatos'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except Error as e:
        print(f'Erro ocorrido: {e}')
    else:
        for contato in contatos:
            print(f'{contato[2]:3d} - {contato[0]:10s} Telefone: {contato[1]}')
