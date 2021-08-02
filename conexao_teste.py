from db import nova_conexao

with nova_conexao() as conexao:
    if conexao:
        print('Conectado!')

print('Fim!')
