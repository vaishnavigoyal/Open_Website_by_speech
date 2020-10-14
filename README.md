# Open_Website_by_speech
Opening website by speechRecognition using python

We need to import two important libraries from python, which are essential to run this script.  •  SpeechRecognition: It is the library used mainly for recognising the speech.
 •  Web browser: Web Browser module is used to display the web-based content to the users.
The main class that we use in this script is the Recognizer class that’s present in the speech recognition library.


Aceesing the browser:

There are several methods available in the web browser module in order to open the browser.

webbrowser.open(url, new=0, autoraise=True)
 •  Display the url given as input.
 •  If new is set to 0 the url is opened in the same browser.

webbrowser.open_new(url)
 •  Opens the url in a new window in the browser which is set to default

webbrowser.open_new_tab(url) 
 •  Opens the url in a new tab.
We will be using the simple method open( ) in this script.
We will add a hypertext link at the start and the pass the url to the open method.

wb.open('http://'+text)
If there is any problem in recognising the text we can raise an exception stating that unable to recognise the voice.

print("Couldn't recognize your voice")
Note: Make sure to install speech_recognition and pyaudio libraries using pip.
