from api_handler import APIHandler
from complex_task_handler import ComplexTaskHandler
from simple_task_handler import SimpleTaskHandler
from speech_handler import SpeechHandler
from task_classifier import TaskClassifier

# Ties everything together in the main loop, continuously listening to user
# input and providing responses based on task classification.
class VoiceAssistant:
    def __init__(self):
        self.speech_handler = SpeechHandler()
        self.task_classifier = TaskClassifier()
        self.simple_task_handler = SimpleTaskHandler()
        self.complex_task_handler = ComplexTaskHandler()
        self.api_handler = APIHandler()

    def run(self):
        while True:
            user_input = self.speech_handler.get_voice_input()
            if not user_input:
                continue

            task_type = self.task_classifier.classify_task(user_input)

            if task_type == "simple":
                response = self.simple_task_handler.handle_task(user_input)
            elif task_type == "complex":
                response = self.complex_task_handler.handle_task(user_input)
            else:
                response = self.api_handler.call_api(user_input)

            print(f"Assistant: {response}")
            self.speech_handler.speak_response(response)

# Run the Assistant
if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()