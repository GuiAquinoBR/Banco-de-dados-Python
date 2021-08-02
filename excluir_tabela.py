from db import nova_conexao
from pymysql import Error

def excluir_tabela_emails():
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute('DROP TABLE emails')
        except Error as e:
            print(f'Erro de EXCLUSÃO: {e}')

def excluir_tabela_contatos():
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute('DROP TABLE contatos')
        except Error as e:
            print(f'Erro de EXCLUSÃO: {e}')
