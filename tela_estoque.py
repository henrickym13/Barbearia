from tkinter import *
from tkinter import ttk
from utils.centralizar_frame import centralizar
from tela_cad_estoque import CadastroProduto
from tela_atualizar_estoque import AtualizarProduto
from utils.config_imagens import configurar_imagem
from control.controle_estoque import exibir_produtos, pesquisar_produto


class Estoque:
    """Classe principal"""

    def __init__(self, master):
        """Método construtor da classe"""

        # configurações da tela
        janela = Toplevel(master)
        janela.transient(master)
        janela.title('Estoque')
        janela_largura = 400
        janela_altura = 560
        janela.maxsize(janela_largura, janela_altura)
        janela.minsize(janela_largura, janela_altura)

        # chamada da função centralizar
        centralizar(janela, janela_largura, janela_altura)

        # configurando imagens
        img_cadastro = configurar_imagem('imagens\\registro.png', 25, 25)
        img_sair = configurar_imagem('imagens\\sair.png', 25, 25)

        # adicionando labels no frame
        lbl_pesquisar_nome = Label(janela, text='Produto:')
        lbl_pesquisar_nome.place(x=15, y=10)
        lbl_filtro = Label(janela, text='Filtro:')
        lbl_filtro.place(x=95, y=50)

        # adicionando entry no frame
        self.txt_pesquisar_nome = Entry(janela)
        self.txt_pesquisar_nome.place(x=80, y=10, width=140)

        # adicionando buttons ao frame
        btn_pesquisar = Button(janela, text='Pesquisar Produto',
        command=self.exibir_produto_pesquisado)
        btn_pesquisar.place(x= 240, y=7, width=140)

        btn_cadastrar_prod = Button(janela, image=img_cadastro, 
        text='Cadastrar novo produto', compound=LEFT, padx=10,
        command=lambda: CadastroProduto(janela))
        btn_cadastrar_prod.place(x=10, y=450, width=180, height=40)

        btn_atualizar_prod = Button(janela, image=img_cadastro, 
        text='Atualizar quantidade', compound=LEFT, padx=10,
        command=lambda: AtualizarProduto(janela))
        btn_atualizar_prod.place(x=210, y=450, width=180, height=40)

        btn_sair = Button(janela, image=img_sair, text='Sair',
        compound=LEFT, padx=10, command=lambda: self.fechar_janela(janela))
        btn_sair.place(x=110, y=510, width=180, height=40)

        # adicionando combobox no frame
        self.ccbox_filtro = ttk.Combobox(janela, state='readonly', values=['Todos'])
        self.ccbox_filtro.place(x=135, y=50)
        self.ccbox_filtro.bind("<<ComboboxSelected>>", self.opcao_cbox)

        # treeview na janela
        # colunas do treeview
        colunas = ['#1', '#2']
        # treeview na janela 
        self.tree = ttk.Treeview(janela, columns=colunas, show='headings')
        self.tree.place(x=10, y=100, width=380, height=320)
        # definindo os headings
        self.tree.heading('#1', text='PRODUTO')
        self.tree.heading('#2', text='QUANTIDADE')
        # definindo as column
        self.tree.column("#1", stretch=NO, minwidth=100, width=189, anchor='center')
        self.tree.column('#2', stretch=NO, minwidth=100, width=189, anchor='center')
        # stripped treeview
        self.tree.tag_configure('even', foreground='black', background='lightblue')
        self.tree.tag_configure('odd', foreground='black', background='white')

        # mostrar dados treeview
        self.mostrar_dados_treeview()

        # manter o frame em loop
        janela.mainloop()


    def mostrar_dados_treeview(self):
        """Método para mostrar os dados do banco de dados na treeview"""
        
        count = 0
        lista_produto = exibir_produtos()

        # chamar método para limpar treeview
        self.limpar_treeview()

        for linha in lista_produto:
            if count % 2 == 0:
                self.tree.insert('', 'end', values=(linha[0], linha[1]), tags=('even',))
            else:
                self.tree.insert('', 'end', values=(linha[0], linha[1]), tags=('odd',))
            count +=1    


    def mostrar_dados_treeview_produto_especifico(self, lista_produto):
        """Método para mostrar os dados de um produto pesquisado"""
        
        # limpar treeview
        self.limpar_treeview()

        # exibir o produto na treeview
        for linha in lista_produto:
            self.tree.insert('', 'end', values=(linha[0], linha[1]), tags=('even',)) 


    def limpar_treeview(self):
        """Método para apagar os dados da treeview"""

        valor = self.tree.get_children()
        for item in valor:
            self.tree.delete(item)
    

    def opcao_cbox(self, event):
        """Método para aplicar  filtro na treeview a partir da escolha no
        cbox"""
        
        # pegando a string do combobox
        entrada = self.ccbox_filtro.get()

        # fazendo a verificação
        if entrada == 'Todos':
            self.limpar_treeview()
            self.mostrar_dados_treeview()


    def exibir_produto_pesquisado(self):
        """Método para encontrar produto digitado pelo usuario"""

        # chamar função de outro pacote e passar os dados para variavel
        produto = pesquisar_produto(self.txt_pesquisar_nome.get())

        # exibir na treeview o produto
        self.mostrar_dados_treeview_produto_especifico(produto)
        self.txt_pesquisar_nome.delete(0, END)


    def fechar_janela(self, frame):
        """Método para fechar a janela ao pressionar o button cancelar"""

        frame.destroy()


if __name__ == '__main__':
    Estoque()