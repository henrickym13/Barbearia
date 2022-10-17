def centralizar(janela, largura, altura):
    """Função para centralizar janela"""

    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (largura/2))
    y_cordinate = int((screen_height/2) - (altura/2))
    janela.geometry("{}x{}+{}+{}".format(
        largura, altura, x_cordinate, y_cordinate))