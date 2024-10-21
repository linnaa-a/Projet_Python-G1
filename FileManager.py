import os
import re


class FileManager:
    def __init__(self, file_path):
        """Initialise le gestionnaire de fichiers avec le chemin du fichier"""
        self.file_path = file_path

    def read_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Le fichier {self.file_path} n'existe pas.")

        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def write_file(self, content):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def append_to_file(self, content):
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(content)

    def search_keyword(self, keyword):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Le fichier {self.file_path} n'existe pas.")

        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        matching_lines = [line.strip() for line in lines if re.search(keyword, line, re.IGNORECASE)]
        return matching_lines
