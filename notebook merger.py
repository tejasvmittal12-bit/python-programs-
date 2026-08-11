import os

print("===Science Notes===")
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("===Word Count===")
with open("math-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words -> ", line.strip())
print()

print("===Merging Notes===")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists. Overwriting.")
else:
    print("Creating all-notes.txt.")

content = ""
with open("science-notes.txt", "r") as f:
    content += "---science-notes.txt---\n"
    content += f.read() + "\n"
with open("math-notes.txt", "r") as f:
    content += "---math-notes.txt---\n"
    content += f.read() + "\n"
with open("all-notes.txt", "w") as out:
    out.write(content)
print("Saved to all-notes.txt")
print()

if os.path.exists("all-notes.txt"):
    os.remove("all-notes.txt")
    print("Deleted all-notes.txt")
else:
    print("all-notes.txt does not exist.")