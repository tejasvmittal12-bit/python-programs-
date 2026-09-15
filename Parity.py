# 03-parity-bits.py
# Topic: Parity Check and Counting Bits

input("Parity - last bit = 0 even, last bit = 1 odd. Press Enter ")
for n in [2, 3, 4, 5, 6, 9]:
    if n & 1:
        print(" ", n, "-> odd")
    else:
        print(" ", n, "-> even")

n = int(input("Enter a number (try 13 or 7): "))
input("Count the 1s - wants bits drop off. Press Enter ")

temp = n
while temp > 0:
    print("binary:", bin(temp)[2:], " last bit:", temp & 1)
    temp >>= 1

print("total 1s in", n, "=", bin(n).count('1'))