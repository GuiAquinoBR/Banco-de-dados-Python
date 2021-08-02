from pymysql import cursors
from pymysql.cursors import DictCursor
from db import nova_conexao
from pymysql import Error

sql = '''
    SELECT 
        grupos.descricao AS grupo,
        contatos.nome AS contato_nome
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, contato_nome 
'''

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(DictCursor)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except Error as e:
        print(f'Erro ocorrido: {e}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["contato_nome"]}')
