from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from utils.centralizar_frame import centralizar
from utils.config_imagens import configurar_imagem
from control.controle_funcionario import listar_funcionarios
from control.controle_servico import exibir_servico_preco
from control.controle_agendamento import (exibir_valor_servico, exibir_horario_marcado_func,
realizar_agendamento)


class Agendamento:
    """classe principal"""

    def __init__(self, master):
        """método construtor da classe"""

        # criação e configurações da janela
        janela = Toplevel(master)
        janela.transient(master)
        janela.title('Agendamento')
        janela_largura = 430
        janela_altura = 340
        janela.maxsize(janela_largura, janela_altura)
        janela.minsize(janela_largura, janela_altura)

        # centralizar a janela na tela
        centralizar(janela, janela_largura, janela_altura)

        # adicionando e configurando imagens
        img_agendar = configurar_imagem('imagens\\agenda.png', 25, 25)
        img_limpar = configurar_imagem('imagens\\apagar.png', 25, 25)
        img_sair = configurar_imagem('imagens\\sair.png', 25, 25)

        # variavel global
        self.valor_total = 0
        # adicionando componentes a janela
        # Label
        lb_data = Label(janela, text='Dia: ').place(x=10, y=10)
        lb_funcionario = Label(janela, text='Funcionario:').place(x=10, y=50)
        lb_horario = Label(janela, text='Horário:').place(x=10, y=90)
        lb_cliente = Label(janela, text='Cliente:').place(x=10, y=130)
        lb_servico = Label(janela, text='Serviços').place(x=10, y=170)
        self.lb_valor = Label(janela, font='14')
        self.lb_valor.place(x=145, y=215, width=140, height=50)
        

        # adicionado um dateEntry na tela e pegando a data atual
        data_hoje = datetime.now()
        self.calendario = DateEntry(janela, year=data_hoje.year,
        month=data_hoje.month, day=data_hoje.day, mindate=data_hoje)
        self.calendario.place(x=90, y=10, width=250)

        # adicionando combobox no frame
        self.ccbox_funcionario = ttk.Combobox(janela, state='readonly',
        postcommand=self.exibir_funcionarios_ccbox)
        self.ccbox_funcionario.place(x=90, y=50)
        self.ccbox_horario = ttk.Combobox(janela, state='readonly')
        self.ccbox_horario.place(x=90, y=90)
        self.ccbox_servicos = ttk.Combobox(janela, state='readonly',
        postcommand=self.exibir_servicos_ccbox)
        self.ccbox_servicos.place(x=90, y=170, width=330)

        # event nas combobox
        self.ccbox_funcionario.bind("<<ComboboxSelected>>", self.mostra_horario_disponivel)
        self.ccbox_servicos.bind("<<ComboboxSelected>>", self.exibir_valor_servico)

        # adicionando entry
        self.txt_cliente = Entry(janela)
        self.txt_cliente.place(x=90, y=130, width=220, height=20)

        # adicionando buttons
        btn_agendar = Button(janela, image=img_agendar, text='Agendar',
        compound=LEFT, padx=10, command=self.pegar_informacoes_campos)
        btn_agendar.place(x=10, y=290, width=120, height=40)
        btn_limpar = Button(janela, image=img_limpar, text='Limpar campos',
        compound=LEFT, padx=10, command=self.limpar_campos)
        btn_limpar.place(x=145, y=290, width=140, height=40)
        btn_sair = Button(janela, image=img_sair, text='Sair',
        compound=LEFT, padx=10, command=lambda: self.fechar_janela(janela))
        btn_sair.place(x=300, y=290, width=120, height=40)

        # manter a tela em loop
        janela.mainloop()


    def exibir_funcionarios_ccbox(self):
        """Método para exibir os funcionarios"""
        
        funcionarios = listar_funcionarios()
        nome_funcionarios = []

        # usando for para pegar apenas os nomes
        for nome in funcionarios:
            nome_funcionarios.append(nome[0])

        # passar os dados para a ccbox funcionario
        self.ccbox_funcionario.configure(values=nome_funcionarios)
    

    def exibir_servicos_ccbox(self):
        """Método para exibir os funcionarios"""
        
        servicos_preco = exibir_servico_preco()
        servicos = []

        # usando for para exibir apenas os serviços
        for servico in servicos_preco:
            servicos.append(servico[0])

        # passar os dados para a ccbox serviços
        self.ccbox_servicos.configure(values=servicos)
    

    def exibir_valor_servico(self, event):
        """Exibir na label valor do serviço selecionado"""

        preco = exibir_valor_servico(self.ccbox_servicos.get())
        self.valor_total = float(preco)
        self.lb_valor.configure(text=f'Valor Total:\n R$:{preco}', anchor='center')
       

    def mostra_horario_disponivel(self, event):
        """Método para exibir horarios disponiveis"""
        
        # chamada do método para formatar a data
        data_formatada = self.formatar_data()

        # chamada da função para obter todos os horarios disponiveis
        horario = exibir_horario_marcado_func(self.ccbox_funcionario.get(),
        data_formatada)

        # limpar a seleção da combobox e enviar a nova lista de horarios
        self.ccbox_horario.set(' ')
        self.ccbox_horario.config(values=horario)


    def formatar_data(self):
        """Método para pegar a data do dateentry e formatar"""

        data = self.calendario.get_date()
        data_formatada = datetime.strftime(data, '%d/%m/%Y')
        return data_formatada


    def pegar_informacoes_campos(self):
        """Método para pegar as informações dos campos preenchidos"""

        # converter data
        data_convertida = self.formatar_data()

        # chamar função para gravar os dados no banco de dados
        realizar_agendamento(data_convertida, self.ccbox_funcionario.get(),
        self.ccbox_horario.get(), self.txt_cliente.get(),
        self.ccbox_servicos.get(), float(self.valor_total))

        # limpar os campos depois de gravar os dados
        self.limpar_campos()


    def limpar_campos(self):
        """Método para limpar os campos"""

        self.ccbox_funcionario.set(' ')
        self.ccbox_horario.set(' ')
        self.ccbox_servicos.set(' ')
        self.txt_cliente.delete(0, END)
        self.lb_valor.configure(text=' ')
        self.calendario.delete(0, END)


    def fechar_janela(self, frame):
        """Método para fechar a janela ao pressionar o button cancelar"""

        frame.destroy()


if __name__ == '__main__':
    Agendamento()