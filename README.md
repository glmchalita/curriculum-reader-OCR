
# OCR Curriculum Reader
## Objetivo / descrição do Projeto
Leitura de curriculos utilizando OCR (Optical Character Recognition) com Python e as bibliotecas Pytesseract e OpenCV. O projeto retorna as informações: nome, objetivo, experiencia e formação.
Conferir os modelos aceitáveis do script.

## Como usar
Clone o projeto:
> cd /user/pasta<br>
> git clone https://github.com/glmchalita/opencv-nac1.git <br>
> cd opencv-nac1<br>
> dir

Instale as bibliotecas necessárias:
>  pip install -r /diretório/pasta/requirements.txt

Instale o [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (informações adicionais de como installar em seu sistema).

Configure o diretório em que foi instalar o Tesseract:
> pytesseract.pytesseract.tesseract_cmd = 'diretorio_para_seu_tesseract_executavel'

Configure o diretório em que está seu currículo, necessário estar em formato .jpg:
> img = cv2.imread('diretorio_para_seu_curriculo.jpg')

Após configurar tudo, basta iniciar o script _main.py_ e checar no seu diretório o arquivo _retorno.txt_.

### Modelos aceitáveis

* [Modelo-01](https://github.com/glmchalita/curriculum-reader-OCR/blob/master/modelos/modelo-01-exemplo.docx)