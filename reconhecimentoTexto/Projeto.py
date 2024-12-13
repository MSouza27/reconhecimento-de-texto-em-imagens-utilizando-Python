import pytesseract
import numpy as np
import cv2
import re
import os
import matplotlib.pyplot as plt

from PIL import ImageFont, ImageDraw, Image
from pytesseract import Output

#Percorre todos os arquivos da pasta do projeto
projeto = ("/Users/magnosouza/PycharmProjects/VisaoComputacional/"
           "reconhecimentoTexto/Arquivos/text-recognize/Imagens/Projeto")

fonte_dir = "/Users/magnosouza/PycharmProjects/VisaoComputacional/reconhecimentoTexto/Imagens/calibri.ttf"

caminho = [os.path.join(projeto, f) for f in os.listdir(projeto)]
print(caminho)


def mostrar(img):
    fig = plt.gcf()  # buscar a figura atual
    fig.set_size_inches(20, 10)  # definindo o tamanho
    plt.axis('off')  # removendo a visualização dos eixos
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # faz a conversão de cores com o OpenCV
    plt.show()  # mostra a imagem


for imagem in caminho:
    imagem = cv2.imread(imagem)
    mostrar(imagem)

config_tesseract = "--tessdata-dir /opt/homebrew/share/tessdata"


def OCR_processa(img, config_tesseract):
    texto = pytesseract.image_to_string(img, config=config_tesseract, lang='por')
    return texto


texto_completo = ''
nome_txt = 'resultados_ocr.txt'

for imagem in caminho:  # percorre as imagens no caminho
    img = cv2.imread(imagem)
    nome_imagem = os.path.split(imagem)[-1]  # recebe os nomes e diretórios
    nome_divisao = '==================\n' + str(nome_imagem)  # divisão + nome da imagem
    texto_completo = texto_completo + nome_divisao + '\n'  # recebe o texto completo
    texto = OCR_processa(img, config_tesseract)  # passa a imagem que será usada
    texto_completo = texto_completo + texto  # concatena as duas variáveis
print(texto_completo)

# salvando em arquivo os textos das imagem
arquivo_txt = open(nome_txt, 'w+')  # a+ é para colocar no final do arquivo, w+ é para sobre escrever o arquivo
arquivo_txt.write(texto_completo + '\n')  # passa o texto que quer adicionar
arquivo_txt.close()

# Busca de Ocorrência nos textos

termo_pesquisa = 'learning'
with open(nome_txt, 'r+') as f:
    ocorrencias = [i.start() for i in re.finditer(termo_pesquisa, f.read())]

for imagem in caminho:
    img = cv2.imread(imagem)
    nome_imagem = os.path.split(imagem)[-1]
    print('====================\n' + str(nome_imagem))

    texto = OCR_processa(img, config_tesseract)

    ocorrencias = [i.start() for i in re.finditer(termo_pesquisa, texto)]

    print('Número de ocorrências para o termo: {}: {}'.format(len(ocorrencias), len(ocorrencias)))
    print('\n')

fonte_dir = '/content/text-recognize/Imagens/calibri.ttf'


def escreve_texto(texto, x, y, img, fonte_dir, cor=(50, 50, 255), tamanho=16):
    fonte = ImageFont.truetype(fonte_dir, tamanho)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y), texto, font=fonte, fill=cor)
    img = np.array(img_pil)
    return img


def caixa_texto(i, resultado, img, cor=(255, 100, 0)):
    x = resultado["left"][i]
    y = resultado["top"][i]
    w = resultado["width"][i]
    h = resultado["height"][i]

    cv2.rectangle(img, (x, y), (x + w, y + h), cor, 2)
    return x, y, img

min_conf = 0
def OCR_processa_imagem(img, termo_pesquisa, config_tesseract):
    resultado = pytesseract.image_to_data(img, config=config_tesseract, lang='por',
                                          output_type=Output.DICT)  #imagem para dados, que já fizemos anteriormente
    num_ocorrencias = 0  #inicializando como 0

    for i in range(0, len(resultado['text'])):  # vai de 0 ao tamanho do número de valores do texto
        confianca = int(resultado['conf'][i])  # qual a confiança da detecção
        if confianca > min_conf:  # se a confiança for maior que o valor mínimo, passa para a linha abaixo
            texto = resultado['text'][i]  #texto será igual ao resultado text no momento i
            if termo_pesquisa.lower() in texto.lower():  #se o termo de pesquisa estiver no texto:
                x, y, img = caixa_texto(i, resultado, img, (0, 0, 255))  # faz a caixa de bounding box
                img = escreve_texto(texto, x, y, img, fonte_dir, (50, 50, 225), 14)  #escreve o texto

                num_ocorrencias += 1  #faz a iteração no num de ocorrências e volta para o laço até acabar o texto
    return img, num_ocorrencias

