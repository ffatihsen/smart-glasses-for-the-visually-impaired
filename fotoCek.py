
import time
import cv2# kullanacağın modülü içe aktar

class Cek():
    def basla(self):
        camera = cv2.VideoCapture(0)  # Video çekmeye başla
        return_value, image = camera.read()  # İlk fotğrafı al
        cv2.imwrite('test.jpg', image)  # Kaydet
        camera.release()  # ?
        cv2.destroyAllWindows()  # Tüm ekranları kapat

        time.sleep(3)
#cek=Cek()
#cek.basla()
