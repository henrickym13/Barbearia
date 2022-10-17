from control.db.db_conexao import conexao

def exibir_servico_preco():
    """Função para exibir todos os serviços"""

    # creando cursor
    banco = conexao()
    cursor = banco.cursor()

    # executando query
    query = 'select * from servicos'

    # executar query para pegar o arquivo
    cursor.execute(query)
    servicos = cursor.fetchall()
    #servicos = sorted(servicos)

    return servicos
