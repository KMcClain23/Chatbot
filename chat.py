import os
import speech_recognition as sr
from dotenv import load_dotenv
import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard
from stti import SpeechToTextInterpreter

load_dotenv()

token = os.environ.get('COOKIE_1')
cookie_2 = os.environ.get('COOKIE_2')
cookie_3 = os.environ.get('COOKIE_3')

session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set('__Secure-1PSID', token)
session.cookies.set('__Secure-1PSIDTS', cookie_2)
session.cookies.set('__Secure-1PSIDCC', cookie_3)

bard = Bard(token=token, session=session)


def get_response(user_input):
    bad_chars = ['*', '**', '[', ']', '\\', '/']
    response = bard.get_answer(user_input)['content']
    for char in bad_chars:
        response = response.replace(char, "")
    return response


class Chatbot:
    def __init__(self):
        self.name = "Botman"
        self.user_name = 'User'

    def save_user_info(self, user_name):
        self.user_name = user_name

    def get_user_info(self):
        print("What is your name? ")
        name = input("")
        self.save_user_info(name)
        print(f'Welcome {name}')

    def chat(self):
        print(f"Hello, I'm {self.name}")
        self.get_user_info()
        # print("What can I do for you today?")
        while True:
            user_input = input("How can I help you? ")
            if user_input.lower() == "quit":
                print(f"Bye. Hope we can chat soon! Don't forget, I'm {self.name}!")
                break

            response = get_response(user_input)
            print(response)

with SpeechToTextInterpreter():
    chatbot = Chatbot()
    chatbot.chat()
