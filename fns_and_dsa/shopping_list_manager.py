# shopping_list_manager.py

def display_menu():
    print("\n=== Shopping List Manager ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    if item:
        shopping_list.append(item)
        print(f" '{item}' added to your shopping list.")
    else:
        print(" Item name cannot be empty.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f" '{item}' removed from your shopping list.")
    else:
        print(f" '{item}' not found in your shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("\n Your Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is currently empty.")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye! Thanks for using Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
