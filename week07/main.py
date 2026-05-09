from word_collection import WordCollection
from story_template import TEMPLATES

def display_summary(words):
    count = {
        "adj": 0,
        "adv": 0,
        "n": 0,
        "prep": 0,
        "v": 0
    }

    for word in words:
        count[word.part_of_speech] += 1
    
    print(f"\nLoaded {len(words)} words:")

    for pos in sorted(count):
        print(f"\t{pos}: {count[pos]}")

def choose_template():
    print("\nAvailable story styles:")

    for i, template in enumerate(TEMPLATES, start=1):
        print(f"\t{i}. {template.name}")
    
    while True:
        try:
            choice = int(input("Choose a style: "))

            if 1 <= choice <= len(TEMPLATES):
                return TEMPLATES[choice - 1]
            print("Invalid entry")
        except ValueError:
            print("Please enter a number")

def main():
    print("\n" + "*" * 55 )
    print("%32s" % ("StoryTeller"))
    print("*" * 55 + "\n")

    filepath = input("Enter path to word file: ")

    try:
        words = WordCollection.from_file(filepath)
    except FileNotFoundError:
        print("File was not found")
        return
    
    display_summary(words)
    
    while True:
        template = choose_template()

        while True:
            try:
                sentences = int(input("How many sentences? "))
                if sentences > 0:
                    break
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a whole number")
        
        print(f"\n----- {template.name} Story -----")

        for _ in range(sentences):
            print(template.generate(words))

        another_story = input("\n Generate another story? (yes/no): ")

        if another_story != "yes":
            break
    
    print("\nThank you for using StoryTeller :D")

if __name__ == "__main__":
    main()