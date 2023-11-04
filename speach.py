import speech_recognition as speech_recog
import time


def speach():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        print('говорите пожалуйста')
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="ru-RU")
        
            


def speachen():
    micc = speech_recog.Microphone()
    recogg = speech_recog.Recognizer()

    with micc as audio_filee:
        print('spiak plase')
        recogg.adjust_for_ambient_noise(audio_filee)
        audioo = recogg.listen(audio_filee)
        return recogg.recognize_google(audioo, language="en-EN")
