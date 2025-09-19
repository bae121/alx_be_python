# User's number
number = int(input("Enter a number to see its multiplication table: "))

# Usage of 'for loop' to print the multiplication table from 1 to 10
for i in range(1, 11):  # < this loops through numbers 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")
