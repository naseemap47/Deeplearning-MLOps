import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_dirs:list, verbose=True):
    """create list of directories
    
    Args:
        path_to_dirs (list): list of path of directories
        ignore_log (bool, optional): ignore if mutiple dirs is to be created.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory: {path}")


@ensure_annotations
def save_json(path:Path, data:dict):
    """save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved: {path}")


@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """load json file data
    
    Args:
        path (Path): path to json file
    
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(path)
    
    logger.info(f"json file loaded successfully: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any, path:Path):
    """save binary file
    
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved: {path}")


@ensure_annotations
def load_bin(path:Path) -> Any:
    """load binary data
    
    Args:
        path (Path): path to binary file
    
    Returns:
        Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded: {path}")
    return data


@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(img_str, file_name):
    img_data = base64.b64decode(img_str)
    with open(file_name, 'wb') as f:
        f.write(img_data)
        f.close()


def encodeImageIntoBase64(cropped_img_path):
    with open(cropped_img_path, 'rb') as f:
        return base64.b64encode(f.read())
    
