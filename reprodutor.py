from playsound import playsound  # Funcao responsavel por falar
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import requests
import json


def call_watson(txt):
    url = "URL"
    querystring = {"version": "2019-02-28"}
    payload = {'input': {
        'text': txt}
    }
    payload = json.dumps(payload)
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic auth",
    }
    response = requests.request(
        "POST", url, data=payload, headers=headers, params=querystring)
    responseJSON = json.loads(response.text)
    return responseJSON['output']['text'][0]


def lysten_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Say something: ")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            print("You said:", frase)
        except sr.UnkownValueError:
            print("I did not understand")
    return frase


def create_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/ad.mp3')
    playsound('audios/ad.mp3')


def menu():
    frs = lysten_microfone()
    resp = call_watson(frs)
    create_audio(resp)
    return ''


menu()
