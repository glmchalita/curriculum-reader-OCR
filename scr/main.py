import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('curriculo-exemplo.jpg.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)

# kernel = np.ones((1, 1), np.uint8)
# img = cv2.dilate(img, kernel, iterations=1)
# img = cv2.erode(img, kernel, iterations=1)

custom_config = '-l eng --oem 3 --psm 6'
thresh = cv2.threshold(cv2.bilateralFilter(img, 8, 10, 10), 190, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

boxes = pytesseract.image_to_data(thresh)
blocks = []
for idx, b in enumerate(boxes.splitlines()):
    if idx != 0:
        b = b.split()
        if len(b) > 11:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])

            # Prevendo sempre o nome como primeira informação
            if not blocks:
                # cv2.rectangle(img, (x, y), (x + w, h + y), (0, 0, 255), 3)
                # cv2.putText(img, str(len(blocks)), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255, 2))
                blocks.append(y)

            # Coletar coordenadas para crop de Informações Pessoais
            if 'OBJETIVO' in b[11]:
                # cv2.rectangle(img, (x, y), (x + w, h + y), (0, 0, 255), 3)
                # cv2.putText(img, str(len(blocks)), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255, 2))
                blocks.append(y)

            # Coletar coordenadas para crop de Objetivo
            if 'RESULTADOS' in b[11]:
                # cv2.rectangle(img, (x, y), (x + w, h + y), (0, 0, 255), 3)
                # cv2.putText(img, str(len(blocks)), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255, 2))
                blocks.append(y)

            # Coletar coordenadas para crop de Resultado
            if 'COMPETENCIAS' in b[11]:
                # cv2.rectangle(img, (x, y), (x + w, h + y), (0, 0, 255), 3)
                # cv2.putText(img, str(len(blocks)), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255, 2))
                blocks.append(x)
            if 'IDIOMAS' in b[11]:
                # cv2.rectangle(img, (x, y), (x + w, h + y), (0, 0, 255), 3)
                # cv2.putText(img, str(len(blocks)), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255, 2))
                blocks.append(x)
            if 'EXPERIENCIA' in b[11]:
                # cv2.rectangle(img, (x,y), (x+w, h+y), (0,0,255), 3)
                # cv2.putText(img, str(len(blocks)), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255, 2))
                blocks.append(y)

            # Coletar coordenadas para crop de Experiencia
            if 'FORMACAO' in b[11]:
                # cv2.rectangle(img, (x,y), (x+w, h+y), (0,0,255), 3)
                # cv2.putText(img, str(len(blocks)), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255, 2))
                blocks.append(y)

# Crops
pessoal = img[blocks[0]:blocks[1]]
objetivo = img[blocks[1]:blocks[2]]
resultado = img[blocks[2]:blocks[5],:blocks[3]]
competencias = img[blocks[2]:blocks[5],blocks[3]:blocks[4]]
idiomas = img[blocks[2]:blocks[5],blocks[4]:]
experiencia = img[blocks[5]:blocks[6]]
formacao = img[blocks[6]:]

crops = [pessoal, objetivo, experiencia, formacao]
with open('retorno.txt', 'a+') as f:
    for idx, val in enumerate(crops):
        preview = cv2.resize(val, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        if idx == 0:
            nome = (pytesseract.image_to_string(val)).splitlines()
            nome = f'NOME: {nome[0]}\n'
            f.write(nome)
        else:
            f.write(f'\n{pytesseract.image_to_string(preview, lang="por")}')

# cv2.imshow('Result', img)
# cv2.waitKey(0)

