number = 1

while number != 0:
    number = input("Input a number to know if it is even or odd: ")
    number = int(number)
    if number == 0:
        print("Exiting...")
    if number % 2 == 0:
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")