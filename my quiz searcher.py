# ================================
# MY QUIZ RESULT SEARCHER
# ================================
# Topics:
# Asymptotic Analysis | Big-O | Omega | Theta
# Best, Average, Worst Case | O(1), O(n), O(n^2)

# A list of quiz scores
quiz_scores = [45, 62, 78, 85, 91, 56, 73, 88]

print("================================")
print("MY QUIZ RESULT SEARCHER")
print("================================")
print("Quiz Scores:", quiz_scores)


# --------------------------------
# PART 1 - O(1): Direct Access
# --------------------------------
# This directly checks the first student's score.
# It takes the same time even if the list becomes bigger.

first_score = quiz_scores[0]

print("PART 1: Direct Access")
print("First Student Score:", first_score)
print("Time Complexity: O(1)")
print("Theta Notation: Theta(1)")
print("Reason: Direct access takes one step.")


# --------------------------------
# PART 2 - O(n): Linear Search
# --------------------------------
# This searches for a target score one by one.
# Best Case: Score is found at the beginning.
# Average Case: Score is found somewhere in the middle.
# Worst Case: Score is found at the end or not found.

target_score = 88
steps = 0
found = False

print("PART 2: Linear Search")
print("Searching for score:", target_score)

for score in quiz_scores:
    steps = steps + 1

    if score == target_score:
        found = True
        print("Score found:", score)
        print("Steps Taken:", steps)
        break

if found == False:
    print("Score not found.")
    print("Steps Taken:", steps)

print("Best Case: Omega(1)")
print("Average Case: O(n)")
print("Worst Case: O(n)")
print("Reason: The program may need to check many scores.")


# --------------------------------
# PART 3 - O(n^2): Pair Comparison
# --------------------------------
# This compares every score with every other score.
# It uses one loop inside another loop.

print("PART 3: Pair Comparison")
pair_steps = 0

for score1 in quiz_scores:
    for score2 in quiz_scores:
        pair_steps = pair_steps + 1

print("Total Pair Checks:", pair_steps)
print("Time Complexity: O(n^2)")
print("Reason: A nested loop compares every score with every other score.")


# --------------------------------
# PART 4 - Best, Average, Worst Case Demo
# --------------------------------

print("PART 4: Case Comparison")

best_case_score = 45
average_case_score = 85
worst_case_score = 88

print("Best Case Target:", best_case_score, "- Found near the beginning")
print("Average Case Target:", average_case_score, "- Found around the middle")
print("Worst Case Target:", worst_case_score, "- Found near the end")


# --------------------------------
# FINAL SUMMARY
# --------------------------------

print("================================")
print("ASYMPTOTIC ANALYSIS SUMMARY")
print("================================")
print("O(1): Direct access is fastest.")
print("O(n): Linear search grows with the number of scores.")
print("O(n^2): Nested loops grow much faster.")
print("Omega(1): Best case for search when the target is found first.")
print("Theta(1): Direct access always takes constant time.")
print("Big-O shows the upper/worst-case growth.")
print("================================")