from tkinter import *
from tkinter import ttk
from utils.centralizar_frame import centralizar
from utils.config_imagens import configurar_imagem
from control.controle_servico import exibir_servico_preco

class Servico:
    """Classe principal"""

    def __init__(self, master):
        """Método construtor da classe"""
        
        # criação e configurações da janela
        janela = Toplevel(master)
        janela.transient(master)
        janela.title('Serviços')
        janela_largura = 455
        janela_altura = 350
        janela.maxsize(janela_largura, janela_altura)
        janela.minsize(janela_largura, janela_altura)

        # centralizar janela
        centralizar(janela, janela_largura, janela_altura)

        # configurando imagem
        img_sair = configurar_imagem('imagens\\sair.png', 25, 25)

        # adicionando button
        btn_sair = Button(janela, image= img_sair, text='Sair', compound=LEFT,
        padx=10, command=lambda: self.fechar_janela(janela))
        btn_sair.place(x=135, y=300, width=180, height=40)

        # treeview na janela
        # colunas do treeview
        colunas = ['#1', '#2']
        # scrollbar
        tree_scrollbar = Scrollbar(janela)
        tree_scrollbar.place(x=430, y=10, height=270)
        # treeview na janela 
        tree = ttk.Treeview(janela, columns=colunas, show='headings', yscrollcommand=tree_scrollbar.set)
        tree.place(x=10, y=10, width=420, height=270)
        # definindo os headings
        tree.heading('#1', text='SERVIÇO')
        tree.heading('#2', text='VALOR')
        # definindo as colunas
        tree.column("#1", stretch=NO, minwidth=274, width=274, anchor='center')
        tree.column("#2", stretch=NO, minwidth=144, width=144, anchor='center')
        # treeview tag
        tree.tag_configure('even', foreground='black', background='lightblue')
        tree.tag_configure('odd', foreground='black', background='white')
        # configurando scrollbar
        tree_scrollbar.config(command=tree.yview)

        # mostrar dados treeview
        self.mostrar_dados_treeview(tree)

        # janela em loop
        janela.mainloop()
    

    def mostrar_dados_treeview(self, tree):
        """Método para mostrar os dados do banco de dados na treeview"""
        
        count = 0
        lista_servico = exibir_servico_preco()

        for linha in lista_servico:
            if count % 2 == 0:
                tree.insert('', 'end', values=(linha[0], linha[1]), tags=('even',))
            else:
                tree.insert('', 'end', values=(linha[0], linha[1]), tags=('odd',))
            count +=1


    def fechar_janela(self, frame):
        """Método para fechar a janela"""

        frame.destroy()


if __name__ == '__main__':
    Servico()