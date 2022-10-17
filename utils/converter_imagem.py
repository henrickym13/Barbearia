import base64
from PIL import Image
import io


def converter_img_em_bytes(imagem):
    """Função para converter uma imagem em bytes"""

    # abrir um arquivo no modo binario
    file = open(imagem, 'rb').read()

    # encoda o file em base64
    file = base64.b64encode(file)

    return file


def converter_bytes_em_imagem(imagem_bytes):
    """Fubção para converter bytes em imagem"""

    # decode
    data_binaria = base64.b64decode(imagem_bytes)

    # converter os bytes em uma imagem Pil
    imagem = Image.open(io.BytesIO(data_binaria))

    # exibir imagem
    return imagem


def converter_imagem(imagem):
    """função para converter imagem ja aberta"""

    # encoda o file em base64
    imagem = imagem.tobytes('xbm', 'rgb')
    file = base64.b64encode(imagem)

    return file