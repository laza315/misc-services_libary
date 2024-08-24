import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd='Tesseract/tesseract.exe'
img=cv2.imread('pic.jpg')
imgdata=pytesseract.image_to_data(img)
imgg=imgdata.splitlines()
br=0
print('pocetak')
for i in range(len(imgg)):
    duzina = len(imgg[i])
    p=0
    while duzina>0:
        if i==0:
            break
        if imgg[i][duzina-1]=='X':
            print('pogodak')
            p=1
            print(imgg[i])
        duzina-=1
    if p==1:
        br+=1
    i+=1
