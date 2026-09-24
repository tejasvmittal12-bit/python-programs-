input("Binary exponentiation uses both bits of the exponent. Press enter")
print(" 2^8 = 256 exponent 8 = binary"," bin(8)[2:]")
print(" 2^5 = 32 exponent 5 = binary"," bin(5)[2:]")

exp = int(input("Enter an exponent (try 3 or 6): "))
print("   exponent", exp, "binary", bin(exp)[2:])
guess = input("What is 2^" + str(exp) + "? ")
input("Binary exponentiation reads bits of the exponent. Press enter")
print(" 2^" + exp + " = ", 2 ** exp, "your guess:", guess)