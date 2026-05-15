from book import Book
from dvd import DVD
from magazine import Magazine

class ItemFactory:
    
    @classmethod
    def create_item(cls, type, title, author, year, *type_specific):
        type =  type.lower()

        if type == "book":
            return Book(title, author, year, type_specific[0], type_specific[1])
        elif type == "dvd":
            return DVD(title, author, year, type_specific[0], type_specific[1]) 
        elif type == "magazine":
            return Magazine(title, author, year, type_specific[0], type_specific[1]) 
        else:
            raise ValueError("Unknown type")
        
