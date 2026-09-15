try:
    # Attempt to run code that might fail
    age = int(input("Enter your age in numbers: "))
    print(f"Next year you will be {age + 1} years old.")
except ValueError:
    # Run this code if a text-to-number error occurs
    print("Error: Please type an actual number (e.g., 25), not letters.")
  
