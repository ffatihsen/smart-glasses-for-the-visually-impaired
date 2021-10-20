
#Kütüphanelerin import edildiği kısım
import speech_recognition as sr
from gtts import gTTS
import os
import time
import okuma
import fotoCek
import renkTanıma
import Asistan
import Verimain


r = sr.Recognizer()

#Asistanın kullanıcıya söyleyeceği belli başlı metinlerin tanımlandığı bölüm
metin1="Merhaba Ben Sanal Asistan EyeX. Senin için ne yapabilirim ? . Yeteneklerimi öğrenmek istersen, Yeteneklerin neler diyebilirsin."

metin2Y ="İstersen Renk Tanıma İşlemi yaparım, istersen okuma işlemi yaparım, istersen senin için hava durumuna bakabilirim ,istersen de ChetBot ile Sohbet Etmeni sağlayabilirim." \
        "Renk Tanıma işlemi yapmamı istersen, renk tanı demen yeterli olacaktır." \
        "Okuma işlemi yapmamı istersen, Okuma işlemi yap, demen yeterli olacaktır." \
        "ChetBot ile Sohbet Etmek için , Sohbet demen yeterli olacaktır." \
        "Hava durumunu öğrenmek için ise hava durumunu öğren demen yeterli olacaktır." \
        "Beni kapatmak için de asistan dur, diyebilirsin." \

metin3="İşleminiz Tamamlandı. Şimdi Ne yapmak istersiniz ?"


metin4="Okuma işlemi için Fotoğraf çekilmesi gerekiyor. Lütfen Kameraya okutacağınız nesneyi yaklaştırın."

metin5="Asistan kapanıyor Hoşçakalın"

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

konustur(metin1)
time.sleep(14)

#konustur(metin2)
#time.sleep(40)

while True:
    print("Konuş")
    emir=kayit()
    emir = emir.lower()
    print(emir)

    if "okuma işlemi yap" in emir or "okuma" in emir or "okuma işlemi" in emir:
        konustur(metin4)
        time.sleep(8)
        cek=fotoCek.Cek()
        cek.basla()
        time.sleep(3)
        oku=okuma.Oku()
        oku.basla()

    elif "renk tanı" in emir or "renk" in emir:
        time.sleep(3)
        tani=renkTanıma.Renk_Tani()
        tani.basla()
        time.sleep(5)

    elif "sohbet" in emir:
        bot = Asistan.Bot()
        bot.basla()

    elif "hava durumu" in emir or "hava durumunu öğren" in emir or "hava" in emir:
        hava=Verimain.HavaDurumu()
        hava.basla()

    elif "yeteneklerin neler" in emir or "yetenekler" in emir or "yeteneğin" in emir:
        konustur(metin2Y)

    elif "asistan dur" in emir or "dur" in emir or "kapat" in emir:
        konustur(metin5)
        break
    konustur(metin3)
    time.sleep(8)
