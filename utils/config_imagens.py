from PIL import Image, ImageTk

def configurar_imagem(imagem, largura, altura):
    """Função para configurar imagem"""

    imagem_icone = imagem
    img_icone = Image.open(imagem_icone)
    img_icone.thumbnail((largura, altura))
    photo_icone = ImageTk.PhotoImage(img_icone)
    
    return photo_icone


def imagem_conf(imagem, largura, altura):

    imagem.thumbnail((largura, altura))
    photo_icone = ImageTk.PhotoImage(imagem)
    return photo_icone