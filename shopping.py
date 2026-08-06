# ================================
# MY SHOPPING LIST MANAGER
# ================================

# File name
file_name = "shopping_list.txt"


# PART 1 - WRITING TO A FILE

shopping_file = open(file_name, "w")

shopping_file.write("Shopping List\n")
shopping_file.write("1. Milk\n")
shopping_file.write("2. Bread\n")
shopping_file.write("3. Eggs\n")
shopping_file.write("4. Apples\n")

shopping_file.close()

print("Shopping list created successfully!")


# PART 2 - OPENING AND READING A FILE

shopping_file = open(file_name, "r")

print("\n===== Full Shopping List =====")
content = shopping_file.read()
print(content)

shopping_file.close()


# PART 3 - APPENDING TO A FILE

shopping_file = open(file_name, "a")

shopping_file.write("5. Rice\n")
shopping_file.write("6. Butter\n")
shopping_file.write("7. Juice\n")

shopping_file.close()

print("New items added to the shopping list!")


# PART 4 - READING THE UPDATED FILE

shopping_file = open(file_name, "r")

print("\n===== Updated Shopping List =====")
updated_content = shopping_file.read()
print(updated_content)

shopping_file.close()


# PART 5 - READING LINE BY LINE

shopping_file = open(file_name, "r")

print("\n===== Reading Shopping List Line by Line =====")

line_number = 1

for line in shopping_file:
    print("Line", line_number, ":", line.strip())
    line_number = line_number + 1

shopping_file.close()


# FINAL SUMMARY

print("\n================================")
print("SHOPPING LIST MANAGER SUMMARY")
print("================================")
print("File created:", file_name)
print("Items were written, appended, and read successfully.")
print("================================")