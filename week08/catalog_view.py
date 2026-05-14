class CatalogView:

    def display_items(self, items):
        
        for item in items:
            print(item)

        if not items:
            print("No items to display")
            return
        
    def display_message(self, message):
        
        print(message)

    def display_menu(self):
        
        print("\n" + "*" * 55 )
        print("%32s" % ("Library Catalog System"))
        print("*" * 55 + "\n")
        print("1. List all items")
        print("2. Search by title")
        print("3. Search by author")
        print("4. Check out item")
        print("5. Check in item")
        print("6. Add new item")
        print("7. View checked-out items")
        print("8. Save and quit\n")

    def display_search_results(self, items, query):
        
        print(f"--- Search Results for {query} ---")
        self.display_items(items)
