# Menu-driven Program Example

entry = "y"
while entry == "y":
    print ("""
Menu options:
1. Burger
2. Hot dog
3. Pasta
4. Pizza
5. Salad""")
    
    choice = int(input("\nPlease select your menu choice: "))

    if choice == 1:
        print ("Your choice is Burger")

    elif choice == 2:
        print ("Your choice is Hot dog")

    elif choice == 3:
        print ("Your choice is Pasta")

    elif choice == 4:
        print ("Your choice is Pizza")

    elif choice == 5:
        print ("Your choice is Salad")

    else:
        print ("Invalid entry - try again.")

    entry = input("\nChoose again? (y/n) ")

input("\nPress enter to exit.")
