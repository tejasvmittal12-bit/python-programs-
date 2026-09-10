print("Binary to Decimal Converter")

binary = input("Enter a binary number: ")

# Check that only 0 and 1 are entered
if all(digit in "01" for digit in binary):
    decimal = int(binary, 2)

    print("Binary :", binary)
    print("Decimal:", decimal)
else:
    print(" Please enter only 0 and 1.")