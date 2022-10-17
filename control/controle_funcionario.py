import mysql.connector
from control.db.db_conexao import conexao
from tkinter import messagebox as mg
from control.error.captura_erros import (SenhaDiferente, EmailInvalido, CampoVazio)


def listar_funcionarios():
    """Função para exibir todos os funcionarios cadastrados"""

    # creando cursor
    banco = conexao()
    cursor = banco.cursor()

    # executando query
    query = 'select nome, cpf from funcionario'

    # executar query para pegar o arquivo
    cursor.execute(query)
    servicos = cursor.fetchall()

    return servicos


def exibir_funcionario(cpf):
    """Função para exibir dados do funcionario pelo cpf"""
    
    # creando cursor
    banco = conexao()
    cursor = banco.cursor()

    # executando query
    query = f'select * from funcionario where cpf ="{cpf}"'

    # executar query para pegar o arquivo
    cursor.execute(query)
    funcionario = cursor.fetchone()

    return funcionario


def verificar_login(login):
    """verificar login de funcionario"""

    # creando cursor
    banco = conexao()
    cursor = banco.cursor()

    # montando a query
    query = f'SELECT login, senha FROM funcionario where login="{login}";'

    # executar query para pegar o arquivo
    cursor.execute(query)
    funcionario = cursor.fetchone()

    return funcionario

def verificar_senha(senha, confirmacao_senha):
    """Função para verificar se a senha conferem"""
    
    if senha != confirmacao_senha:
        raise SenhaDiferente


def verificar_email(email):
    """Função para verificar se o email é valido"""
    
    letras_maiusculas = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    simbolos_permitidos = [i for i in email if i not in letras_maiusculas]

    if simbolos_permitidos != ['@', '.']:
        raise EmailInvalido


def verificar_campos_vazio(*args):
    """Função para verificar se a campos vazios"""
    
    # passando valores para verificar em uma lista
    dados = [*args]

    # fazendo verificação dos campos, caso vazio retorna um erro
    for dado in dados:
        if not dado:
            raise CampoVazio


def gravar_dados_funcionario(cpf, nome, celular, email, cep, cidade, uf,
complemento, bairro, endereco, numero, imagem, login, senha, confir_senha):
    """Função para gravar os dados do funcionario no banco"""

    try:

        # verficar se a campos vazios
        verificar_campos_vazio(cpf, nome, celular, email, cep, cidade, uf,
        complemento, bairro, endereco, numero, imagem, login, senha, confir_senha)

        # chamada de funções para verificar email e senha
        verificar_email(email)
        verificar_senha(senha, confir_senha)

        # criando um cursor 
        banco = conexao()
        cursor = banco.cursor()

        # passando os dados para uma tupla
        funcionario = (cpf, nome, celular, email, cep, cidade, uf,
         complemento, bairro, endereco, numero, imagem, login, senha) 

        # preparar a query
        query = 'INSERT INTO funcionario(cpf, nome, celular, email, cep, cidade,'+\
        'uf, complemento, bairro, endereco, numero, imagem, login, senha)'+\
        'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'

        # execute a query e commit no banco de dados
        cursor.execute(query, funcionario)
        banco.commit()
        mg.showinfo('Sucesso', 'Funcionario cadastrado com sucesso!')

    except mysql.connector.errors.ProgrammingError:
        mg.showerror('Error', 'Parâmetros insuficientes para a instrução SQL')

    except mysql.connector.errors.IntegrityError:
        mg.showerror('Error', 'Funcionario ja cadastrado no sistema!')

    except mysql.connector.errors.DataError:
        mg.showerror('Error', 'excedeu o numero de caracteres!')
    finally:
        banco.close()
        

def atualizar_dados_funcionario(cpf, nome, celular, email, cep, cidade, uf,
        complemento, bairro, endereco, numero, login, senha, confir_senha):
    """Função para atualizar os dados do funcionario no banco"""
    
    try:

        # verficar se a campos vazios
        verificar_campos_vazio(cpf, nome, celular, email, cep, cidade, uf,
        complemento, bairro, endereco, numero, login, senha, confir_senha)

        # chamada de funções para verificar email e senha
        verificar_email(email)
        verificar_senha(senha, confir_senha)

        # criando um cursor 
        banco = conexao()
        cursor = banco.cursor()

        # preparar a query
        query = f'UPDATE funcionario SET nome = "{nome}", celular = "{celular}",'+\
           f'email = "{email}", cep = "{cep}", cidade = "{cidade}", uf = "{uf}",'+\
           f'complemento = "{complemento}", bairro = "{bairro}", endereco = "{endereco}",'+\
           f'numero = {numero}, login = "{login}",'+\
           f'senha = "{senha}" WHERE cpf = "{cpf}";'

        # execute a query e commit no banco de dados
        cursor.execute(query)
        banco.commit()
        banco.close()
        mg.showinfo( 'Sucesso','Dados atualizados com sucesso!')

    except mysql.connector.errors.ProgrammingError:
        mg.showerror('Error', 'Parâmetros insuficientes para a instrução SQL')

    except mysql.connector.errors.IntegrityError:
        mg.showerror('Error', 'Funcionario ja cadastrado no sistema!')

    except mysql.connector.errors.DataError:
        mg.showerror('Error', 'Excedeu o numero de caracteres!')
