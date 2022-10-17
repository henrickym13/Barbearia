from tkinter import *
from tkinter import messagebox as mg
from datetime import datetime
from time import strftime
from tela_funcionario import Funcionario
from tela_estoque import Estoque
from tela_horario import TelaHorario
from tela_agendamento import Agendamento
from tela_servicos import Servico
from utils.centralizar_frame import centralizar
from utils.config_imagens import configurar_imagem


class TelaPrincipal:
    """classe da tela principal"""

    def __init__(self, master):
        """Método construtor da classe"""

        # configurações da tela
        janela = Toplevel(master)
        janela.transient(master)
        janela.title('Barbearia')
        janela_largura = janela.winfo_screenwidth()
        janela_altura = janela.winfo_screenheight()
        janela.maxsize(janela_largura, janela_altura)
        janela.minsize(janela_largura, janela_altura)
        janela.state('zoomed')

        # centralizar o frame na tela
        centralizar(janela, janela_largura, janela_altura)

        # configurando imagens
        img_icone = configurar_imagem('imagens\\teste.webp', 980, 500)
        img_agenda = configurar_imagem('imagens\\agenda.png', 50, 50)
        img_horario = configurar_imagem('imagens\\horarios.png', 50, 50)
        img_estoque = configurar_imagem('imagens\\estoque-pronto.png', 50, 50)
        img_servico = configurar_imagem('imagens\\salvando.png', 50, 50)
        img_funcionario = configurar_imagem('imagens\\funcionario.png', 50, 50)
        img_sair = configurar_imagem('imagens\\sair.png', 50, 50)
        
        # adicionado labels na tela
        # label com imagem 
        lbl_img_barber = Label(janela, image=img_icone)
        lbl_img_barber.place(x=370, y=10, width=980, height=500)

        # label com data e hora
        self.lbl_data_hora = Label(janela,background='black',
         font='Arial 42', fg='white')
        self.lbl_data_hora.place(x=370, y=520, width=980, height=175)
        self.horario()

        # adicionando os buttons
        btn_agendamento = Button(janela, image=img_agenda,text='Agendamento',
         compound=LEFT, font='Arial 20', padx=10, command=
         lambda: Agendamento(janela))
        btn_agendamento.place(x=10, y=10, width=350, height=90)

        btn_horario = Button(janela, image=img_horario, text='Horário',
         compound=LEFT, font='Arial 20', padx=10, command=
         lambda:TelaHorario(janela))
        btn_horario.place(x=10, y=110, width=350, height=90)

        btn_funcionario = Button(janela, image=img_funcionario, text='Funcionarios',
         compound=LEFT, font='Arial 20', padx=10, command=lambda:Funcionario(janela))
        btn_funcionario.place(x=10, y=210, width=350, height=90)

        btn_estoque = Button(janela, image=img_estoque, text='Estoque',
         compound=LEFT, font='Arial 20', padx=10, command=lambda: Estoque(janela))
        btn_estoque.place(x=10, y=310, width=350, height=90)

        btn_servico = Button(janela, image=img_servico, text='Serviços',
         compound=LEFT, font='Arial 20', padx=10, command=lambda: Servico(janela))
        btn_servico.place(x=10, y=410, width=350, height=90)

        btn_sair = Button(janela, image=img_sair, text='Sair', compound=LEFT,
        font='ARIAL 20', padx=10, command=self.fechar_janela)
        btn_sair.place(x=10, y=510, width=350, height=90)
        
        # manter a tela em loop
        janela.mainloop()
    

    def data_extenso(self):
        """Função para exibir a data por extenso"""

        # montando uma list com os meses e a semana
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
        'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira',
        'Sexta-feira', 'Sábado', 'Domingo']

        # pegando a data atual
        data_e_hora = datetime.now()

        return f'{semana[data_e_hora.weekday()]}, {data_e_hora.day} de '+\
        f'{meses[data_e_hora.month-1]} de {data_e_hora.year}\n'
    

    def horario(self):
        """Método para exibir horario na label"""

        # chamada de método
        data = self.data_extenso()
        string = strftime('%H:%M:%S %p')
        self.lbl_data_hora.config(text = data + string)
        self.lbl_data_hora.after(1000, self.horario)
    

    def fechar_janela(self):
        """Método para exibir mensagem se o usuario deseja sair"""

        mensagem = mg.askquestion(title='Sair do Aplicativo', 
        message='Tem certeza que deseja sair do aplicativo?')
        
        # validando escolha do usuario
        if mensagem == 'yes':
            exit()
    
        
if __name__ == "__main__":
    TelaPrincipal()