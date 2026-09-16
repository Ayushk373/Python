# 1. Open file in write mode
f = open("data.txt", "w")

# 2. Write data
f.write("Hello Python\n")
f.write("Data Structures\n")
f.write("NPTEL Exam")

# 3. Close file
f.close()


# 4. Open file in read mode
f = open("data.txt", "r")

# 5. Read entire file
print("READ:")
print(f.read())

# 6. Close file
f.close()


# 7. Open again for reading
f = open("data.txt", "r")

# 8. Read one line
print("\nREADLINE:")
print(f.readline())

# 9. Read remaining lines as a list
print("READLINES:")
print(f.readlines())

f.close()


# 10. Open file and check position
f = open("data.txt", "r")

print("\nTELL:")
print(f.tell())

# 11. Move pointer to beginning
f.seek(0)

print("After SEEK:")
print(f.tell())

f.close()


# 12. Append new data
f = open("data.txt", "a")

f.write("\nPython is easy")

f.close()
