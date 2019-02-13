"""
SHOPPING LIST APP

Project Requirements:

As a user, I should continually be  prompted so that I can add a grocery item or view my list when I need to. 

As a user, I should be able to ask for help so that I can understand how to use the application.

As a user, I should be able to add an item for the list.

As a user upon adding an item to a list, I should know my total items.

As a user, I should be able to see the list at any time so that I can verify my order.

As a user I should be able to state when I'm done so that I can print out the list in totality.
"""
#import os library
import os

#create new shopping list
shopping_list = []

#function to add item to list
def add_item_to_list(item):
    shopping_list.append(item)
    #confirm item name and list total
    print("{} has been added to the list. There are {} total items on the list.".format(item,len(shopping_list)))

    
#function to show help menu
def show_help():
    clear_screen()
    print("My Shopping List App")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to show the help menu.
Enter 'PRINT' to print the current list.
Enter 'REMOVE' to remove an item from the list.
Enter 'CLEAR' to clear the screen.

...or just add an item to the bottom of the list by tying the item name below.
""")


#function to print all items in the list
def print_list():
    counter = 1
    for item in shopping_list:
        print("{}. {}".format(counter, item))
        counter += 1


#funtion to remove item
def remove_item():
    print_list()
    try:
        item_to_remove = int(input("Enter item number to remove: "))
        shopping_list.pop((item_to_remove - 1))    
    except IndexError:
        print("{} is not a valid item number...returning to previous screen.".format(item_to_remove))


#function to clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#show help screen
show_help()

#run program unless user types 'DONE'
while True:
    new_item = input("Enter item to add to list: ")
    
    if new_item.upper() == "DONE":
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'PRINT':
        print_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_item()
        continue
    elif len(new_item) < 1:
        print("You must enter a valid item to add it to the list.")
        continue
    elif new_item.upper() == "CLEAR":
        clear_screen()
        show_help()
        continue    
    else:
        add_item_to_list(new_item)

#print final list on exit
print()
print("SHOPPING LIST")
print("-------------")
print_list()