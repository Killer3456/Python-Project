import requests
import json
import win32com.client as wincom

city = input("Enter the name of the city\n")

url= f"https://api.weatherapi.com/v1/current.json?key=fb3eeed0cf1948f68ad32952230507&q={city}"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.SpVoice")

text = "The current weather in " + city + " is"+ str(w) + "degree"
speak.Speak(text)

