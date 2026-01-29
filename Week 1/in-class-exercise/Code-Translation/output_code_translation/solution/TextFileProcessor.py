import json
import os

class TextFileProcessor:
    def __init__(self, filename: str):
        self.filename_ = filename

    def read_file_as_json(self):
        with open(self.filename_, 'r', encoding='utf-8') as file:
            return json.load(file)

    def read_file(self) -> str:
        with open(self.filename_, 'r', encoding='utf-8') as file:
            return file.read()

    def write_file(self, content: str):
        with open(self.filename_, 'w', encoding='utf-8') as file:
            file.write(content)

    def process_file(self) -> str:
        content = self.read_file()
        result = ''.join(c for c in content if c.isalpha())
        self.write_file(result)
        return result
