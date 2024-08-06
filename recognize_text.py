import cv2
import pytesseract
from PIL import Image
import os

# Define o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Diretório das imagens de entrada
input_dir = 'inputs'
# Diretório do texto de sa'ida
output_dir = 'output'

# Cria o diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Iterar sobre as imagens no diretório de entrada
for image_name in os.listdir(input_dir):
    image_path = os.path.join(input_dir, image_name)

    # Ler a imagem
    image = cv2.imread(image_path)

    # Converter a imagem para cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar OCR na imagem
    text = pytesseract.image_to_string(gray_image)

    # Salvar o texto em um arquivo .txt
    output_path = os.path.join(output_dir, f"{os.path.splitext(image_name)[0]}.txt")
    with open(output_path, 'w') as file:
        file.write(text)

    print(f"Texto reconhecido e salvo em {output_path}")



