
import speech_recognition as sr
from gtts import gTTS
import os
from bs4 import BeautifulSoup as bs
import urllib.request as istek
import time

r = sr.Recognizer()

def konustur(metin):
    tts = gTTS(text=metin, lang="tr")
    tts.save("metin.mp3")
    os.system("metin.mp3")

def kayit():
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice=""
        try:
            voice=r.recognize_google(audio,language="tr")

        except sr.UnknownValueError :
            print("Sesi Anlayamadım")
        return voice

class HavaDurumu():
	def basla(self):
		konustur("Hangi ilin hava durumunu öğrenmek istiyorsunuz. Söyleyin ")
		time.sleep(7)
		print("->")
		il = kayit()
		il=il.lower()
		print(il)

		konustur("Hangi ilçenin hava durumunu öğrenmek istiyorsunuz. Söyleyin ")
		time.sleep(7)
		print("->")
		ilce = kayit()
		ilce = ilce.lower()
		print(ilce)
		url = "http://www.mynet.com/havadurumu//asya/turkiye/{}/{}".format(il, ilce)
		urlOku = istek.urlopen(url)
		veri = bs(urlOku, 'html.parser')
		sicaklik = veri.find_all('span', attrs={'class': 'hvDeg1'})
		derece =sicaklik[0].text
		print(derece)
		metin="{} {} hava durumu {} dir.".format(il,ilce,derece)
		konustur(metin)
		time.sleep(6)


#da = HavaDurumu()
#da.basla()