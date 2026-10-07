from transformers import AutomodelForSeq2SeqLM, AutomodelTokenizer
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from datasets import load_from_disk
import torch
import os
from src.textSummerizer.entity import ModelTrainerconfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerconfig):
        self.config = config

    def train(self):
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_name)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_name)

        dataset = load_from_disk(self.config.data_path)

        training_args = TrainingArguments(
            output_dir=self.config.output_dir,
            evaluation_strategy=self.config.evaluation_strategy,
            save_strategy=self.config.save_strategy,
            learning_rate=self.config.learning_rate,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            num_train_epochs=self.config.num_train_epochs,
            weight_decay=self.config.weight_decay
        )

        data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"],
            tokenizer=tokenizer,
            data_collator=data_collator
        )

        trainer.train()

        # Save the trained model
        model.save_pretrained(self.config.output_dir)

        # Save the tokenizer
        tokenizer.save_pretrained(self.config.output_dir)