input ("Xor with 0 keeps the number. Press Enter")
print(" 5 ^ 0 =", 5 ^ 0)
print(" 9 ^ 0 =", 9 ^ 0)

input("XOR with itself gives 0. Press Enter")
print(" 5 ^ 5 =", 5 ^ 5)
print(" 9 ^ 9 =", 9 ^ 9)

n = int(input("Enter a number (try 6 or 12) "))
guess = input("What is 3 ^ " + str(n) + "^ 3 ")
input("Xor cancels - 3 appears twice so it disappears. Press Enter")
print(" 3 ^", n, "^ 3 =", 3 ^ n ^ 3, "your guess :  ", guess)    