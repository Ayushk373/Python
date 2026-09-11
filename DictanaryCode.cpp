# 1. Create a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
print("Original dictionary:", student)

# 2. Access a value using its key
print("Student Name:", student["name"])

# 3. Add a new key-value pair
student["gpa"] = 3.8

# 4. Update an existing value
student["age"] = 22

print("After updates:", student)

# 5. Delete a key-value pair
del student["major"]

# 6. Loop through the dictionary (Key and Value)
print("\nLooping through the items:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
