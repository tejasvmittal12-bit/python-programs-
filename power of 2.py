input("n & (n-1) clears the rightmost set bit. Press enter")
print("12 & 11 =", 12 & 11, "binary:", bin(12 & 11)[2:])
print(" 8 & 7 =", 8 & 7)

n = int(input("Enter a number (try 4 or 6): "))
guess = input(" Is " + str(n) + " a power of 2? (yes/no): ")
input("Power of 2: n & (n-1) == 0 means only one bit is on. Press enter")
if n > 0 and (n & (n - 1)) == 0:
    print(" ", n, "binary " , bin(n)[2:], " power of 2: yes your guess:", guess)
else:
    print(" ", n, "binary " , bin(n)[2:], " power of 2: no your guess:", guess)