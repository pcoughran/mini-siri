import speech_recognition as sr
import pyttsx3

# Manages the voice input/output functionality.
class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

    def get_voice_input(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"User: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Error with the STT service")
        return ""

    def speak_response(self, response_text):
        self.tts_engine.say(response_text)
        self.tts_engine.runAndWait()
