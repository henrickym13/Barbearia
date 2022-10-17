from tkinter import *
from tkinter import ttk
from API.api_buscar_cep import buscar_cep
from tela_cad_func import CadastroFuncionario
from utils.centralizar_frame import centralizar
from utils.config_imagens import configurar_imagem, imagem_conf
from control.controle_funcionario import exibir_funcionario, listar_funcionarios
from utils.converter_imagem import converter_bytes_em_imagem
from control.controle_funcionario import atualizar_dados_funcionario


class Funcionario:
    """Classe principal"""

    def __init__(self, master):
        """Método construtor"""

        # configurações da tela
        janela = Toplevel(master)
        janela.transient(master)
        janela.title('Funcionário')
        janela_largura = 765
        janela_altura = 495
        janela.maxsize(janela_largura, janela_altura)
        janela.minsize(janela_largura, janela_altura)

        # centralizar o frame na tela
        centralizar(janela, janela_largura, janela_altura)

        # configurações das imagens
        img_gravar = configurar_imagem('imagens\\salvar.png', 25, 25)
        img_limpar = configurar_imagem('imagens\\apagar.png', 25, 25)
        img_sair = configurar_imagem('imagens\\sair.png', 25, 25)
        img_cadastrar = configurar_imagem('imagens\\registro.png', 25, 25)

        # add as labels a tela
        lbl_nome = Label(janela, text='Nome')
        lbl_nome.place(x=310, y=10)
        lbl_cpf = Label(janela, text='CPF')
        lbl_cpf.place(x=310, y=50)
        lbl_celular = Label(janela, text='Celular')
        lbl_celular.place(x=470, y=50)
        lbl_email = Label(janela, text='E-mail')
        lbl_email.place(x=310, y=90)
        lbl_cep = Label(janela, text='CEP')
        lbl_cep.place(x=310, y=130)
        lbl_cidade = Label(janela, text='Cidade')
        lbl_cidade.place(x=310, y=170)
        lbl_uf = Label(janela, text='UF')
        lbl_uf.place(x=510, y=170)
        lbl_complemento = Label(janela, text='Complemento')
        lbl_complemento.place(x=310, y=210)
        lbl_bairro = Label(janela, text='Bairro')
        lbl_bairro.place(x=450, y=210)  
        lbl_endereco = Label(janela, text='Endereço')
        lbl_endereco.place(x=310, y=250)
        lbl_numero = Label(janela, text='Numero')
        lbl_numero.place(x=500, y=250)
        lbl_borda = Label(janela, borderwidth=2, relief="groove")
        lbl_borda.place(x=310, y=310, width=440, height=120)
        lbl_campo_usuario = Label(janela, text='Cadastro de usuário')
        lbl_campo_usuario.place(x=315, y=300)
        lbl_login_usuario = Label(janela, text='Login')
        lbl_login_usuario.place(x=380, y=330)
        lbl_senha_usuario = Label(janela, text='Senha')
        lbl_senha_usuario.place(x=380, y=360)
        lbl_confirmar_usuario = Label(janela, text='Confirmar')
        lbl_confirmar_usuario.place(x=380, y=390)

        # label para exibir imagem do funcionario
        self.lbl_foto = Label(janela, borderwidth=2, relief='groove')
        self.lbl_foto.place(x=600, y=30, width=150, height=200)

        # adicionando os campos entry a janela
        self.txt_nome = Entry(janela)
        self.txt_nome.place(x=310, y=30, width=270, height=20)
        self.txt_cpf = Entry(janela)
        self.txt_cpf.place(x=310, y=70, width=120, height=20)
        self.txt_celular = Entry(janela)
        self.txt_celular.place(x=470, y=70, width=110, height=20)
        self.txt_email = Entry(janela)
        self.txt_email.place(x=310, y=110, width=270, height=20)
        self.txt_cep = Entry(janela)
        self.txt_cep.place(x=310, y=150, width=130, height=20)
        self.txt_cidade = Entry(janela)
        self.txt_cidade.place(x=310, y=190, width=190, height=20)
        self.txt_uf = Entry(janela)
        self.txt_uf.place(x=510, y=190, width=70, height=20)
        self.txt_complemento = Entry(janela)
        self.txt_complemento.place(x=310, y=230, width=130)
        self.txt_bairro = Entry(janela)
        self.txt_bairro.place(x=450, y=230, width=130, height=20)
        self.txt_endereco = Entry(janela)
        self.txt_endereco.place(x=310, y=270, width=180)
        self.txt_numero = Entry(janela)
        self.txt_numero.place(x=500, y=270, width=80)
        self.txt_login_usuario = Entry(janela)
        self.txt_login_usuario.place(x=450, y=330, width=210, height=20)
        self.txt_senha_usuario = Entry(janela)
        self.txt_senha_usuario.place(x=450, y=360, width=210, height=20)
        self.txt_confirmar_usuario = Entry(janela)
        self.txt_confirmar_usuario.place(x=450, y=390, width=210, height=20)

        # adicionando Buttons
        btn_salvar = Button(janela, image=img_gravar, text='Atualizar Dados',
        compound=LEFT, padx=10, command=lambda: self.pegar_informacoes_campos())
        btn_salvar.place(x=310, y=440, width=130, height=40)

        btn_limpar = Button(janela, image= img_limpar, text='Limpar Campos',
        compound=LEFT, padx=10, command=lambda: self.limpar_campos())
        btn_limpar.place(x=465, y=440, width=130, height=40)

        btn_cancelar = Button(janela, image=img_sair, text='Sair', 
        command=lambda: self.fechar_janela(janela), compound=LEFT, padx=10)
        btn_cancelar.place(x=620, y=440, width=130, height=40)

        btn_buscar_cep = Button(janela, text='Buscar CEP',
        command=self.exibir_info_endereco)
        btn_buscar_cep.place(x=470, y=145, width=110)

        btn_cadastrar_func = Button(janela, image=img_cadastrar,
        text='Cadastrar novo funcionário',
        command= lambda: self.abrir_janela_cadastro(janela), compound=LEFT, padx=10)
        btn_cadastrar_func.place(x=10, y=440, width=280, height=40)

        # treeview na janela
        # colunas do treeview
        colunas = ['#1', '#2']
        self.tree = ttk.Treeview(janela, columns=colunas, show='headings')
        self.tree.place(x=10, y=30, width=280, height=400)
        # definindo os headings
        self.tree.heading('#1', text='NOME')
        self.tree.heading('#2', text='CPF')
        # definindo column
        self.tree.column("#1", stretch=NO, minwidth=139, width=139, anchor='center')
        self.tree.column("#2", stretch=NO, minwidth=139, width=139, anchor='center')
        # treeview tag
        self.tree.tag_configure('even', foreground='black', background='lightblue')
        self.tree.tag_configure('odd', foreground='black', background='white')
        # exibir dados
        self.mostrar_dados_treeview()
        self.tree.bind("<<TreeviewSelect>>", self.treeview_selecionado)

        # manter a janela em loop
        janela.mainloop()
    
    
    def mostrar_dados_treeview(self):
        """Método para mostrar os dados do banco de dados na treeview"""
        
        count = 0
        lista_servico = listar_funcionarios()

        for linha in lista_servico:
            if count % 2 == 0:
                self.tree.insert('', 'end', values=(linha[0], linha[1]), tags=('even',))
            else:
                self.tree.insert('', 'end', values=(linha[0], linha[1]), tags=('odd',))
            count +=1


    def treeview_selecionado(self, event):
        """Método para pegar o valor selecionado na treeview
        pelo mouse"""
        global cpf
        lista = []
        for item in self.tree.selection():
            item_texto = self.tree.item(item)
            cpf = item_texto['values'][1]
        
        # enviando a variavel cpf para o método
        self.limpar_campos()
        lista = exibir_funcionario(cpf)
        self.preencher_campos(lista)


    def limpar_treeview(self):
        """Método para apagar os dados da treeview"""

        valor = self.tree.get_children()
        for item in valor:
            self.tree.delete(item)


    def abrir_janela_cadastro(self, janela):
        """Método para abrir janela de cadastro"""

        # chamada da classe
        CadastroFuncionario(janela)

        # atualizar a treeview logo apos cadastro
        #self.limpar_treeview()
        self.mostrar_dados_treeview()


    def preencher_campos(self, lista_funcionario):
        """Método para preencher os campos com os dados do cliente"""

        # enviando os dados para os entry
        self.txt_cpf.insert(0, lista_funcionario[0])
        self.txt_nome.insert(0, lista_funcionario[1])
        self.txt_celular.insert(0, lista_funcionario[2])
        self.txt_email.insert(0, lista_funcionario[3])
        self.txt_cep.insert(0, lista_funcionario[4])
        self.txt_cidade.insert(0, lista_funcionario[5])
        self.txt_uf.insert(0, lista_funcionario[6])
        self.txt_complemento.insert(0, lista_funcionario[7])
        self.txt_bairro.insert(0, lista_funcionario[8])
        self.txt_endereco.insert(0, lista_funcionario[9])
        self.txt_numero.insert(0, lista_funcionario[10])
        self.txt_login_usuario.insert(0, lista_funcionario[12])
        self.txt_senha_usuario.insert(0, lista_funcionario[13])
        self.txt_confirmar_usuario.insert(0, lista_funcionario[13])

        # converter o byte em imagem e configurar
        self.img_byte = lista_funcionario[11]
        img_funcionario = converter_bytes_em_imagem(lista_funcionario[11])
        foto_funcionario = imagem_conf(img_funcionario, 150, 200)

        # passando imagem para label
        self.icon = self.lbl_foto
        self.icon.image = foto_funcionario
        self.icon.configure(image=foto_funcionario)


    def pegar_informacoes_campos(self):
        """Método para pegar todas as informações inseridas nos campos
        de texto """

        # chamada de funções do outro pacote para verificar os campos
        atualizar_dados_funcionario(self.txt_cpf.get(), self.txt_nome.get(),
        self.txt_celular.get(), self.txt_email.get(), self.txt_cep.get(),
        self.txt_cidade.get(), self.txt_uf.get(), self.txt_complemento.get(),
        self.txt_bairro.get(), self.txt_endereco.get(), self.txt_numero.get(),
        self.txt_login_usuario.get(), self.txt_senha_usuario.get(),
        self.txt_confirmar_usuario.get())

        # depois limpar os campos
        self.limpar_campos()
        
        # atualizar a treview
        self.limpar_treeview()
        self.mostrar_dados_treeview()


    def limpar_campos(self):
        """Método para limpar os campos preenchidos"""

        self.txt_nome.delete(0, END)
        self.txt_celular.delete(0, END)
        self.txt_cpf.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_cep.delete(0, END)
        self.txt_uf.delete(0, END)
        self.txt_cidade.delete(0, END)
        self.txt_bairro.delete(0, END)
        self.txt_endereco.delete(0, END)
        self.txt_complemento.delete(0, END)
        self.txt_numero.delete(0, END)
        self.txt_login_usuario.delete(0,END)
        self.txt_senha_usuario.delete(0, END)
        self.txt_confirmar_usuario.delete(0, END)

        # trocando a imagem
        # passando imagem para label
        ft_usuario = 'imagens\\usuario.png'
        imagem = configurar_imagem(ft_usuario, 150, 200)
        self.icon = self.lbl_foto
        self.icon.image = imagem
        self.icon.configure(image=imagem)
    

    def exibir_imagem_lbl(self, caminho_imagem):
        """Método para exibir imagem na label"""

        # configurando tamanho da imagem
        imagem = configurar_imagem(caminho_imagem, 150, 200)

        # passando imagem para label
        self.icon = self.lbl_foto
        self.icon.image = imagem
        self.icon.configure(image=imagem)
    

    def exibir_info_endereco(self):
        """Método para exibir as informações de endereço"""

        # chamada da função 
        cep = buscar_cep(self.txt_cep.get())

        # passando as informações paras os campos
        self.txt_uf.insert(0, cep['uf'])
        self.txt_cidade.insert(0, cep['localidade'])
        self.txt_bairro.insert(0, cep['bairro'])
        self.txt_endereco.insert(0, cep['logradouro'])
        self.txt_complemento.insert(0, cep['complemento'])
    

    def fechar_janela(self, frame):
        """Método para fechar a janela ao pressionar o button cancelar"""

        frame.destroy()


if __name__ == '__main__':
    Funcionario()