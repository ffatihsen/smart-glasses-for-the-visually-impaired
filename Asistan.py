
#Kütüphanelerin import edildiği kısım
import nltk
from snowballstemmer import TurkishStemmer
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import Adam
import numpy as np
import numpy
import random
import json
import speech_recognition as sr
from gtts import gTTS
import os
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



class Bot():
    def basla(self):
        with open(r"data.json") as file:
            data = json.load(file)
        stemmer = TurkishStemmer()
        words = []
        labels = []
        docs_x = []
        docs_y = []
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])
            if intent["tag"] not in labels:
                labels.append(intent["tag"])
        print("-------")
        print(words)
        print("--------")
        words = [stemmer.stemWord(w.lower()) for w in words if w != "?"]
        words = sorted(list(set(words)))
        print("-------")
        print(words)
        print("--------")
        labels = sorted(labels)
        training = []
        output = []
        out_empty = [0 for _ in range(len(labels))]
        for x, doc in enumerate(docs_x):
            bag = []
            wrds = [stemmer.stemWord(w.lower()) for w in doc]
            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)
            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1
            training.append(bag)
            output.append(output_row)
        training = numpy.array(training)
        output = numpy.array(output)
        # print(labels) #['ayrÄ±lma', 'bilgi', 'learn', 'selamlama']
        model = Sequential()
        model.add(Dense(16, input_shape=(len(training[0]),), activation="relu"))
        model.add(Dense(16, activation="relu"))
        model.add(Dropout(0.2))
        model.add(Dense(4, activation="softmax"))
        model.summary()
        model.compile(Adam(lr=.001), loss="categorical_crossentropy", metrics=["accuracy"])
        model.fit(training, output, epochs=300, verbose=2, batch_size=4)
        def bag_of_words(s, words):
            bag = [0 for _ in range(len(words))]
            s_words = nltk.word_tokenize(s)
            s_words = [stemmer.stemWord(word.lower()) for word in s_words]
            print("*************")
            print(s_words)
            print("*************")
            for se in s_words:
                for i, w in enumerate(words):
                    if w == se:
                        bag[i] = 1
            return numpy.array(bag)
        def chat():
            print("Chatbot ile konuşmaya başlayabilirsiniz (çık diyerek çıkabilirsiniz)!")
            konustur("Chatbot ile konuşmaya başlayabilirsiniz. çık diyerek çıkabilirsiniz")
            time.sleep(8)
            while True:
                print("konuş...")

                inp = kayit()
                inp=inp.lower()
                print(inp)

                #inp = input("You: ")
                if inp.lower() == "çık":
                    break
                results = model.predict(np.asanyarray([bag_of_words(inp, words)]))[0]
                print(results)
                results_index = numpy.argmax(results)
                tag = labels[results_index]
                if results[results_index] > 0.85:
                    for tg in data["intents"]:
                        if tg['tag'] == tag:
                            responses = tg['responses']
                    cevap=random.choice(responses)
                    print(cevap)
                    metin1=cevap
                    konustur(metin1)
                    time.sleep(4)
                else:
                    print("Tam olarak anlayamadım")
                    metin2="Tam olarak anlayamadım"
                    konustur(metin2)
                    time.sleep(4)

        chat()

#bot =Bot()
#bot.basla()