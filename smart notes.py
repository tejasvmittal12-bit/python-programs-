# ================================
# SMART NOTES ORGANIZER
# ================================
# Topics:
# read(n) | readlines()
# Looping Through a File Line by Line
# Filtering Lines with Conditions
# Copying Selected Lines to a New File
 
print("================================")
print("SMART NOTES ORGANIZER")
print("================================")
 
 
# ------------------------------------------------
# SETUP — CREATE A SAMPLE NOTES FILE
# ------------------------------------------------
 
sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n"
]
 
file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
 
print("Sample file 'class-notes.txt' created successfully.")
 
 
# ------------------------------------------------
# PART 1 — read(n)
# ------------------------------------------------
 
print("\nPART 1: Preview Notes with read(n)")
 
file = open("class-notes.txt", "r")
preview = file.read(40)
file.close()
 
print("First 40 characters:")
print(preview)
 
 
# ------------------------------------------------
# PART 2 — readlines()
# ------------------------------------------------
 
print("\nPART 2: Read All Lines with readlines()")
 
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
 
print("Total lines in file:", len(lines))
 
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
 
 
# ------------------------------------------------
# PART 3 — LOOP THROUGH A FILE LINE BY LINE
# ------------------------------------------------
 
print("\nPART 3: Loop Through File Line by Line")
 
file = open("class-notes.txt", "r")
 
for line in file:
    print("Reading:", line.strip())
 
file.close()
 
 
# ------------------------------------------------
# PART 4 — FILTERING LINES WITH CONDITIONS
# ------------------------------------------------
 
print("\nPART 4: Filter Lines with Conditions")
 
file = open("class-notes.txt", "r")
 
for line in file:
    if line.startswith("SKIP"):
        print("Skipped:", line.strip())
    else:
        print("Kept:", line.strip())
 
file.close()
 
 
# ------------------------------------------------
# PART 5 — COPY SELECTED LINES TO A NEW FILE
# ------------------------------------------------
 
print("\nPART 5: Copy Selected Lines to a New File")
 
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
 
output_file = open("organized-notes.txt", "w")
 
for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        output_file.write(line)
 
output_file.close()
 
print("Selected lines copied to 'organized-notes.txt'.")
 
 
# ------------------------------------------------
# PART 6 — DISPLAY THE ORGANIZED FILE
# ------------------------------------------------
 
print("\nOrganized Notes:")
 
file = open("organized-notes.txt", "r")
 
for line in file:
    print(line.strip())
 
file.close()
 
 
# FINAL SUMMARY
 
print("\n================================")
print("SMART NOTES ORGANIZER SUMMARY")
print("================================")
print("read(n): Previewed the first few characters.")
print("readlines(): Stored all lines in a list.")
print("Loop: Read the file line by line.")
print("Condition: Skipped lines starting with SKIP.")
print("Copy: Saved IMPORTANT and TODO lines into a new file.")
print("================================")