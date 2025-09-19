# User's sizing for square pattern
size = int(input("Enter the size of the pattern: "))

# Row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns (printing asterisks in one row)
    for col in range(size):
        print("*", end="")  # print star without moving to a new line
    print()  # move to the next line after finishing a row
    row += 1
