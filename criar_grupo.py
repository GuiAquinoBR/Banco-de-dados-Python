from db import nova_conexao
from pymysql import Error

tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(50)
    )
"""

tabela_alterar_contato_1 = """
    ALTER TABLE contatos ADD grupo_id INT
"""

tabela_alterar_contato_2 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES grupos(id)
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_grupo)
            cursor.execute(tabela_alterar_contato_1)
            cursor.execute(tabela_alterar_contato_2)
        except Error as e:
            print(f'Erro: {e}')
except Error as e:
    print(f'Erro CONEXÃO: {e}')
