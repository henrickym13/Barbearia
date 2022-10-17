from tkinter import *
from tkinter import filedialog as fd
from API.api_buscar_cep import buscar_cep
from utils.centralizar_frame import centralizar
from utils.config_imagens import configurar_imagem
from control.controle_funcionario import gravar_dados_funcionario
from utils.converter_imagem import converter_img_em_bytes


class CadastroFuncionario:
    """classe principal da tela de cadastro de funcionario"""

    def __init__(self, master):
        """Método construtor"""       

        # configurações da tela
        #janela = Tk()
        janela = Toplevel(master)
        janela.transient(master)
        janela.title('Cadastro de Funcionário')
        janela_largura = 465
        janela_altura = 495
        janela.maxsize(janela_largura, janela_altura)
        janela.minsize(janela_largura, janela_altura)

        # centralizar o frame na tela
        centralizar(janela, janela_largura, janela_altura)

        # configurações das imagens
        img_gravar = configurar_imagem('imagens\\salvar.png', 25, 25)
        img_limpar = configurar_imagem('imagens\\apagar.png', 25, 25)
        img_sair = configurar_imagem('imagens\\sair.png', 25, 25)
        img_foto = configurar_imagem('imagens\\fotos.png', 25, 25)
        
        # variavel global
        self.caminho_imagem = ''

        # add as labels a tela
        lbl_nome = Label(janela, text='Nome')
        lbl_nome.place(x=10, y=10)
        lbl_cpf = Label(janela, text='CPF')
        lbl_cpf.place(x=10, y=50)
        lbl_celular = Label(janela, text='Celular')
        lbl_celular.place(x=170, y=50)
        lbl_email = Label(janela, text='E-mail')
        lbl_email.place(x=10, y=90)
        lbl_cep = Label(janela, text='CEP')
        lbl_cep.place(x=10, y=130)
        lbl_cidade = Label(janela, text='Cidade')
        lbl_cidade.place(x=10, y=170)
        lbl_uf = Label(janela, text='UF')
        lbl_uf.place(x=210, y=170)
        lbl_complemento = Label(janela, text='Complemento')
        lbl_complemento.place(x=10, y=210)
        lbl_bairro = Label(janela, text='Bairro')
        lbl_bairro.place(x=150, y=210)  
        lbl_endereco = Label(janela, text='Endereço')
        lbl_endereco.place(x=10, y=250)
        lbl_numero = Label(janela, text='Numero')
        lbl_numero.place(x=200, y=250)
        lbl_borda = Label(janela, borderwidth=2, relief="groove")
        lbl_borda.place(x=10, y=310, width=440, height=120)
        lbl_campo_usuario = Label(janela, text='Cadastro de usuário')
        lbl_campo_usuario.place(x=15, y=300)
        lbl_login_usuario = Label(janela, text='Login')
        lbl_login_usuario.place(x=80, y=330)
        lbl_senha_usuario = Label(janela, text='Senha')
        lbl_senha_usuario.place(x=80, y=360)
        lbl_confirmar_usuario = Label(janela, text='Confirmar')
        lbl_confirmar_usuario.place(x=80, y=390)

        # label para exibir imagem do funcionario
        self.lbl_foto = Label(janela, borderwidth=2, relief='groove')
        self.lbl_foto.place(x=300, y=30, width=150, height=200)

        # adicionando os campos entry a janela
        self.txt_nome = Entry(janela)
        self.txt_nome.place(x=10, y=30, width=270, height=20)
        self.txt_cpf = Entry(janela)
        self.txt_cpf.place(x=10, y=70, width=120, height=20)
        self.txt_celular = Entry(janela)
        self.txt_celular.place(x=170, y=70, width=110, height=20)
        self.txt_email = Entry(janela)
        self.txt_email.place(x=10, y=110, width=270, height=20)
        self.txt_cep = Entry(janela)
        self.txt_cep.place(x=10, y=150, width=130, height=20)
        self.txt_cidade = Entry(janela)
        self.txt_cidade.place(x=10, y=190, width=190, height=20)
        self.txt_uf = Entry(janela)
        self.txt_uf.place(x=210, y=190, width=70, height=20)
        self.txt_complemento = Entry(janela)
        self.txt_complemento.place(x=10, y=230, width=130)
        self.txt_bairro = Entry(janela)
        self.txt_bairro.place(x=150, y=230, width=130, height=20)
        self.txt_endereco = Entry(janela)
        self.txt_endereco.place(x=10, y=270, width=180)
        self.txt_numero = Entry(janela)
        self.txt_numero.place(x=200, y=270, width=80)
        self.txt_login_usuario = Entry(janela)
        self.txt_login_usuario.place(x=150, y=330, width=210, height=20)
        self.txt_senha_usuario = Entry(janela)
        self.txt_senha_usuario.place(x=150, y=360, width=210, height=20)
        self.txt_confirmar_usuario = Entry(janela)
        self.txt_confirmar_usuario.place(x=150, y=390, width=210, height=20)

        # adicionando Button a tela
        btn_salvar = Button(janela, image=img_gravar, text='Gravar Dados',
        command=self.pegar_informacoes_campos, compound=LEFT, padx=10)
        btn_salvar.place(x=10, y=440, width=130, height=40)

        btn_limpar = Button(janela, image=img_limpar, text='Limpar Campos',
        command=self.limpar_campos, compound=LEFT, padx=10)
        btn_limpar.place(x=165, y=440, width=130, height=40)

        btn_cancelar = Button(janela, image=img_sair, text='Cancelar', 
        command=lambda: self.fechar_janela(janela), compound=LEFT, padx=10)
        btn_cancelar.place(x=320, y=440, width=130, height=40)

        btn_buscar_cep = Button(janela, text='Buscar CEP',
        command=self.exibir_info_endereco)
        btn_buscar_cep.place(x=170, y=145, width=110)

        btn_buscar_foto = Button(janela, image=img_foto, text='Selecionar Foto',
        command=self.selecionar_imagem, compound=LEFT, padx=10)
        btn_buscar_foto.place(x=300, y=240, width=150, height=50)

        # manter a janela em loop
        janela.mainloop()
    

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
    

    def selecionar_imagem(self):
        """Método para selecionar a imagem"""

        # variavel global
        
        filetypes = (
            ('image files', '*.jpg'),
            ('image files', '*.png'),
            ('All files', '*.*'))

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='C:\\Users\\Henrique\\Pictures',
            filetypes=filetypes)
        
        self.exibir_imagem_lbl(filename)
        self.caminho_imagem = filename
    

    def exibir_imagem_lbl(self, caminho_imagem):
        """Método para exibir imagem na label"""

        # chamada da função
        imagem = configurar_imagem(caminho_imagem, 150, 200)
        
        self.icon = self.lbl_foto
        self.icon.image = imagem
        self.icon.configure(image=imagem)
    

    def pegar_informacoes_campos(self):
        """Método para pegar todas as informações inseridas nos campos
        de texto """

        # converter imagem em bytes
        imagem_byte = converter_img_em_bytes(self.caminho_imagem)

        # chamada de funções do outro pacote para verificar os campos
        gravar_dados_funcionario(self.txt_cpf.get(), self.txt_nome.get(),
        self.txt_celular.get(), self.txt_email.get(), self.txt_cep.get(),
        self.txt_cidade.get(), self.txt_uf.get(), self.txt_complemento.get(),
        self.txt_bairro.get(), self.txt_endereco.get(), self.txt_numero.get(),
        imagem_byte, self.txt_login_usuario.get(), self.txt_senha_usuario.get(),
        self.txt_confirmar_usuario.get())

        # depois limpar os campos
        self.limpar_campos()
    

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
    

    def fechar_janela(self, frame):
        """Método para fechar a janela ao pressionar o button cancelar"""

        frame.destroy()


if __name__ == '__main__':
    CadastroFuncionario()