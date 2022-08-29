numberOne = input("Insert the first number: ")
numberTwo = input("Insert the second number: ")

numberOne = int(numberOne)
numberTwo = int(numberTwo)

if numberOne < numberTwo:
    print(f"Number {numberOne} is lower than {numberTwo}")
else:
    print(f"Number {numberOne} is greater than {numberTwo}")