from tkinter import messagebox as mg

class CampoVazio(Exception):
    """classe para exibir erro de campo vazio"""

    def __str__(self) -> str:
        return mg.showerror('Erro', 'Campos obrigatórios vazio!')


class EmailInvalido(Exception):
    """classe para exibir mensagem de email invalido"""

    def __str__(self) -> str:
        return mg.showerror('Erro', 'Digite um e-mail valido!')


class SenhaDiferente(Exception):
    """classe para verificar senhas"""

    def __str__(self) -> str:
        return mg.showerror('Erro', 'Senhas não conferem!')