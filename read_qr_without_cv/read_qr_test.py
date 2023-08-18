# Тестовый файлик всей работы, которую нужно сделать
import os
import tempfile
import cv2
from pyzbar.pyzbar import decode
from read_qr import decode_qr_code

def main():
    with open('..\..\img_2.jpg', "rb") as image:
        # Чтение данных изображения в виде байтов
        f = image.read()

    # Создаем временный файл и записываем в него байты изображения
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_filename = temp_file.name
        temp_file.write(f)

    try:
        # Преобразование изображения в оттенки серого
        gray_image = cv2.cvtColor(cv2.imread(temp_filename), cv2.COLOR_BGR2GRAY)
        '''
        [[255 255 255 ... 255 255 255]
        [255 255 255 ... 255 255 255]
        [255 255 255 ... 255 255 255]
        ...
        [255 255 255 ... 255 255 255]
        [255 255 255 ... 255 255 255]
        [255 255 255 ... 255 255 255]]
        '''
        # Поиск QR-кодов на изображении
        decoded_object = decode(gray_image)
        '''
        [Decoded(data=b't=20230806T1758&s=3033.00&fn=7281440500987470&i=235004&fp=2228331747&n=1', 
        type='QRCODE', rect=Rect(left=410, top=20, width=264, height=264), polygon=[Point(x=410, y=20), 
        Point(x=411, y=284), Point(x=674, y=284), Point(x=673, y=22)], quality=1, orientation='UP')]
        '''
        if len(decoded_object) == 1:
            decoded_data = decoded_object[0].data.decode('utf-8')
        '''
        t=20230806T1758&s=3033.00&fn=7281440500987470&i=235004&fp=2228331747&n=1  
        //data без decode
        '''
    finally:
        os.remove(temp_filename)

if __name__ == '__main__':
    main()