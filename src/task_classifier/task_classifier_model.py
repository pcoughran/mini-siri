from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

# A fine tuned BERT classifier to determine if an input is simple or complex.
class TaskClassifierModel:

    def __init__(self):
        # Sample data
        self.data = {
            "text": [
                "What time is it?",
                "What is the weather today?",
                "Tell me a joke.",
                "How do neural networks work?",
                "Explain the theory of gravity."
            ],
            "label": [0, 0, 0, 1, 1]  # 0: Simple, 1: Complex
        }

        # Convert to Hugging Face dataset
        self.dataset = Dataset.from_dict(self.data)

        # Tokenizer and model setup
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

    # Tokenization function
    def tokenize_function(self, examples):
        return self.tokenizer(examples["text"], padding="max_length", truncation=True)

    def train_and_save(self):
        # Apply tokenization
        tokenized_dataset = self.dataset.map(self.tokenize_function, batched=True)

        # Define training arguments
        training_args = TrainingArguments(
            output_dir='./results',
            num_train_epochs=3,
            per_device_train_batch_size=2,
            evaluation_strategy="no",
            save_strategy="no"
        )

        # Trainer setup
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=tokenized_dataset,
        )

        # Train the model
        trainer.train()

        # Save the model
        self.model.save_pretrained("./task_classifier_model")
        self.tokenizer.save_pretrained("./task_classifier_model")

# Train and save the model
tcm = TaskClassifierModel()
tcm.train_and_save()