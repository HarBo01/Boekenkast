# boekenkast = []

# while True:
#     boeken_titel = input("Boektitel invoeren in je boekenkast!")
#     auteur_boeken = input("Schrijver boeken invoeren!")


#     if boeken_titel or auteur_boeken == 'nee':
#         break
#     boekenkast.append (boeken_titel)

# AFBLIJVEN OP STRAFFE DES DOODS

# mijn_boekenkast = []


# while True:
#     boek = input("Voer een boek in om aan de boekenkast toe te voegen (of typ 'Q' om te stoppen): ")
#     if boek == 'q' or boek == 'Q':
#         break
#     mijn_boekenkast.append(boek)


# print("Mijn boekenkast:", mijn_boekenkast)

import json

books: list[dict] = []
categories = ['Schaakboeken', 'Romans', 'Oorlog']


def add_book(title: str, author: str, category: str):
    """Add_book"""
    book = {'title': title, 'author': author, 'category': category}
    books.append(book)

# TODO: Validatie input gebruiker, stel ik doe "cyd" of "8"


def choose_category():
    print("Kies uit een van de volgende categorieen")
    for index, category in enumerate(categories, 1):
        print(f"{index}: {category}")
    choice = int(input())
    return categories[choice-1]

# (schaakboeken, 1), (Romans, 2), (Oorlog, 3)


def input_book():
    title = input("Geef een titel op\n")
    author = input("Geef een author\n")
    category = choose_category()
    add_book(title, author, category)


def print_books():
    for book in books:
        print(book)


def save_books():
    with open("Boekenkast.json", "w") as file:
        json.dump(books, file)


def load_books():
    with open("Boekenkast.json", "r") as file:
        loaded_books = json.load(file)
        for book in loaded_books:
            books.append(book)


load_books()
while True:
    print("1. Boek toevoegen")
    print("2. Toon boekenkast")
    print("3. Boeken opslaan")
    print("Q om af te sluiten")

    choice = input("Maak uw keuze!\n")
    if choice == 'Q':
        break
    elif choice == '1':
        input_book()
    elif choice == '2':
        print_books()
    elif choice == '3':
        save_books()
        print("Boeken zijn met succes opgeslagen")
