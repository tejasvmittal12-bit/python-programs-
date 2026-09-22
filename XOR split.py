input("XOR all - pairs cancel , two odd-occurring ones remain. Press enter")
print(" [1, 4, 3, 3] XOR of all:", 1 ^ 4 ^ 3 ^ 3, "binary:",bin(1 ^ 4 ^ 3 ^ 3)[2:])
print("split bit 1 ->group A (bit 0 ON): 1  group B (bit 0 OFF): 4")

n=int(input("Enter a number (try 6 or 9): "))
guess = input(" Is bit 0 of " + str(n) + " ON (yes/no):")
input("Check the split bit. Press enter")
if n & 1:
    print(" ", n , "binary:" , bin(n)[2:], "bit 0 ON - group A your guess:", guess)
    print(" ", n , "binary:" , bin(n)[2:], "bit 0 ON - group B your guess:", guess)