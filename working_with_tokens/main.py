from app.app import Application
from app.file_processer import FileProcesser
from app.ollama_client import OllamaClient

if __name__ == '__main__':
    client = OllamaClient()
    file_processer = FileProcesser()
    app = Application(client, file_processer)

    for result in app.process_dir('files'):
        print(result[0]['message']['content'])
