from pymysql import Error
from db import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contato_grupo = {
    'Inês': 'Casa',
    'Nilton': 'Casa',
    'Guilherme': 'Casa',
    'Leidiane': 'Casa',
    'Washington': 'Trabalho',
    'Daiane': 'Trabalho',
    'Arnaldo': 'Futebol',
    'Bernardo': 'Futebol',
    'Carlos': 'Futebol'
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except Error as e:
        print(f'Erro ocorrido: {e}.')
    else:
        print('Contatos associados.')
