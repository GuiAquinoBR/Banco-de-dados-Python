from pymysql import Error
from db import nova_conexao

sql = 'ALTER TABLE contatos ADD COLUMN\
       id INT AUTO_INCREMENT PRIMARY KEY'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
    except Error as e:
        print(f'Erro ocorrido: {e}')
