shopping_list = ()

def display_menu():
           print("Shopping list manager")
           print("1. Add item")
           print("2. Remove item")
           print("3. View list")
           print("4. Exit")


def add_items(shopping_list):
    item = input("Add item: ")
    shopping_list.append(item)
    print(f"{item} has been successfully added.")
def remove_item(shopping_list):
    item = input("Remove item:")
    if item in shopping_list:
        shopping_list.remove (item)
        print(f"{item} succesfully removed")
    else:
        print(f"{item} not found")
def display_list(shopping_list):
     if shopping_list:     
      print(shopping_list)
      for item in shopping_list:
          print(f" -{item}")
     else:
         print("No shopping list.")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_items(shopping_list)
            pass
        elif choice == '2':
            remove_item(shopping_list)
            pass
        elif choice == '3':
            display_list(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    


