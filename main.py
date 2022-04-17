# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyttsx3
listh = (1,2,3,4)
print(listh[0:3])
#Male Voice
audio = pyttsx3.init()
audio.setProperty('rate',150)
audio.setProperty('volume',0.8)
audio.say("Hello Friend")
audio.runAndWait()

#Female voice
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
audio.setProperty('rate',150)
audio.setProperty('volume',0.8)
audio.setProperty('voice',voice_id)
audio.say("Hello Friend")
audio.runAndWait()