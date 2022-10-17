import mysql.connector
from tkinter import messagebox as mg
from control.db.db_conexao import conexao
from control.error.captura_erros import CampoVazio


def exibir_produtos():
    """Função para exibir produtos cadastrados"""

    # criando cursor
    banco = conexao()
    cursor = banco.cursor()

    # executando query
    query = 'select nome, quantidade from produto'

    # executar query para pegar o arquivo
    cursor.execute(query)
    servicos = cursor.fetchall()

    return servicos


def pesquisar_produto(produto_nome):
    """Função para procurar produtos especifico"""

    # criando cursor
    banco = conexao()
    cursor = banco.cursor()

    # executando query
    query = f'SELECT nome, quantidade FROM produto WHERE nome = "{produto_nome}"'

    # executar query para pegar o arquivo
    cursor.execute(query)
    servicos = cursor.fetchall()

    return list(servicos)


def verificar_campos_vazio(nome, quantidade):
    """Função para verificar campos vazio"""

    dados = [nome, quantidade]

    # fazendo verificação dos campos, caso vazio retorna um erro
    for dado in dados:
        if not dado:
            raise CampoVazio


def cadastrar_produto(nome, quantidade):
    """Função para cadastrar produtos no sistema"""

    try:

        # verificar campos
        verificar_campos_vazio(nome, quantidade)

        # criando cursor
        banco = conexao()
        cursor = banco.cursor()

        # passando a lista para uma tupla e executando query
        produto = (nome, quantidade)
        query = 'INSERT INTO produto(nome, quantidade) VALUES'+\
        '(%s, %s);'

        # executando cursor
        cursor.execute(query, produto)
        banco.commit()
        mg.showinfo('Sucesso', 'dados gravados com sucesso!')
    
    except mysql.connector.errors.IntegrityError:
        mg.showerror('Error', 'Produto ja cadastrado no sistema!')


def atualizar_qtd_produto(nome, quantidade):
    """Função para atualizar quantidade produtos no sistema"""

    # verificar campos
    verificar_campos_vazio(nome, quantidade)

    # criando cursor
    banco = conexao()
    cursor = banco.cursor()

    # passando a lista para uma tupla e executando query
    query = f'UPDATE produto set quantidade = "{int(quantidade)}" '+\
        f'WHERE nome = "{nome}"'

    # executando cursor
    cursor.execute(query)
    banco.commit()
    banco.close()
    mg.showinfo('Sucesso', 'Dados atualizados com sucesso!')
