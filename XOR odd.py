input("XOR all numbers - pairs cancel, the odd one stays. Press enter")
print(" list: [2,3,4,3,2]")
print("odd-occuring:", 2 ^ 3 ^ 4 ^ 3 ^ 2)

n = int(input("Enter a number (try 7 or 11): "))
nums = [3, n, 5, 3, 5]
guess = input("Which numbers in " + str(nums) + " appears once ? ")
result = 0
for x in nums:
    result ^= x
print("XOR cancels pairs - the odd one survives. Press Enter")
print(" list:", nums, "odd-occuring:", result, "your guess :  ", guess)   