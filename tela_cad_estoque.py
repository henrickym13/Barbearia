from tkinter import *
from utils.centralizar_frame import centralizar
from utils.config_imagens import configurar_imagem
from control.controle_estoque import cadastrar_produto


class CadastroProduto:
    """Classe principal"""

    def __init__(self, master):
        """Método construtor da classe"""

        # configurações da janela
        janela = Toplevel(master)
        janela.transient(master)
        janela.title('Cadastro de Produto')
        janela_largura = 470
        janela_altura = 110
        janela.maxsize(janela_largura, janela_altura)
        janela.minsize(janela_largura, janela_altura)

        # centralizar janela
        centralizar(janela, janela_largura, janela_altura)

        # adicionar e configurar icones
        img_cadastro = configurar_imagem('imagens\\salvar.png', 25, 25)
        img_limpar = configurar_imagem('imagens\\apagar.png', 25, 25)
        img_sair = configurar_imagem('imagens\\sair.png', 25, 25)
        
        # adicionando labels na tela
        lbl_prod_nome = Label(janela, text='Produto:')
        lbl_prod_nome.place(x=10, y=20)
        lbl_prod_qtd = Label(janela, text='Quantidade:')
        lbl_prod_qtd.place(x=315, y=20)

        # adicionando entry na tela
        self.txt_prod_nome = Entry(janela)
        self.txt_prod_nome.place(x=75, y=20, width=165)
        self.txt_prod_qtd = Entry(janela)
        self.txt_prod_qtd.place(x=400, y=20, width=60)

        # adicionando buttons ao tela
        btn_cadastrar = Button(janela, image=img_cadastro, text='Cadastrar',
        compound=LEFT, padx=10, command=self.pegar_informacoes_campos)
        btn_cadastrar.place(x=10, y=60, width=140, height=40)

        btn_limpar = Button(janela, image=img_limpar, text='Limpar',
        compound=LEFT, padx=10, command=self.limpar_campos)
        btn_limpar.place(x=165, y=60, width=140, height=40)

        btn_sair = Button(janela, image=img_sair, text='Sair', 
        compound=LEFT, padx=10, command=lambda: self.fechar_janela(janela))
        btn_sair.place(x=320, y=60, width=140, height=40)

        # manter a tela em loop
        janela.mainloop()


    def pegar_informacoes_campos(self):
        """Método para pegar as informações da entry"""

        # chamada da função de outro pacote
        cadastrar_produto(self.txt_prod_nome.get(), self.txt_prod_qtd.get())
        
        # chamar função para limpar os campos
        self.limpar_campos()


    def limpar_campos(self):
        """Método para limpar os campos preenchidos"""

        self.txt_prod_nome.delete(0, END)
        self.txt_prod_qtd.delete(0, END)

    
    def fechar_janela(self, frame):
        """Método para fechar a janela ao pressionar o button cancelar"""

        frame.destroy()


if __name__ == '__main__':
    CadastroProduto()