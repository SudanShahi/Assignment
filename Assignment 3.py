def supermarket():
    print("Supermarket")
    print("===========")

    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total_sum = 0

    while True:
        choice = input("Please select product (1-10) 0 to Quit: ")
        try:
            product_num = int(choice)
            if product_num == 0:
                break
            elif 1 <= product_num <= 10:
                price = prices[product_num - 1]
                total_sum += price
                print(f"Product: {product_num} Price: {price}")
            else:
                print("Invalid product number. Please select between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10, or 0 to quit.")


    print(f"Total: {total_sum}")

    while True:
        try:
            payment = int(input("Payment: "))
            if payment >= total_sum:
                change = payment - total_sum
                print(f"Change: {change}")
                break
            else:
                print(f"Insufficient payment. You need at least {total_sum}.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

if __name__ == "__main__":
    supermarket()
