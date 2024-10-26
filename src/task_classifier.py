
# Classifies tasks into either "simple" or "complex".
class TaskClassifier:
    def classify_task(self, user_input):
        simple_tasks = ["time", "date", "weather", "joke", "news"]
        if any(task in user_input.lower() for task in simple_tasks):
            return "simple"
        return "complex"