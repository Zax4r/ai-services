import os
from loguru import logger

class FileProcesser:
    def __init__(self) -> None:
        pass

    def process_dir(self, path_to_dir: str):
        buffer = ''
        for filename in os.listdir(path_to_dir):
            if filename.endswith('.txt'):
                file_path = os.path.join(path_to_dir, filename)
                with open(file_path, 'r') as f:
                    buffer = f.read()
                logger.info(f'Processing file {file_path}')
                yield buffer
