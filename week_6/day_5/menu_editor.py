#Instructions below

from ex_py import MenuItem

def load_manager(*args):
    return MenuItem(*args)

def show_user_menu():
    #show user menu
    user_input = input('''
    MENU
    (a) Add an item
    (b) Delete an item
    (v) View the menu
    (x) Exit
    ''')
    return user_input

def add_item_to_menu():
    print("Adding a new item to the menu:\n")
    item_name_input = input("What is the item's name?\n")
    item_price_input = input("What is the item's price?\n")
    new_item_to_add = load_manager(item_name_input,item_price_input)
    try:
        new_item_to_add.save()
        print("item was added successfully.\n")
    except:
        print("Error adding item.")


def remove_item_from_menu():
    item_to_remove_input = input("What item do you want to remove?\n")
    try:

        menu_item = MenuItem.get_by_name(item_to_remove_input)
        print(menu_item)
        menu_item.delete()
        print("Item deleted successfully")
    except:
        print("Error - item was not deleted")

def show_restaurant_menu():
    #show all items in menu
    print("This is our restaurant's menu:\n")
    menu_items = MenuItem.all()
    for item in menu_items:
        print(item)


while(user_input := show_user_menu()):
    if user_input == 'v':
        show_restaurant_menu()
    elif user_input == 'b':
        remove_item_from_menu()
    elif user_input == 'a':
        add_item_to_menu()
    elif user_input == 'x':
        show_restaurant_menu()
        break



# Part 2
# Create a file called menu_editor.py , which will have the following functions:
# load_manager()- this function should create a new MenuItem instance.

# show_user_menu() - this function should display the program menu
#  (not the restaurant menu!), and ask the user to choose an item.
#  Call the appropriate function that matches the user’s input.

# add_item_to_menu() - this will ask the user to input the item’s name
#  and price. It will not interact with the menu itself, but simply
#  call the appropriate function from the MenuItem object.
# If the item was added successfully print a message which states: item
#  was added successfully.

# remove_item_from_menu()- this function should ask the user to
#  input the name of the item they want to remove from the restaurant’s
#  menu.
#  The function should not interact with the menu itself, but simply call
#  the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let
# the user know this was completed.
# If not – print a message which states that there was an
# error.

# show_restaurant_menu() - print the restaurant’s
# menu.

# When the user chooses to exit the program, display the
# restaurant menu and exit the program.

# Here’s an example of the menu shown to
#  the user:
# Exercise Menu Manager
