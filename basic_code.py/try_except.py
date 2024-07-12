while True:
    try:
        # Benutzereingabe
        user_input = input("Bitte geben Sie eine ganze Zahl ein: ")
        
        # Versuch, die Eingabe in eine ganze Zahl umzuwandeln
        number = int(user_input)
        
        # Wenn die Umwandlung erfolgreich ist, wird die Schleife beendet
        break
    except ValueError:
        # Wenn eine ValueError auftritt, wird diese Nachricht ausgegeben und die Schleife beginnt von vorne
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")

# Fortsetzung des Codes mit der gültigen Eingabe
print(f"Sie haben die Zahl {number} eingegeben.")