from tkinter import *
from tkinter import messagebox as mg
from utils.config_imagens import configurar_imagem
from utils.centralizar_frame import centralizar
from control.controle_funcionario import verificar_login
from tela_inicial import TelaPrincipal


class TelaLogin:

    def __init__(self):
        """Método construtor da classe"""

        # configurações da tela
        janela = Tk()
        janela.title('Login')
        janela_largura = 350
        janela_altura = 500
        janela.minsize(janela_largura, janela_altura)
        janela.maxsize(janela_largura, janela_altura)

        # centralizar o frame na tela
        centralizar(janela, janela_largura, janela_altura)
        
        # configurações das imagens
        img_logo = configurar_imagem('imagens\\logo_02.png', 330, 240)
        img_entrar = configurar_imagem('imagens\\entrar.png', 25, 25)
        img_sair = configurar_imagem('imagens\\sair.png', 25, 25)
        
        # adicionando labels
        lbl_icone = Label(janela, image=img_logo)
        lbl_icone.place(x=18, y=10)
        lbl_div = Label(janela, background='black')
        lbl_div.place(x=10, y=270, width=330, height=3)
        lbl_login = Label(janela, text='Login', font='Arial 12')
        lbl_login.place(x=70, y=320, width=50)
        lbl_senha = Label(janela, text='Senha', font='Arial 12')
        lbl_senha.place(x=70, y=360, width=50)

        # adicionando entries
        self.txt_login = Entry(janela)
        self.txt_login.place(x=130, y=322)
        self.txt_senha = Entry(janela, show='*')
        self.txt_senha.place(x=130, y=362)

        # adicionando buttons
        btn_entrar = Button(janela, image=img_entrar, text='Entrar',
        compound=LEFT, font='Arial 12', padx= 10,
        command=lambda: self.verificar_login(janela))
        btn_entrar.place(x=10, y=450, width=140, height=40)
        btn_sair = Button(janela, image=img_sair, text='Sair',
        compound=LEFT, font='Arial 12', padx= 10, command=self.fechar_programa)
        btn_sair.place(x=200, y=450, width=140, height=40)

        # manter a tela em loop
        janela.mainloop()
    

    def verificar_login(self, janela):
        """Método para verificar login"""
        
        # pegando as dados das entry
        login = self.txt_login.get()
        senha = self.txt_senha.get()

        # verificar credencial
        dados_login = verificar_login(login)

        if dados_login:
            if login == dados_login[0] and senha == dados_login[1]:
                mg.showinfo('Sucesso', f'Bem vindo {login}!')
                self.realizar_login(janela)
            else:
                mg.showerror('Error', 'Senha inválida!')
        else:
            mg.showerror('Error', 'Funcionário não encontrado!')


    def realizar_login(self, janela):
        """Método para mudar de tela"""
       
        Tk(TelaPrincipal(janela))


    def fechar_programa(self):
            """Método para fechar a janela do programa"""

            exit()


if __name__ == '__main__':
    TelaLogin()