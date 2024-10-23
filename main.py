from FileManager import FileManager  # Importe la classe FileManager depuis le fichier FileManager

log_file = 'log.txt'  # Définit le fichier de log à gérer

file_manager = FileManager(log_file)  # Instancie la classe FileManager avec le chemin du fichier log

print("Contenu du fichier log :")
print(file_manager.read_file())  # Lit et affiche le contenu du fichier log

# Ajoute une nouvelle ligne au fichier log avec une date et un message d'information
file_manager.append_to_file("\n[2024-10-21 12:00:00] INFO: Test d'ajout de ligne.")
print("\nAprès ajout de contenu :")
print(file_manager.read_file())  # Relit et affiche le contenu du fichier log après l'ajout

# Recherche et affiche toutes les lignes contenant le mot 'ERROR' dans le fichier log
print("\nLignes contenant 'ERROR' :")
errors = file_manager.search_keyword('ERROR')
for error in errors:
    print(error)  # Affiche chaque ligne contenant 'ERROR'

# Recherche et affiche toutes les lignes contenant le mot 'INFO' dans le fichier log
print("\nLignes contenant 'INFO' :")
infos = file_manager.search_keyword('INFO')
for info in infos:
    print(info)  # Affiche chaque ligne contenant 'INFO'
