from simple_task_handler import SimpleTaskHandler

# Manages different API calls based on user input.
class APIHandler:
    def call_api(self, user_input):
        if "weather" in user_input.lower():
            return SimpleTaskHandler().get_weather()
        elif "calendar" in user_input.lower():
            # Placeholder for calendar API call
            return "I can add events to your calendar."
        else:
            return "I don't recognize that API call."