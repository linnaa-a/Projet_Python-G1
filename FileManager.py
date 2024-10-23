import os
import re

class FileManager:
    def __init__(self, file_path):
        """Initialise le gestionnaire de fichiers avec le chemin du fichier"""
        self.file_path = file_path

    def read_file(self):
        """Lit le contenu du fichier spécifié.

        Si le fichier n'existe pas, lève une exception FileNotFoundError.
        Retourne le contenu du fichier sous forme de chaîne de caractères.
        """
        if not os.path.exists(self.file_path):  # Vérifie si le fichier existe
            raise FileNotFoundError(f"Le fichier {self.file_path} n'existe pas.")

        with open(self.file_path, 'r', encoding='utf-8') as file:  # Ouvre le fichier en lecture
            data = file.read()  # Lit tout le contenu
        return data

    def write_file(self, data):
        """Écrit le contenu donné dans le fichier.

        Si le fichier n'existe pas, il sera créé.
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:  # Ouvre le fichier en mode écriture (écrase le contenu existant)
            file.write(data)  # Écrit le contenu fourni dans le fichier

    def append_to_file(self, data):
        """Ajoute le contenu donné à la fin du fichier sans écraser l'existant."""
        with open(self.file_path, 'a', encoding='utf-8') as file:  # Ouvre le fichier en mode ajout
            file.write(data)  # Ajoute le contenu à la fin du fichier

    def search_keyword(self, keyword):
        """Recherche un mot-clé dans le fichier.

        Retourne une liste des lignes contenant le mot-clé (recherche insensible à la casse).
        Si le fichier n'existe pas, lève une exception FileNotFoundError.
        """
        if not os.path.exists(self.file_path):  # Vérifie si le fichier existe
            raise FileNotFoundError(f"Le fichier {self.file_path} n'existe pas.")

        with open(self.file_path, 'r', encoding='utf-8') as file:  # Ouvre le fichier en lecture
            lines = file.readlines()  # Lit toutes les lignes du fichier

        # Recherche le mot-clé dans chaque ligne, en ignorant la casse
        matching_lines = [line.strip() for line in lines if re.search(keyword, line, re.IGNORECASE)]
        return matching_lines  # Retourne une liste de lignes correspondant au mot-clé
