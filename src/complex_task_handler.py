from openai import OpenAI
import os
from dotenv import load_dotenv

# Uses the OpenAI API to handle complex tasks that require deeper conversational AI.

class ComplexTaskHandler:
    def __init__(self):
        # Specify your custom assistant's model name
        self.model_name = "gpt-3.5-turbo"  # Update to your custom model's identifier, e.g., 'mini-siri'
        self.assistant_name = "mini-siri"
        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

    def handle_task(self, user_input):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": "Say this is a test",
                    }
                ],
                model="gpt-3.5-turbo",
            )
            reply = chat_completion['choices'][0]['message']['content']
            return reply
        except Exception as e:
            return f"Error interacting with {self.assistant_name}: {e}"