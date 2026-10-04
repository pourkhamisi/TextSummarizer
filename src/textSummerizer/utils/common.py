import os
from pathlib import Path
from src.textSummerizer.logging import logger
from box.exceptions import BoxValueError   
from box import ConfigBox
import yaml
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Returns:
        ConfigBox: A ConfigBox object containing the yaml data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True) -> None:
    """
     Creates directories if they do not exist.

     Args:
        path_to_directories (list): List of directory paths to create.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")    
