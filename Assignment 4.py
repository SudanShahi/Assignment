def my_split(sentence, separator):
    """
    Splits a sentence into a list of items using the given separator character.
    """
    result = []
    current_item = ""
    for char in sentence:
        if char == separator:
            result.append(current_item)
            current_item = ""
        else:
            current_item += char
    result.append(current_item)
    return result

def my_join(items, separator):
    """
    Joins a list of items into a string, separated by the given separator character.
    """
    result = ""
    for i, item in enumerate(items):
        result += item
        if i < len(items) - 1:
            result += separator
    return result

def main():
    sentence = input("Please enter sentence: ")
    separator = " "

    split_result = my_split(sentence, separator)

    print(my_join(split_result, ","))

    for word in split_result:
        print(word)

if __name__ == "__main__":
    main()
