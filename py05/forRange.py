number = input("Input a number to iterate from 1 to it: ")
number = int(number)

for i in range(number):

    if number == 0:
        print(f"The number {number} has been inserted, breaking the code...")
        break
    print(f"{(i + 1)}")
    

print("")

for i in range(1, (number + 1)):

    if number == 0:
        print(f"The number {number} was inserted, breaking the code...")
        break

    print(f"{i}")

print("")

for i in range(1, (number + 1), 2):

    if number == 0:
        print(f"The number {number} was inputed, breaking the code...")
        break
    print(f"{i}")