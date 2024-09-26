from termcolor import colored

#  our Checklist
checklist = list()

# Define Functions
def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    print("\nCaptain Rainbow's Color Checklist:")
    for index, item in enumerate(checklist):
        print(f"{index}: {colorize_item(item)}")

def mark_completed(index):
    checklist[index] = f"√ {checklist[index]}"

def user_input(prompt):
    return input(prompt).strip().upper()

def colorize_item(item):
    """Color the printed item based on its color."""
    if "red" in item.lower():
        return colored(item, "red")
    elif "blue" in item.lower():
        return colored(item, "blue")
    elif "green" in item.lower():
        return colored(item, "green")
    elif "yellow" in item.lower():
        return colored(item, "yellow")
    elif "purple" in item.lower():
        return colored(item, "magenta")
    elif "cyan" in item.lower():
        return colored(item, "cyan")
    else:
        return item

def select(function_code):
    if function_code == "C":
        item = input("Enter item to add: ")
        create(item)
        print(f"Added item: {colorize_item(item)}")

    elif function_code == "R":
        index = int(input("Enter index to read: "))
        print(f"Item at index {index}: {colorize_item(read(index))}")

    elif function_code == "U":
        index = int(input("Enter index to update: "))
        item = input("Enter new item: ")
        update(index, item)
        print(f"Updated item at index {index} to: {colorize_item(item)}")

    elif function_code == "D":
        index = int(input("Enter index to delete: "))
        print(f"Deleted item: {colorize_item(read(index))}")
        destroy(index)

    elif function_code == "M":
        index = int(input("Enter index to mark as completed: "))
        mark_completed(index)
        print(f"Marked item at index {index} as completed.")

    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        print("Goodbye! Captain Rainbow salutes you.")
        return False

    else:
        print("Unknown Option")
    return True

def test():
    create("Red Paint")
    create("Blue Paint")
    create("Green Paint")
    list_all_items()

# main loop
running = True
while running:
    selection = user_input(
            "\nCaptain Rainbow's Commands:\n"
            "Press C to Add to the list\n"
            "Press R to Read from the list\n"
            "Press U to Update an item\n"
            "Press D to Delete an item\n"
            "Press M to Mark an item as completed\n"
            "Press P to Print the list\n"
            "Press Q to Quit\n"
            "Enter your choice: "
        )
    running = select(selection)