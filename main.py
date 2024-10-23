from FileManager import FileManager  # Importe la classe FileManager depuis le fichier FileManager
import datetime  # Pour ajouter des timestamps dynamiquement


def main():
    # Demander à l'utilisateur de spécifier le fichier de log à gérer
    log_file = input("Entrez le nom du fichier de log (par défaut: log.txt) : ") or 'log.txt'

    file_manager = FileManager(log_file)  # Instancie la classe FileManager avec le fichier sélectionné

    while True:
        # Menu d'options
        print("\nOptions:")
        print("1. Lire le fichier log")
        print("2. Ajouter une nouvelle ligne au fichier log")
        print("3. Rechercher des lignes contenant un mot-clé")
        print("4. Quitter")

        choice = input("\nEntrez votre choix (1-4) : ")

        if choice == '1':
            # Lire et afficher le contenu du fichier log
            print("\nContenu du fichier log :")
            print(file_manager.read_file())

        elif choice == '2':
            # Ajouter une nouvelle ligne au fichier log avec une date et un message d'information
            timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            message = input("Entrez le message à ajouter au fichier log : ")
            file_manager.append_to_file(f"\n{timestamp} INFO: {message}")
            print("\nContenu du fichier log après ajout :")
            print(file_manager.read_file())

        elif choice == '3':
            # Rechercher des lignes contenant un mot-clé
            keyword = input("Entrez le mot-clé à rechercher (ex: ERROR, INFO, WARNING) : ")
            results = file_manager.search_keyword(keyword)
            if results:
                print(f"\nLignes contenant '{keyword}' :")
                for result in results:
                    print(result)
            else:
                print(f"\nAucune ligne trouvée contenant le mot-clé '{keyword}'.")

        elif choice == '4':
            print("Fermeture du programme.")
            break

        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
