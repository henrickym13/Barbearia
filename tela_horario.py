from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from utils.centralizar_frame import centralizar
from utils.config_imagens import configurar_imagem
from control.controle_agendamento import exibir_agendamentos, exibir_agendamentos_funcionario
from control.controle_funcionario import listar_funcionarios


class TelaHorario:
    """classe principal"""

    def __init__(self, master):
        """método construtor da classe"""

        # criação e configurações da janela
        janela = Toplevel(master)
        janela.transient(master)
        janela.title('Horário')
        janela_largura = 630
        janela_altura = 450
        janela.maxsize(janela_largura, janela_altura)
        janela.minsize(janela_largura, janela_altura)

        # centralizar a janela na tela
        centralizar(janela, janela_largura, janela_altura)

        # configurações de imagem
        img_sair = configurar_imagem('imagens\\sair.png', 25, 25)

        # add componentes na janela
        # label
        lbl_data = Label(janela, text='Selecione a data')
        lbl_data.place(x=85, y=15)
        lbl_filtro = Label(janela, text='filtrar por Barbeiro')
        lbl_filtro.place(x=465, y=15)

        # adicionado um dateEntry na tela e pegando a data atual
        data_hoje = datetime.now()
        self.calendario = DateEntry(janela, year=data_hoje.year,
        month=data_hoje.month, day=data_hoje.day)
        self.calendario.place(x=10, y=50, width=250)

        # adicionando combobox no frame
        self.ccbox_filtro = ttk.Combobox(janela, state='readonly',
        postcommand=self.exibir_funcionarios_ccbox)
        self.ccbox_filtro.place(x=445, y=50)
        self.ccbox_filtro.bind("<<ComboboxSelected>>", self.exibir_dados_filtrado_treeview)

        # adicionando Button a janela
        btn_sair = Button(janela, image= img_sair, text='Sair', compound=LEFT,
        padx=10, command=lambda: self.fechar_janela(janela))
        btn_sair.place(x=210, y=390, width=180, height=40)

        # treeview na janela
        # colunas do treeview
        colunas = ['#1', '#2', '#3', '#4', '#5']
        # scrollbar
        tree_scrollbar = Scrollbar(janela)
        tree_scrollbar.place(x=592, y=100, height=270)
        # treeview na janela 
        self.tree = ttk.Treeview(janela, columns=colunas, show='headings')
        self.tree.place(x=10, y=100, width=580, height=270)
        # definindo os headings
        self.tree.heading('#1', text='HORÁRIO')
        self.tree.heading('#2', text='BARBEIRO')
        self.tree.heading('#3', text='CLIENTE')
        self.tree.heading('#4', text='SERVIÇOS')
        self.tree.heading('#5', text='VALOR')
        # definindo as colunas
        self.tree.column("#1", stretch=NO, minwidth=100, width=80, anchor='center')
        self.tree.column("#2", stretch=NO, minwidth=100, width=125, anchor='center')
        self.tree.column("#3", stretch=NO, minwidth=100, width=120, anchor='center')
        self.tree.column("#4", stretch=NO, minwidth=100, width=165, anchor='center')
        self.tree.column("#5", stretch=NO, minwidth=100, width=88, anchor='center')
        # treeview tag
        self.tree.tag_configure('even', foreground='black', background='lightblue')
        self.tree.tag_configure('odd', foreground='black', background='white')
        # configurando scrollbar
        tree_scrollbar.config(command=self.tree.yview)
        # exibir os dados da treeview
        self.exibir_agendamento_dia()

        # manter a tela em loop
        janela.mainloop()
    

    def exibir_agendamento_dia(self):
        """Método para mostrar todos os agendamentos do dia
        ao abrir a janela"""

        # formatar formato de data
        data_formatada = self.formatar_data()

        # chamada do método para exibir na treeview
        agendamento = exibir_agendamentos(data_formatada)
        self.exibir_dados_treeview(agendamento)


    def exibir_dados_treeview(self, lista_agendamento):
        """Método para mostrar os dados do banco de dados na treeview"""
        
        count = 0
        # chamada dos métodos
        self.limpar_treeview()
    
        for linha in lista_agendamento:
            if count % 2 == 0:
                self.tree.insert('', 'end', values=(linha[0], linha[1],
                 linha[2], linha[3], linha[4]),tags=('even',))
            else:
                self.tree.insert('', 'end', values=(linha[0], linha[1],
                linha[2], linha[3], linha[4]), tags=('odd',))
            count +=1


    def limpar_treeview(self):
        """Método para apagar os dados da treeview"""

        valor = self.tree.get_children()
        for item in valor:
            self.tree.delete(item)

    
    def exibir_dados_filtrado_treeview(self, event):
        """Exibir na treeview os dados filtrado pelo usuario"""

        data = self.formatar_data()
        funcionario = self.ccbox_filtro.get()

        if data and funcionario == 'Todos':
            self.exibir_agendamento_dia()
        else:
            # chamada de função 
            dados = exibir_agendamentos_funcionario(funcionario, data)

            # passando os dados para treeview
            self.exibir_dados_treeview(dados)
    

    def exibir_funcionarios_ccbox(self):
        """Método para exibir os funcionarios"""
        
        funcionarios = listar_funcionarios()
        nome_funcionarios = []

        # usando for para pegar apenas os nomes
        for nome in funcionarios:
            nome_funcionarios.append(nome[0])
        
        # extende a lista
        nome_funcionarios.extend(['Todos'])

        # passar os dados para a ccbox funcionario
        self.ccbox_filtro.configure(values=nome_funcionarios)


    def formatar_data(self):
        """Método para pegar a data do dateentry e formatar"""

        data = self.calendario.get_date()
        data_formatada = datetime.strftime(data, '%d/%m/%Y')
        return str(data_formatada)


    def fechar_janela(self, frame):
        """Método para fechar a janela ao pressionar o button cancelar"""

        frame.destroy()


if __name__ == '__main__':
    TelaHorario()