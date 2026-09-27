# ================================
# POWER OF TWO SCANNER
# ================================
# Topics:
# n & (n-1) Trick | Power of 2 Check | Power of 4 Check
# Power of 8 Check | Binary Exponentiation

print("================================")
print("POWER OF TWO SCANNER")
print("================================")


# ------------------------------------------------
# PART 1 — THE n & (n-1) TRICK
# ------------------------------------------------

n = 16

print("PART 1: The n & (n-1) Trick")
print("n       =", n, "->", bin(n))
print("n - 1   =", n - 1, "->", bin(n - 1))
print("n&(n-1) =", n & (n - 1), "->", bin(n & (n - 1)))

print("This trick removes the rightmost set bit.")


# ------------------------------------------------
# PART 2 — POWER OF 2 CHECK
# ------------------------------------------------

def is_power_of_2(num):
    return num > 0 and (num & (num - 1)) == 0


print("================================")
print("PART 2: Power of 2 Check")
print("================================")

numbers = [1, 2, 4, 6, 8, 12, 16, 18, 32]

for num in numbers:
    print(num, "->", bin(num), "->", is_power_of_2(num))


# ------------------------------------------------
# PART 3 — POWER OF 4 CHECK
# ------------------------------------------------

def is_power_of_4(num):
    if not is_power_of_2(num):
        return False

    position = 0

    while num > 1:
        num = num >> 1
        position = position + 1

    return position % 2 == 0


print("================================")
print("PART 3: Power of 4 Check")
print("================================")

for num in numbers:
    print(num, "->", is_power_of_4(num))


# ------------------------------------------------
# PART 4 — POWER OF 8 CHECK
# ------------------------------------------------

def is_power_of_8(num):
    if not is_power_of_2(num):
        return False

    position = 0

    while num > 1:
        num = num >> 1
        position = position + 1

    return position % 3 == 0


print("================================")
print("PART 4: Power of 8 Check")
print("================================")

for num in numbers:
    print(num, "->", is_power_of_8(num))


# ------------------------------------------------
# PART 5 — BINARY EXPONENTIATION
# ------------------------------------------------

def binary_power(base, exponent):
    answer = 1

    while exponent > 0:
        if exponent & 1:
            answer = answer * base

        base = base * base
        exponent = exponent >> 1

    return answer


print("================================")
print("PART 5: Binary Exponentiation")
print("2^5 =", binary_power(2, 5))
print("3^4 =", binary_power(3, 4))
print("5^3 =", binary_power(5, 3))


# FINAL SUMMARY

print("================================")
print("POWER SCANNER SUMMARY")
print("================================")
print("Power of 2: only one bit is set.")
print("Power of 4: set-bit position is even.")
print("Power of 8: set-bit position is divisible by 3.")
print("Binary exponentiation calculates powers quickly.")
print("================================")
