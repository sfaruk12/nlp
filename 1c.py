#Convert audio file Speech to Text. Source code:
#pip3 install SpeechRecognition pydub

import speech_recognition as sr
filename = "open-the-door.wav"

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
# listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)