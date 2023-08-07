from beepy import beep
import speech_recognition as sr
import builtins

def play_sound():
    beep(sound =3)

class SpeechToTextInterpreter:
    def __init__(self):
        self.r = sr.Recognizer()

    def read_line(self, *args):
        while True:
            with sr.Microphone() as source:
                play_sound()
                audio = self.r.record(source, 4)
                print('\a')
            try:
                text = self.r.recognize_google(audio)
                if text:
                    return text
            except sr.UnknownValueError:
                print("Sorry, did you mumble? Try that again.")
            except sr.RequestError:
                print("Make sure you have interwebs.")
            except Exception:
                print("Try again. Accidentally got the beep boops mixed up with the bip bops.")

    def __enter__(self):
        self.og_input = builtins.input
        builtins.input = self.read_line

    def __exit__(self, exc_type, exc_value, exc_trace):
        builtins.input == self.og_input