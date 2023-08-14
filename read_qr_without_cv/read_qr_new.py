import os
import tempfile
import numpy as np
from PIL import Image

with open('..\..\img.png', "rb") as image:
    # Чтение данных изображения в виде байтов
    f = image.read()

# Создаем временный файл и записываем в него байты изображения
with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
    temp_filename = temp_file.name
    temp_file.write(f)

try:
    # Преобразование изображения в массив цветов пикселей
    # Без чёрно-белого фильтра!
    im = Image.open('..\..\img.png')
    p = np.array(im)
    print(len(p))    # 412
    print(len(p[0])) # 1117
finally:
    os.remove(temp_filename)