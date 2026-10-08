# ================================
# BINARY SUBSET BUILDER
# ================================
# Topics:
# Power Set | Binary Mask as a Subset Selector
# Bit Probe | Enumerating All Subsets with Two Loops
# Bit Difference

items = ["A", "B", "C"]
n = len(items)
total_subsets = 2 ** n

print("================================")
print("BINARY SUBSET BUILDER")
print("================================")

print("Items:", items)
print("Number of items:", n)
print("Total subsets: 2 ^", n, "=", total_subsets)


# ------------------------------------------------
# PART 1 - POWER SET
# ------------------------------------------------
# A power set contains all possible subsets of a set.
# For n items, total subsets = 2 ^ n.

print("================================")
print("PART 1: Power Set")
print("================================")
print("For", n, "items, we can create", total_subsets, "subsets.")


# ------------------------------------------------
# PART 2 - BINARY MASK AS A SUBSET SELECTOR
# ------------------------------------------------
# Each number from 0 to total_subsets - 1 acts like a binary mask.
# If a bit is 1, the item is selected.
# If a bit is 0, the item is not selected.

print("================================")
print("PART 2: Binary Mask Table")
print("================================")

mask = 0

while mask < total_subsets:
    bit2 = (mask >> 2) & 1
    bit1 = (mask >> 1) & 1
    bit0 = mask & 1

    print("Mask", mask, "-> [C][B][A] =", bit2, bit1, bit0)

    mask = mask + 1


# ------------------------------------------------
# PART 3 - BIT PROBE: CHECKING THE j-th BIT
# ------------------------------------------------
# 1 << j creates a probe with only the j-th bit turned ON.
# mask & probe checks whether that bit is set.

print("================================")
print("PART 3: Bit Probe")
print("================================")

sample_mask = 5   # Binary: 101

print("Sample Mask:", sample_mask)
print("Binary:", bin(sample_mask))

j = 0

while j < n:
    probe = 1 << j

    if sample_mask & probe:
        print("Bit", j, "is set, so item", items[j], "is selected.")
    else:
        print("Bit", j, "is not set, so item", items[j], "is not selected.")

    j = j + 1


# ------------------------------------------------
# PART 4 - ENUMERATING ALL SUBSETS WITH TWO LOOPS
# ------------------------------------------------
# Outer loop: goes through every mask.
# Inner loop: checks every item using a bit probe.

print("================================")
print("PART 4: All Subsets")
print("================================")

mask = 0

while mask < total_subsets:
    subset = []

    j = 0
    while j < n:
        probe = 1 << j

        if mask & probe:
            subset.append(items[j])

        j = j + 1

    print("Mask", mask, "->", subset)

    mask = mask + 1


# ------------------------------------------------
# PART 5 - BIT DIFFERENCE
# ------------------------------------------------
# Bit difference tells how many bit positions are different
# between two numbers.

def bit_difference(a, b):
    difference_count = 0

    while a > 0 or b > 0:
        last_bit_a = a & 1
        last_bit_b = b & 1

        if last_bit_a != last_bit_b:
            difference_count = difference_count + 1

        a = a >> 1
        b = b >> 1

    return difference_count


print("================================")
print("PART 5: Bit Difference")
print("================================")
print("Difference between 12 and 15:", bit_difference(12, 15))
print("12 =", bin(12), "15 =", bin(15))

print("Difference between 21 and 24:", bit_difference(21, 24))
print("21 =", bin(21), "24 =", bin(24))

print("Difference between 8 and 8:", bit_difference(8, 8))
print("8 =", bin(8), "8 =", bin(8))


# FINAL SUMMARY

print("================================")
print("BINARY SUBSET BUILDER SUMMARY")
print("================================")
print("Power Set: All possible subsets of a set.")
print("Binary Mask: A number that selects items using bits.")
print("Bit Probe: Uses 1 << j to check a specific bit.")
print("Two Loops: One loop for masks, one loop for items.")
print("Bit Difference: Counts different bit positions.")
print("================================")