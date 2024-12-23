import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime


def transform_audio_into_text():
  r = sr.Recognizer()

  #set microphone
  with sr.Microphone() as source:
    print('Listening...')
    r.pause_threshold = 1
    audio = r.listen(source)


    audio = r.listen(source)

    try:
      #search on google
      request = r.recognize_google(audio, language='en-us')

      # Test in text
      print('You said: ' + request)

      return request
    
    except sr.UnknownValueError:
      print('Sorry, I did not understand what you said')
      return 'I am still waiting for your command'

    except sr.RequestError:
      print('Sorry, the service is down')
      return 'I am still waiting for your command'

    except:
      print("Something went wrong")

      return 'I am still waiting for your command'

# Function so that the assistant can be heard
def speak(message):
  engine = pyttsx3.init()
  engine.say(message)
  engine.runAndWait()

# Function to get the assistant's response: Ask what day it is?
def ask_day():

  # Today information
  day = datetime.date.today().strftime('%A')
  speak(f'Today is {day}')

# Function to get the assistant's response: Ask what time it is?
def ask_time():
  time = datetime.datetime.now().strftime('%I:%M %p')
  speak(f'At this moment it is{time}')

def initial_greeting():
  speak('Hello, I am your virtual assistant. How can I help you today?')


def my_assistant():
  
  initial_greeting()

  go_on = True

  while go_on:
    my_req = transform_audio_into_text()

    if 'open youtube' in my_req:
      speak('Opening Youtube')
      webbrowser.open('https://www.youtube.com')
      continue
    elif 'open browser' in my_req:
      speak('Opening Browser')
      webbrowser.open('https://www.google.com')
      continue
    elif 'what day it is' in my_req:
      ask_day()
      continue
    elif 'what time it is' in my_req:
      ask_time()
      continue
    elif 'do a wikipedia search for' in my_req:
      speak('I am looking for it')
      my_req = my_req.replace('do a wikipedia search for', '')
      answer = wikipedia.summary(my_req, sentences=1)
      speak('According to wikipedia')
      speak(answer)
      continue
    elif 'search the internet for' in my_req:
      speak('Of course, right now')
      my_req = my_req.replace('search the internet for', '') 
      pywhatkit.search(my_req)
      speak('I found the following information')
      continue
    elif 'play' in my_req:
      speak('Oh, what a great idea! I\'ll play it right now')
      my_req = my_req.replace('play', '')
      pywhatkit.playonyt(my_req)
      continue
    elif 'joke' in my_req:
      speak(pyjokes.get_joke())
      continue
    elif 'stock price of' in my_req:
      share = my_req.split()[-2].strip()
      portfolio = {
        'apple': 'AAPL',
        'amazon': 'AMZN',
        'google': 'GOOGL',
        'nike': 'NKE',
        'netflix': 'NFLX',
        'spotify': 'SPOT',
      }

      stock = yf.Ticker(share)

      try:
        searched_stock = portfolio[share]
        searched_stock = yf.Ticker(searched_stock)
        price = searched_stock.info('regularMarketPrice')
        speak(f'The price of {share} is {price}')
        continue
      except:
        speak('I am sorry, I could not find the stock you requested')
        continue
    elif 'exit' or 'goodbye' in my_req:
      speak('Goodbye, let me know if you need anything else. Have a great day!')
      go_on = False
my_assistant()  