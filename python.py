import json
import os

def save_input(data, filename):
    # Öppna filen i läge 'w' (skrivläge) och spara datan som JSON
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_input(filename):
    # Kontrollera om filen existerar
    if os.path.exists(filename):
        # Öppna filen i läge 'r' (läsläge) och ladda datan från JSON
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        # Skriv ut meddelande om filen inte finns
        print("Inget sparat")
        return None

# Uppgift 2: Spara inmatning
input_data = input("Skriv något att spara: ")
save_input(input_data, 'saved_input.json')

# Uppgift 3: Läs inmatning och skriv ut om filen inte existerar
saved_data = load_input('saved_input.json')

# Uppgift 5: Spara flera saker med bibliotek och JSON-format
multiple_items = {'item1': 'value1', 'item2': 'value2', 'item3': 'value3'}
save_input(multiple_items, 'multiple_items.json')

# Uppgift 6: Spara/uppdatera en lista med saker/namn
list_of_items = ['item1', 'item2', 'item3']
save_input(list_of_items, 'list_of_items.json')