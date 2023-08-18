from pyzbar.pyzbar import decode
import time
# ----------
from PIL import Image
from skimage import io, color
import imageio.v2
import png

# Вес библиотеки ~83.8 Мб
# ChatGPT говорит, что весит 5 Мб
def decode_with_Pillow(imgName):
    # Открываем изображение и накладываем чёрно-белый фильтр
    img = Image.open(imgName).convert("L")
    decodeObj = decode(img)
    result = []
    for i in decodeObj:
        result.append(i.data.decode("utf-8"))
    return result

# Вес библиотеки ~76 Мб
# ChatGPT говорит, что весит 25 Мб
def decode_with_scikitimage(imgName):
    # Открываем изображение
    img = io.imread(imgName)
    # Накладываем чёрно-белый фильтр
    #image_gray = color.rgb2gray(img)
    decodeObj = decode(img)
    result = []
    for i in decodeObj:
        result.append(i.data.decode("utf-8"))
    return result

# Вес библиотеки ~3.16 Мб
# ChatGPT говорит, что весит 2 Мб
def decode_with_imageio(imgName):
    # Открываем изображение
    img = imageio.v2.imread(imgName)
    # Накладываем чёрно-белый фильтр
    gray_img = img.mean(axis=2, keepdims=True).astype(img.dtype)
    decodeObj = decode(gray_img)
    result = []
    for i in decodeObj:
        result.append(i.data.decode("utf-8"))
    return result

img = ["..\..\img_test.png", "..\..\img_2.jpg", "..\..\img_3.jpg", "..\..\img_4.jpg", "..\..\img_9-.png"]
top = [['t=20230806T1758&s=3033.00&fn=7281440500987470&i=235004&fp=2228331747&n=1'],
       ['t=20230812T2243&s=702.08&fn=7284440500023733&i=34009&fp=4235293319&n=1'],
       ['https://github.com/Radeon590'], [],
       ['t=20200116T1149&s=935.60&fn=9285000100155513&i=30162&fp=1212772341&n=1']]

# print("Pillow test")
# res = []
# start_time = time.time()
# for i in img:
#     res.append(decode_with_Pillow(i))
# tm = time.time() - start_time
# print("--- %s seconds ALL ---" % (tm))
# eq = 0
# for el in range(0, len(top)):
#     if top[eq] == res[eq]:
#         eq = 1
#     else:
#         eq = 0
#         break
# print(eq)
# print(res)

# print("scikit-image test")
# res = []
# start_time = time.time()
# for i in img:
#     res.append(decode_with_scikitimage(i))
# tm = time.time() - start_time
# print("--- %s seconds ALL ---" % (tm))
# eq = 0
# for el in range(0, len(top)):
#     if top[eq] == res[eq]:
#         eq = 1
#     else:
#         eq = 0
#         break
# print(eq)
# print(res)

print("imageio test")
res = []
start_time = time.time()
for i in img:
    res.append(decode_with_imageio(i))
tm = time.time() - start_time
print("--- %s seconds ALL ---" % (tm))
eq = 0
for el in range(0, len(top)):
    if top[eq] == res[eq]:
        eq = 1
    else:
        eq = 0
        break
print(eq)
print(res)
