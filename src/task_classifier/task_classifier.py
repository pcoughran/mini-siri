from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Classifies tasks into either "simple" or "complex".
class TaskClassifier:
    def __init__(self):
        self.model_path = "./task_classifier/task_classifier_model"
        self.tokenizer = BertTokenizer.from_pretrained(self.model_path)
        self.model = BertForSequenceClassification.from_pretrained(self.model_path)

    def classify_task(self, user_input):
        inputs = self.tokenizer(user_input, return_tensors="pt", padding=True, truncation=True, max_length=128)
        outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_label = torch.argmax(logits, dim=1).item()

        if predicted_label == 0:
            return "simple"
        else:
            return "complex"
