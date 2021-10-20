
#Gerekli kütüphanelerin eklendiği kısım
import cv2
from pytesseract import pytesseract
from pytesseract import Output
import time
from gtts import gTTS
import os

class Oku():
    def basla(self):
        pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        #pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe" #Yol 2
        img = cv2.imread("test.jpg")
        height, width, c = img.shape
        ##############################################
        # Terminal Ekranında çıktı vermek için gerekli
        #words_in_image = pytesseract.image_to_string(img,lang="tur")
        words_in_image = pytesseract.image_to_string(img)
        print(words_in_image)
        uzunluk=len(words_in_image)
        ############################################

        ################################################
        # Sesli konuşmasi icin gereken kodlar
        tts = gTTS(text=words_in_image, lang="tr")
        tts.save("konus.mp3")
        os.system("konus.mp3")
        ################################################
        #time.sleep(30)

        image_data = pytesseract.image_to_data(img, output_type=Output.DICT)

        for i, word in enumerate(image_data["text"]):
            if word != "":
                x, y, w, h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][
                    i]
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(img, word, (x, y - 16), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("window", img)
        #cv2.waitKey(0)
        #time.sleep(10)
        time.sleep((uzunluk/10)+5)
        cv2.destroyAllWindows()




#deneme=Oku()
#deneme.basla()



