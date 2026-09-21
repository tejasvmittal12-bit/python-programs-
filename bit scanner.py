# ================================
# MY SECRET CODE BIT SCANNER
# ================================
# Topics:
# Bits and Binary | AND and OR | NOT and XOR
# Left Shift and Right Shift | Odd or Even with XOR | Counting Bits

secret_code = 13
access_key = 9


def bits(number, width=4):
    return format(number & ((1 << width) - 1), f"0{width}b")


print("================================")
print("MY SECRET CODE BIT SCANNER")
print("================================")
print("Secret Code:", secret_code, "Binary:", bits(secret_code))
print("Access Key:", access_key, "Binary:", bits(access_key))


# PART 1 - BITS AND BINARY
print("PART 1: Bits and Binary")
print("Binary numbers use only 0 and 1.")
print("Secret Code Binary:", bits(secret_code))
print("Access Key Binary:", bits(access_key))


# PART 2 - AND and OR
and_result = secret_code & access_key
or_result = secret_code | access_key

print("PART 2: AND and OR") 
print("PART 2: AND and OR")
print("AND Result:", and_result, "Binary:", bits(and_result))
print("OR Result:", or_result, "Binary:", bits(or_result))
print("AND keeps only positions where both bits are 1.")
print("OR keeps positions where at least one bit is 1.")


# PART 3 - NOT and XOR
not_result = (~secret_code) & 0b1111
xor_result = secret_code ^ access_key

print("PART 3: NOT and XOR")
print("NOT Secret Code within 4 bits:", not_result, "Binary:", bits(not_result))
print("XOR Result:", xor_result, "Binary:", bits(xor_result))
print("XOR gives 1 when the compared bits are different.")


# PART 4 - LEFT SHIFT and RIGHT SHIFT
left_shift = secret_code << 1
right_shift = secret_code >> 1

print("PART 4: Left Shift and Right Shift")
print("Left Shift Result:", left_shift, "Binary:", bits(left_shift, 5))
print("Right Shift Result:", right_shift, "Binary:", bits(right_shift))
print("Left shift moves bits left. Right shift moves bits right.")


# PART 5 - ODD OR EVEN WITH XOR
xor_check = secret_code ^ 1

print("PART 5: Odd or Even with XOR")
print("Secret Code XOR 1:", xor_check)

if xor_check == secret_code - 1:
    print("Secret Code is Odd because XOR with 1 reduced it by 1.")
else:
    print("Secret Code is Even because XOR with 1 increased it by 1.")


# PART 6 - COUNTING BITS
bit_count = secret_code.bit_count()

print("PART 6: Counting Bits")
print("Number of 1 bits in Secret Code:", bit_count)


# FINAL SUMMARY
print("================================")
print("SECRET CODE SCAN SUMMARY")
print("================================")
print("Secret Code:", secret_code, "Binary:", bits(secret_code))
print("Access Key:", access_key, "Binary:", bits(access_key))
print("AND:", and_result)
print("OR:", or_result)
print("NOT within 4 bits:", not_result)
print("XOR:", xor_result)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)
print("1 Bits Count:", bit_count)
print("================================")