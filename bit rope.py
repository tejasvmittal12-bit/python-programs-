input("Bit probe - (n >> j ) & 1 checks if bit j is ON. Press Enter")
print("     12 = binary", bin(12)[2:], " bit 2: ", (12 >> 2) & 1 , "bit 1:", (12 >> 1) & 1)
print("     7 = binary", bin(7)[2:], " bit 2: ", (7 >> 2) & 1 , "bit 1:", (7 >> 1) & 1)

n = int(input("Enter a number( try 9 or 6): "))
print("Binary:", bin(n)[2:])
guess = input("What is bit 2 of " + str(n) + " ? (0 or 1):")
input("Bit probe - (n >> 2 ) & 1 give the bit value 2. Press Enter")
print("" , n , "bit 2=", (n >> 2) & 1 , "Your guess:", guess)