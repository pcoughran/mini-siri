# mini-siri
A mini siri.

# High-Level Architecture

1. Voice Input: Convert speech to text using a Speech-to-Text (STT) library.
2. Task Classification: Train and use a fine tuned BERT classifier to determine if an input is simple or complex.
3. Response Generation:
    - For simple tasks, use a local model.
    - For complex tasks, call an external LLM API like ChatGPT.
4. API Handling: Call external APIs to perform specific tasks (e.g., weather, calendar, etc.).
5. Voice Output: Convert the response to speech using a Text-to-Speech (TTS) library.