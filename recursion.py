n = int(input("Enter n (try 3 or 5):"))
guess = input("How many times does countdown call itself for n = " + str(n) + "? "  )

input("Recursion - watch each call. Press Enter to run ")
def countdown(num):
    print(" call - n =", num)
    if num > 0:
        countdown(num - 1)
countdown(n)
print(" calls =", n + 1, "your guess:", guess, "  -> 0(n)")

input("Watch callsgrow with n. Press Enter")
for size in [ 5, 10, 100]:
    print(" n =", size, " calls =", size + 1, "  -> 0(n)")