def tester(givenstring="Too short"):
    """
    This function checks the length of the given string.
    If the length is less than 10, it prints the default message "Too short".
    If the length is 10 or more, it prints the input string.
    """
    if len(givenstring) < 10:
        print("Too short")
    else:
        print(givenstring)

def main():
    """
    Main function to interact with the user.
    Prompts user for input and sends it to the tester function unless 'quit' is entered.
    """
    while True:
        user_input = input("Write something (quit ends): ")
        if user_input.lower() == "quit":
            break
        tester(user_input)

if __name__ == "__main__":
    main()
