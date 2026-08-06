n = int(input("How many characters to preview? "))
file = open("class-notes.txt", "r")
print(file.read(n)) 
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
print("Total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

word = input("Skip lines starting with: ")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("Skip ->", line.strip())
    else:
        print("Keep ->", line.strip())
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
out = open("odd-lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd linessaved to odd-lines.txt")
file = open("class-notes.txt", "a")
print("Maths notes are completed")
file.write("Maths notes are completed\n")
file.write("Science notes are completed\n")
file.write("History notes are not completed\n")
file.write("English notes are half completed\n")
file.close()