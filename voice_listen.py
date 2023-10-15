import speech_recognition as sr
import respond_to_admin as ra
import hme_auto as hm
import  gettime as gt

Rec = sr.Recognizer()

def Listen_to_Admin():

    try:
        with sr.Microphone() as SRC:
            Rec.adjust_for_ambient_noise(SRC, 0.2)
            AUD_DATA = Rec.listen(SRC)
            DATA = Rec.recognize_google(AUD_DATA, language='en-US')
            print(DATA)
            if DATA != "exit":
                ra.SPEAK(DATA)
            if DATA == "turn off all equipments":
                hm.change_value(0)
            if DATA == "turn on all equipments":
                hm.change_value(1)
            if DATA == "what's the time now":
                CT = gt.Current_Time()
                ra.SPEAK(CT)
            # else:
            #     exit()
    except sr.UnknownValueError():
        return False