# MY SMART SWITCH BIT MONITOR
# ================================
# Topics:
# Set Bits and Zero Bits | Counting Set Bits | First Set Bit
# Building a Bit Mask | Check if the Nth Bit is Set

# Each bit represents one smart switch:
# Bit 0 = Living Room Light
# Bit 1 = Fan
# Bit 2 = Air Conditioner
# Bit 3 = Door Lock
# Bit 4 = Garden Light
# Bit 5 = Security Camera

switch_value = 45   # Binary: 101101


def show_bits(number):
    return bin(number)[2:]


print("================================")
print("MY SMART SWITCH BIT MONITOR")
print("================================")

print("Switch Value:", switch_value)
print("Binary Form:", show_bits(switch_value))


# ------------------------------------------------
# PART 1 — SET BITS AND ZERO BITS
# ------------------------------------------------

binary_value = show_bits(switch_value)

set_bits = binary_value.count("1")
zero_bits = binary_value.count("0")

print("PART 1: Set Bits and Zero Bits")
print("Set Bits / ON Switches:", set_bits)
print("Zero Bits / OFF Switches:", zero_bits)


# ------------------------------------------------
# PART 2 — COUNTING SET BITS
# ------------------------------------------------

count = 0
temp = switch_value

while temp > 0:
    if temp & 1:
        count = count + 1
    temp = temp >> 1

print("PART 2: Counting Set Bits")
print("Number of ON switches:", count)


# ------------------------------------------------
# PART 3 — THE FIRST SET BIT
# ------------------------------------------------

position = 1
temp = switch_value

while temp > 0:
    if temp & 1:
        break
    position = position + 1
    temp = temp >> 1

print("PART 3: The First Set Bit")
print("First ON switch is at position:", position)


# ------------------------------------------------
# PART 4 — BUILDING A BIT MASK
# ------------------------------------------------

print("PART 4: Building a Bit Mask")

for i in range(6):
    mask = 1 << i
    print("Bit", i, "Mask:", mask, "Binary:", show_bits(mask))


# ------------------------------------------------
# PART 5 — CHECK IF THE NTH BIT IS SET
# ------------------------------------------------

switch_names = [
    "Living Room Light",
    "Fan",
    "Air Conditioner",
    "Door Lock",
    "Garden Light",
    "Security Camera"
]

print("PART 5: Check if the Nth Bit is Set")


for i in range(6):
    mask = 1 << i

    if switch_value & mask:
        print("Bit", i, "-", switch_names[i], "is ON")
    else:
        print("Bit", i, "-", switch_names[i], "is OFF")


# FINAL SUMMARY

print("================================")
print("SMART SWITCH SUMMARY")
print("================================")
print("Switch Value:", switch_value)
print("Binary Form:", show_bits(switch_value))
print("Total ON Switches:", count)
print("First ON Switch Position:", position)
print("================================")