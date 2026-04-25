from dog import Dog
from cat import Cat
from fish import Fish

def adopt_pet(pets):
    print("\n" + "=" * 65 )
    print("%45s" % ("WELCOME TO PET ADOPTION"))
    print("=" * 65 )
    print("%35s" % ("Animals in adoption: " + "Dog. " + "Cat. " + "Fish."))
    type = input("What animal do you whish to adopt? ")
    name = input("Name your Pet: ")

    if type == "Dog" or type == "dog" or type == "DOG":
        breed = input("Enter dog breed: ")
        pets.append(Dog(name, breed))
    elif type == "Cat":
        pets.append(Cat(name))
    elif type == "Fish":
        pets.append(Fish(name))
    else:
        print("Invalid entry")

def select_pet(pets):
    if not pets:
        print("No pets available")
    
    for p, pet in enumerate(pets):
        print(f"\n{p + 1}. {pet}")
    
    try:
        choice = int(input("\nChoose your pet: ")) - 1
        return pets[choice]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return None

def main():
    pets = []
    while True:
        print("\n" + "=" * 65 )
        print("%40s" % ("Pet - Simulator"))
        print("=" * 65 + "\n")
        print("1. Adopt a pet")
        print("2. feed a pet")
        print("3. Play with a pet")
        print("4. Put a pet to sleep")
        print("5. View all pets")
        print("6. Quit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            adopt_pet(pets)
        elif choice == "2":
            pet = select_pet(pets)
            if pet:
                print(pet.feed())
        elif choice == "3":
            pet = select_pet(pets)
            if pet:
                print(pet.play())
        elif choice == "4":
            pet = select_pet(pets)
            if pet:
                print(pet.sleep())
        elif choice == "5":
            for pet in pets:
                print(pet.status())
        elif choice == "6":
            print("\nThank you! and Goodbay")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()