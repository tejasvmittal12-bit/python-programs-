# ================================
# STUDY NOTES ORGANIZER
# ================================
# Topics:
# with open() as f | split()
# os.path.exists() | os.remove()
# File Merge
 
import os
 
print("================================")
print("STUDY NOTES ORGANIZER")
print("================================")
 
 
# ------------------------------------------------
# SETUP - CREATE SAMPLE NOTES FILES
# ------------------------------------------------
 
science_notes = ["Plants need sunlight and water",
    "The Earth moves around the Sun",
    "Water can change into ice and steam"
]
 
maths_notes = [
    "Addition means finding the total",
    "Subtraction means taking away",
    "Multiplication is repeated addition"
]
 
with open("science-notes.txt", "w") as f:
    f.writelines(science_notes)
 
with open("maths-notes.txt", "w") as f:
    f.writelines(maths_notes)
 
print("Sample notes files created successfully.")
 
 
# ------------------------------------------------
# PART 1 - READ FILE USING with open() as f
# ------------------------------------------------
 
print("PART 1: Science Notes")
 
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
 
 
# ------------------------------------------------
# PART 2 - USE split() TO COUNT WORDS
# ------------------------------------------------
 
print("PART 2: Word Count in Maths Notes")
 
with open("maths-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())
 
 
# ------------------------------------------------
# PART 3 - CHECK IF MERGED FILE EXISTS
# ------------------------------------------------
 
merged_file = "all-study-notes.txt"
 
print("PART 3: Checking Merged File")
 
if os.path.exists(merged_file):
    print(merged_file, "already exists.")
else:
    print(merged_file, "does not exist yet.")
 
 
# ------------------------------------------------
# PART 4 - REMOVE OLD MERGED FILE IF IT EXISTS
# ------------------------------------------------
 
print("PART 4: Remove Old File")
 
if os.path.exists(merged_file):
    os.remove(merged_file)
    print("Old merged file removed.")
else:
    print("No old merged file to remove.")
 
 
# ------------------------------------------------
# PART 5 - MERGE TWO FILES INTO ONE
# ------------------------------------------------
 
print("PART 5: Merging Files")
 
with open(merged_file, "w") as output:
    output.write("=== SCIENCE NOTES ===")
 
    with open("science-notes.txt", "r") as science:
        output.write(science.read())
 
    output.write("=== MATHS NOTES =")
 
    with open("maths-notes.txt", "r") as maths:
        output.write(maths.read())
 
print("Science and Maths notes merged successfully.")
 
 
# ------------------------------------------------
# PART 6 - DISPLAY MERGED FILE
# ------------------------------------------------
 
print("Merged Study Notes:")
 
with open(merged_file, "r") as f:
    for line in f:
        print(line.strip())
 
 
# FINAL SUMMARY
 
print("================================")
print("STUDY NOTES ORGANIZER SUMMARY")
print("================================")
print("with open() as f: Used for safe file handling.")
print("split(): Used to count words in each line.")
print("os.path.exists(): Used to check if a file exists.")
print("os.remove(): Used to delete an old file.")
print("File Merge: Science and Maths notes combined into one file.")
print("================================")