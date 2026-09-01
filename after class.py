# ================================
# MY RUNNING LAP TRACKER
# ================================
# Topics:
# Algorithm | Pseudocode | Time Complexity | Space Complexity
# One Problem, Three Solutions | Comparing Algorithm Efficiency

# Problem:
# A runner completes laps.
# Lap 1 = 1 point, Lap 2 = 2 points, Lap 3 = 3 points, and so on.
# Find the total running points after n laps using three different solutions.

n = 5

print("================================")
print("MY RUNNING LAP TRACKER")
print("================================")
print("Number of laps:", n)
print()


# ------------------------------------------------
# SOLUTION 1 - FORMULA METHOD
# ------------------------------------------------
# Algorithm:
# Use the formula n * (n + 1) / 2 to calculate total points directly.
#
# Pseudocode:
# START
#   total = n * (n + 1) / 2
#   print total
# END
#
# Time Complexity: O(1)
# Space Complexity: O(1)

formula_total = n * (n + 1) // 2

print("Solution 1: Formula Method")
print("Total Running Points:", formula_total)
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")
print()


# ------------------------------------------------
# SOLUTION 2 - LOOP METHOD
# ------------------------------------------------
# Algorithm:
# Start total from 0.
# Add each lap number one by one.
#
# Pseudocode:
# START
#   total = 0
#   FOR lap FROM 1 TO n
#       total = total + lap
#   print total
# END
#
# Time Complexity: O(n)
# Space Complexity: O(1)

loop_total = 0
steps_loop = 0

for lap in range(1, n + 1):
    loop_total = loop_total + lap
    steps_loop = steps_loop + 1

print("Solution 2: Loop Method")
print("Total Running Points:", loop_total)
print("Steps Taken:", steps_loop)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print()


# ------------------------------------------------
# SOLUTION 3 - NESTED LOOP METHOD
# ------------------------------------------------
# Algorithm:
# For each lap, count points one by one using another loop.
#
# Pseudocode:
# START
#   total = 0
#   FOR lap FROM 1 TO n
#       FOR point FROM 1 TO lap
#           total = total + 1
#   print total
# END
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

nested_total = 0
steps_nested = 0

for lap in range(1, n + 1):
    for point in range(1, lap + 1):
        nested_total = nested_total + 1
        steps_nested = steps_nested + 1

print("Solution 3: Nested Loop Method")
print("Total Running Points:", nested_total)
print("Steps Taken:", steps_nested)
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
print()


# ------------------------------------------------
# COMPARING ALGORITHM EFFICIENCY
# ------------------------------------------------

print("================================")
print("ALGORITHM EFFICIENCY COMPARISON")
print("================================")
print("Formula Method: Fastest because it uses only 1 calculation.")
print("Loop Method: Slower because it repeats once for every lap.")
print("Nested Loop Method: Slowest because it uses a loop inside another loop.")
print()
print("Best Method: Formula Method")
print("Reason: It has O(1) time complexity, so it stays fast even when laps increase.")
print("================================")