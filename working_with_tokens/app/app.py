from app.exceptions import NoFileProcesserException
from app.file_processer import FileProcesser
from app.ollama_client import OllamaClient


class Application:
    def __init__(
        self, client: OllamaClient, file_processer: FileProcesser | None = None
    ) -> None:
        self.chat_client = client
        self.file_processer = file_processer

    def process_text(self, text: str):
        result = self.chat_client.chat(text)
        return result

    def process_dir(self, path_to_dir: str):
        if not self.file_processer:
            raise NoFileProcesserException()

        for text in self.file_processer.process_dir(path_to_dir):
            yield self.process_text(text)
