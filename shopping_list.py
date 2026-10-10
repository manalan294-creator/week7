shopping_list = []

while True:
    choice = input("add / remove / show / done: ").strip().lower()

    if choice == "add":
        item = input("Enter an item: ").strip()
        shopping_list.append(item)

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("That item is not on your list.")

    elif choice == "show":
        for item in shopping_list:
            print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select add, remove, show, or done.")
