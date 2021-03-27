import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',125)
#print(voices[0])
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hora = int(datetime.datetime.now().hour)
    if hora >= 0 and hora < 12:
        speak("Bom Dia")
    elif hora >= 12 and hora < 18:
        speak("Boa Tarde")
    else:
        speak("Boa Noite")
    speak("Me Chamo Helena, sou a sua assistente pessoal, Posso ajudar em alguma coisa?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Ouvindo...")
        speak("Posso Ajudar em alguma coisa?")
        r.pause_threshold = 1
        audio = r.listen(sourse)
    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-br')
        print('O Usuario Disse: ',query)
        speak(f"O você ordenou {query}")
    except Exception as e:
        #print(e)
        speak("não entendi Pode repetir, por favor.")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('teste@gmail.com','********')
    server.sendEmail('teste@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("pesquisa wikipedia...")
            query = query.replace("wikipedia","")
            resultado = wikipedia.summary(query,sentences=2)
            speak("de acordo com a wikipedia")
            print(resultado)
            speak(resultado)
        elif 'abrir youtube' in query:
            speak("Ok, Abrindo o youtube!")
            webbrowser.open("https://www.youtube.com/")

        #link do seu instagram
        elif 'abrir instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("Ok, Abrindo o instagran!")

        elif 'abrir google' in query:
            webbrowser.open("https://www.google.com/")
            speak("Ok, Abrindo o google!")
	
	#link do seu facebook
        elif 'abrir facebook' in query:
            webbrowser.open("https://www.facebook.com/people")
            speak("Ok, Abrindo o seu facebook!")
        
        elif 'abrir stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")
            speak("Ok, Abrindo starckoverflow!")

        elif 'que horas são' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"certo são Exatamente : {strTime}")

        elif 'abrir play music' in query:
            music_dir = "C:\\Users\\Geovane\\Music"
            sons = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,sons[0]))
            speak("Ok, Abrindo Play Music!")


        elif 'abrir vs code' in query:
            codePath = "C:\\Users\\Geovane\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Ok, Abrindo vs Code!")

        elif 'abrir android studio' in query:
            studioPath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(studioPath)
            speak("Ok, Abrindo o Android studio!")

        elif 'e-mail para amigo' in query:
            try:
                speak('O que deveria dizer?')
                content = takeCommand()
                to = "teste@gmail.com"
                sendEmail(to,content)
                speak("o e-mail foi enviado")
            except Exception as e:
                print(e)
                speak("desculpe meu amigo. Não consigui enviar o e-mail")
        
        elif 'descansar' in query:
            speak("certo, foi um prazer ajudar encerrando as atividades, até mais.")
            break




