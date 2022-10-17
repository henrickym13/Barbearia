import mysql.connector
from tkinter import messagebox as mg
from control.db.db_conexao import conexao
from control.error.captura_erros import CampoVazio


def exibir_horario_marcado_func(funcionario, data):
    """Função para exibir os horario marcados para um funcionario"""
    
    # variavel do banco de dados
    banco = conexao()
    cursor = banco.cursor()

    # chamada da funçãoo para pegar cpf
    cpf = exibir_nome_funcionario(funcionario)

    # executando query
    query = f'SELECT horario FROM agendamento WHERE cpf = "{cpf}" and'+\
        f' dia = "{data}";'
    cursor.execute(query)
    horarios = cursor.fetchall()

    return mostrar_horarios_disponivel(horarios)


def mostrar_horarios_disponivel(horario_funcionario):
    """Função para exibir horarios para agendamento"""
    
    horario_agendamento = [str(valor) + ':00' for valor in range(10, 20)]
    horario_ocupado = horario_funcionario

    # verificar os horarios entre as listas
    for valor in horario_agendamento:
        for data in horario_ocupado:
            if(valor==data[0]):
                horario_agendamento.remove(valor)
                break
    
    # retornar a nova lista com os horarios disponiveis
    return horario_agendamento
    

def exibir_valor_servico(servico):
    """Função para exibir o valor do serviço solicitado"""

    banco = conexao()
    cursor = banco.cursor()

    # executar query
    query = f'SELECT preco FROM servicos WHERE servico ="{servico}"'
    cursor.execute(query)
    preco = cursor.fetchone()

    return preco[0]


def verificar_campos_vazio(dia, funcionario, horario, cliente, servico, preco):
    """Função para verificar se a campos vazios"""
    
    # passando valores para verificar em uma lista
    dados = [dia, funcionario, horario, cliente, servico, preco]

    # fazendo verificação dos campos, caso vazio retorna um erro
    for dado in dados:
        if not dado:
            raise CampoVazio


def realizar_agendamento(dia, funcionario, horario, cliente, servico, preco):
    """Função para realizar o  agendamento"""
    
    try:

        # verificar se tem campos vazios
        verificar_campos_vazio(dia, funcionario, horario, cliente, servico, preco)

        # instancia da função de conexao
        banco = conexao()
        cursor = banco.cursor()

        cpf = exibir_nome_funcionario(funcionario)

        agendamento = (dia, cpf, horario, cliente, servico, preco)

        # montar a query
        query = 'INSERT INTO agendamento(dia, cpf, horario, cliente,'+\
            'servico, preco) VALUES (%s, %s, %s, %s, %s, %s);'
        
        # executar a query e exibir mensagem de sucesso
        cursor.execute(query, agendamento)
        banco.commit()
        mg.showinfo('Sucesso', 'Agendamento realizado com sucesso!')

    except mysql.connector.errors.DataError:
        mg.showerror('Error', 'excedeu o numero de caracteres!')
    finally:
        banco.close()


def exibir_agendamentos(dia):
    """Função para exibir os agendamentos do dia"""

    # instancia a função de conexão
    banco = conexao()
    cursor = banco.cursor()

    # motando a query
    query = 'SELECT agendamento.horario, funcionario.nome,'+\
    'agendamento.cliente, agendamento.servico, agendamento.preco '+\
    'FROM agendamento INNER JOIN funcionario on agendamento.cpf='+\
    f'funcionario.cpf and agendamento.dia = "{dia}";'

    # executando query
    cursor.execute(query)
    agendamentos = cursor.fetchall()

    return agendamentos


def exibir_agendamentos_funcionario(nome, data):
    """Função para exibir os agendamentos do dia por funcionario"""

    # instancia a função de conexão
    banco = conexao()
    cursor = banco.cursor()
    cpf = exibir_nome_funcionario(nome)

    # motando a query
    query = 'SELECT agendamento.horario, funcionario.nome,'+\
    'agendamento.cliente, agendamento.servico, agendamento.preco '+\
    'FROM agendamento INNER JOIN funcionario on agendamento.cpf='+\
    f'funcionario.cpf and agendamento.cpf = "{cpf}" and '+\
    f'agendamento.dia= "{data}";'

    # executando query
    cursor.execute(query)
    agendamentos = cursor.fetchall()

    return agendamentos


def exibir_nome_funcionario(nome):
    """Função para exibir cpf do funcionario pelo nome"""

    # creando cursor
    banco = conexao()
    cursor = banco.cursor()

    # preparar query
    query = f'select cpf from funcionario where nome = "{nome}";'

    # executar query para pegar o arquivo
    cursor.execute(query)
    nome_funcionario = cursor.fetchone()
    nome_funcionario = nome_funcionario[0]

    return nome_funcionario