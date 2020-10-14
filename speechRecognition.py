#importing necessary modules
import speech_recognition as sr
import webbrowser as wb

#creating an object for voice recognizer
r=sr.Recognizer()


with sr.Microphone() as source:
    print('Ask for a website to open')#prompt for a input website
    audio=r.listen(source)#listen for the source
    try:
        text=r.recognize_google(audio)#extract the text from the audio
        print("You asked for : {}".format(text)+" website")#Display the website input
        if('.com' in text):
            wb.open('http://'+text)#Add hypertext link as the start and open
        else:
            wb.open('http://'+text+'.com')##Add hypertext link as the start and com at the end and open
    except:
        print("Couldn't recognize your voice")#Raise an exception if the voice can't be heard or analysed