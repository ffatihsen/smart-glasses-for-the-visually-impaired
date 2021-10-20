
#Kütüphanelerin Eklendiği kısım
import numpy as np
import cv2
import datetime, time

from gtts import gTTS
import os
class Renk_Tani():
    def konustur(self,metin):
        tts = gTTS(text=metin, lang="tr")
        tts.save("metin.mp3")
        os.system("metin.mp3")

    def basla(self):
        metin1 = "Bu cismin rengi {} dir"

        # Pc nin kamerası ile görüntüyü alıyoruz
        webcam = cv2.VideoCapture(0,
                                  cv2.CAP_DSHOW)  # İlk parametrenin 0 olması pc nin kamerasını kullanacağımız anlamına geliyor

        # Canlı bir görüntü olduğu için her şey sonsuz bir döngünün içerisinde yer almalı
        while (1):
            # Yakaladığımız görüntüyü burda okutma işlemi yapıyoruz ve bu işlem geriye 2 tane değer dönderiyor
            # bunlardan birisi çok önemli olmadığı için onu bu ' _ ' şekilde yakalıyoruz.
            _, imageFrame = webcam.read()

            # imageFrame i dönüştürme işlemi
            # BGR(RGB color space) to
            # HSV(hue-saturation-value)
            # renk uzayı belirleme
            hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

            # Kırmızı renk için renk aralığı ayarlama ve maske tanımlama
            red_lower = np.array([136, 87, 111], np.uint8)
            red_upper = np.array([180, 255, 255], np.uint8)
            red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

            # Yeşil renk için renk aralığı ayarlama ve maske tanımlama
            green_lower = np.array([25, 52, 72], np.uint8)
            green_upper = np.array([102, 255, 255], np.uint8)
            green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

            # Mavi renk için renk aralığı ayarlama ve maske tanımlama
            blue_lower = np.array([94, 80, 2], np.uint8)
            blue_upper = np.array([120, 255, 255], np.uint8)
            blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

            # Morfolojik Dönüşüm ve Genişleme
            # yalnızca belirli rengi algılamak için
            kernal = np.ones((5, 5), "uint8")  # np.ones() geriye 5 e 5 bir matris dönderir ve içerisi hep 1 dir

            # Kırmızı renk için
            red_mask = cv2.dilate(red_mask,
                                  kernal)  # rengi genişletmek içindir yani red_mask giriyor ve kernal olarak genişliyor
            res_red = cv2.bitwise_and(imageFrame, imageFrame,
                                      mask=red_mask)

            # Yeşil renk için
            green_mask = cv2.dilate(green_mask, kernal)
            res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                        mask=green_mask)

            # Mavi renk için
            blue_mask = cv2.dilate(blue_mask, kernal)
            res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                                       mask=blue_mask)

            # Kırmızı rengi izlemek için kontur oluşturma
            # Konturlar aynı renk ve yoğunluğa sahip olan
            # tüm kesintisiz noktaları sınır boyunca birleştiren bir eğri olarak basitçe açıklanabilir
            """
             1.Birinci argüman kontur bulunacak kaynak görüntüdür.
             2.İkinci argüman kontur alma modudur. 
             3.Üçüncü argüman ise kontur yaklaşım metodur.
            """
            contours, hierarchy = cv2.findContours(red_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)

            # Bulunan konturları enumerate işlemi yapılarak her biri tek tek ele alınır
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)  # Burda konturların genişliği hesaplanır
                if (area > 300):
                    """
                     bu kontur alanlarını dikdörtgen içine almak istiyoruz. 
                     Bunun için cv2.boundingRect() metodu ile kontur çerçeve noktalarını hesaplayıp 
                     cv2.rectangle() metoduyla etraflarına dikdörtgen çizebiliriz.
                    """
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y),
                                               (x + w, y + h),
                                               (0, 0, 255), 2)

                    cv2.putText(imageFrame, "Kirmizi Renk", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                                (0, 0, 255))

                    #print("Kırmızı")
                    metin2 = metin1.format("kırmızı")
                    self.konustur(metin2)
                    cv2.destroyAllWindows()
                    return 1

            # Yeşil renk için contour bulma işlemi tekrarlanır
            contours, hierarchy = cv2.findContours(green_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)

            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y),
                                               (x + w, y + h),
                                               (0, 255, 0), 2)

                    cv2.putText(imageFrame, "Yesil Renk", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (0, 255, 0))

                    #print("Yeşil")
                    metin2=metin1.format("yeşil")
                    self.konustur(metin2)
                    cv2.destroyAllWindows()
                    return 1


            # Mavi renk için contour bulma işlemi tekrarlanır
            contours, hierarchy = cv2.findContours(blue_mask,
                                                   cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if (area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y),
                                               (x + w, y + h),
                                               (255, 0, 0), 2)

                    cv2.putText(imageFrame, "Mavi Renk", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0))

                    #print("Mavi")
                    metin2 = metin1.format("mavi")
                    self.konustur(metin2)
                    cv2.destroyAllWindows()
                    return 1


            # Program Termination
            cv2.imshow("Renk Tanimlama", imageFrame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                # cv2.release()
                cv2.destroyAllWindows()
                break

#ornek=Renk_Tani()
#ornek.basla()
