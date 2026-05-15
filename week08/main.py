import os
from catalog import Catalog
from catalog_view import CatalogView
from item_factory import ItemFactory

DATA_FILE = os.path.join("data", "catalog.tsv")

def load_catalog(catalog, filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                fields = line.strip().split("\t")

                type = fields[0]
                title = fields[1]
                author = fields[2]
                year = fields[3]


                checked_out = fields[-1].lower() == "true"

                type_specific = fields[4:-1]

                item = ItemFactory.create_item(type, title, author, year, *checked_out)

                if checked_out:
                    item.check_out()

                catalog.add_item(item)
    except FileNotFoundError:
        print("File was not Found. Starting empty")


def save_catalog(catalog, filename):
    with open(filename, "w") as file:
        for item in catalog.get_all_items():

            if item.get_item_type() == "Book":
                line = (f"Book\t, {item.title}\t, {item.author}\t, {item.year}\t, {item.isbn}\t, {item.page_count}\t, {str(item.checked_out)}\n")
            elif item.get_item_type() == "DVD":
                line = (f"DVD\t, {item.title}\t, {item.author}\t, {item.year}\t, {item.runtime_minutes}\t, {item.rating}\t, {str(item.checked_out)}\n")
            else:
                line = (f"Magazine\t, {item.title}\t, {item.author}\t, {item.year}\t, {item.issue_number}\t, {item.month}\t, {str(item.checked_out)}\n")
            
            file.write(line)


def add_item_interactive(catalog, view):
    try:
        type = input("Enter Type (Book, DVD, Magazine): ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        year = int(input("Enter Year: "))

        if type.lower() == "book":
            isbn = input("Enter ISBN: ")
            page_count = int(input("Enter Page Count: "))

            item = ItemFactory.create_item(type, title, author, year, isbn, page_count)
        
        elif type.lower() == "dvd":
            runtime = int(input("Enter Runtime Minutes: "))
            rating = input("Enter Rating: ")

            item = ItemFactory.create_item(type, title, author, year, runtime, rating)
        
        elif type.lower() == "magazine":
            issue_number = int(input("Enter Issue Number: "))
            month = input("Enter Month: ")

            item = ItemFactory.create_item(type, title, author, year, issue_number, month)

        else:
            raise ValueError("Invalif Type, Please try again")
        
        catalog.add_item(item)
        
        view.display_message(f"Added: {title}\n")
    
    except ValueError as error:
        view.display_message(f"There was an error! :( {error}\n")


def main():
    catalog = Catalog()
    view = CatalogView()

    load_catalog(catalog, DATA_FILE)
    view.display_message("Catalog loaded")

    while True:
        view.display_menu()
        choice = input("Enter Choice: \n")

        try:
            if choice == "1":
                view.display_items(catalog.get_all_items())
            elif choice == "2":
                title = input("\nEnter title to search: ")
                result = catalog.search_by_title(title)
                view.display_search_results(result, title)
            elif choice == "3":
                author = input("\nEnter author to search: ")
                result = catalog.search_by_author(author)
                view.display_search_results(result, author)
            elif choice == "4":
                title = input("\nEnter the exact title to check out: ")
                found = False
                for item in catalog.get_all_items():
                    if item.title.lower() == title.lower():
                        item.check_out()
                        view.display_message(f"Successfully checked out: {title}")
                        found = True
                        break
                if not found:
                    view.display_message("Item was not found")
            elif choice == "5":
                title = input("\nEnter the exact title to check in: ")
                found = False
                for item in catalog.get_all_items():
                    if item.title.lower() == title.lower():
                        item.check_in()
                        view.display_message(f"Successfully checked in: {title}")
                        found = True
                        break
                if not found:
                    view.display_message("Item was not found")
            elif choice == "6":
                add_item_interactive(catalog, view)
            elif choice == "7":
                view.display_items(catalog.get_checked_out_items())
            elif choice == "8":
                save_catalog(catalog, DATA_FILE)
                view.display_message("Catalog saved. Goodbye!")
                break
            else:
                view.display_message("Invalid choice")
        except RuntimeError as error:
            view.display_message(f"There was an error: {error}")

if __name__ == "__main__":
    main()