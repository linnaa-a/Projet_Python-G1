from FileManager import FileManager

log_file = 'log.txt'

file_manager = FileManager(log_file)

print("Contenu du fichier log :")
print(file_manager.read_file())

file_manager.append_to_file("\n[2024-10-21 12:00:00] INFO: Test d'ajout de ligne.")
print("\nAprès ajout de contenu :")
print(file_manager.read_file())

print("\nLignes contenant 'ERROR' :")
errors = file_manager.search_keyword('ERROR')
for error in errors:
    print(error)

print("\nLignes contenant 'INFO' :")
infos = file_manager.search_keyword('INFO')
for info in infos:
    print(info)
