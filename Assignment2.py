def main():
    shopping_list = []

    while True:
        print("Would you like to")
        print("(1) Add or")
        print("(2) Remove items or")
        print("(3) Quit?: ", end="")
        choice = input()

        if choice == "1":
            item = input("What will be added?: ")
            shopping_list.append(item)
        elif choice == "2":
            list_length = len(shopping_list)
            if list_length == 0:
                print("The list is empty. Nothing to remove.")
            else:
                print(f"There are {list_length} items in the list.")
                try:
                    item_index = int(input("Which item is deleted?: "))
                    if 0 <= item_index < list_length:
                        shopping_list.pop(item_index)
                    else:
                        print("Incorrect selection.")
                except ValueError:
                    print("Incorrect selection.")
        elif choice == "3":
            print("The following items remain in the list:")
            for item in shopping_list:
                print(item)
            break
        else:
            print("Incorrect selection.")

        if __name__ == "__main__":
            main

