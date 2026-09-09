# ================================
# MY TRAIN SEAT FINDER
# ================================
# Topics:
# O(log n) | Binary Search | Recursion
# Recursive Time Complexity | Space Complexity and Call Stack
# Complexity Ladder

# Sorted train seat numbers
seat_numbers = [101, 104, 108, 112, 115, 120, 125, 130, 135, 140, 145, 150]
target_seat = 130

print("================================")
print("MY TRAIN SEAT FINDER")
print("================================")
print("Available Seats:", seat_numbers)
print("Seat to Find:", target_seat)


# PART 1 — BINARY SEARCH
# Algorithm:
# Check the middle seat.
# If the target seat is smaller, search the left half.
# If the target seat is bigger, search the right half.
# Repeat until the seat is found or the search area becomes empty.
# Time Complexity: O(log n)
# Space Complexity: O(1)

def binary_search(seats, target):
    low = 0
    high = len(seats) - 1
    steps = 0

    while low <= high:
        steps = steps + 1
        mid = (low + high) // 2
        print("Checking middle seat:", seats[mid])

        if seats[mid] == target:
            return mid, steps
        elif target < seats[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1, steps


index, steps = binary_search(seat_numbers, target_seat)

print("Binary Search Result:")
if index != -1:
    print("Seat found at index:", index)
else:
    print("Seat not found.")

print("Steps Taken:", steps)
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# PART 2 — RECURSIVE BINARY SEARCH
# Recursion:
# A function calls itself to solve a smaller version of the same problem.
# Recursive Time Complexity: O(log n)
# Space Complexity: O(log n), because each recursive call uses the call stack.

def recursive_binary_search(seats, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    print("Recursive check:", seats[mid])

    if seats[mid] == target:
        return mid
    elif target < seats[mid]:
        return recursive_binary_search(seats, target, low, mid - 1)
    else:
        return recursive_binary_search(seats, target, mid + 1, high)


recursive_index = recursive_binary_search(
    seat_numbers,
    target_seat,
    0,
    len(seat_numbers) - 1
)

print("Recursive Binary Search Result:")
if recursive_index != -1:
    print("Seat found at index:", recursive_index)
else:
    print("Seat not found.")

print("Recursive Time Complexity: O(log n)")
print("Space Complexity: O(log n) because of the call stack")


# PART 3 — COMPLEXITY LADDER
print("================================")
print("COMPLEXITY LADDER")
print("================================")
print("O(1): Directly checking one fixed seat")
print("O(log n): Binary search by cutting the list in half")
print("O(n): Checking every seat one by one")
print("O(n²): Comparing every seat with every other seat")
print("================================")


# FINAL SUMMARY
print("SUMMARY")
print("Binary search is faster than checking every seat one by one.")
print("It works only when the seat list is sorted.")
print("Recursive binary search also uses O(log n) time.")
print("However, recursion uses extra space in the call stack.")