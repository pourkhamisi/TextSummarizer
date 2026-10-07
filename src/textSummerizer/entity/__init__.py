from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataTransformationconfig:
    root_dir: Path 
    data_path: Path 
    tokenizer_name: Path

@dataclass
class ModelTrainerconfig:
    root_dir: Path 
    data_path: Path 
    model_name: Path
    output_dir: Path
    evaluation_strategy: str
    save_strategy: str
    learning_rate: float
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    num_train_epochs: int
    weight_decay: float