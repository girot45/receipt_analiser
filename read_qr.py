import cv2
import requests

from pyzbar.pyzbar import decode

def decode_qr_code(image_path):
    # Преобразование изображения в оттенки серого
    print(image_path)
    gray_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)

    # Поиск QR-кодов на изображении
    # decoded_object = decode(gray_image)

    url = f"https://dewiar.com/scanner/?code=image&url=data:{gray_image}"
    r = requests.post(url)
    print(r.content)
    return None
    # if len(decoded_object) != 1:
    #     return None
    # else:
    #     return decoded_object[0].data.decode('utf-8')



