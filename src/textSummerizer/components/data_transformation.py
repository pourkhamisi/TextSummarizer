import os
from src.textSummerizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from src.textSummerizer.entity import DataTransformationconfig

class DataTransformation:
    def __init__(self, config: DataTransformationconfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
       input_encodings = self.tokenizer(example_batch['dialogue'], truncation=True, padding='max_length', max_length=512)

       with self.tokenizer.as_target_tokenizer():   
           target_encodings = self.tokenizer(example_batch['summary'], truncation=True, padding='max_length', max_length=128)

       return {
          'input_ids': input_encodings['input_ids'], 
          'attention_mask': input_encodings['attention_mask'], 
          'labels': target_encodings['input_ids']
              }  

    def convert_dataset_to_features(self):
        logger.info("Loading dataset from disk")
        dataset = load_from_disk(self.config.data_path)
        dataset_pt = dataset.map(self.convert_examples_to_features, batched=True)
        dataset_pt.save_to_disk(os.path.join(self.config.root_dir, "dataset"))
        logger.info("Converting dataset to features")