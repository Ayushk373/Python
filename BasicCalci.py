def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error! Division by zero."

print(f"Addition: {add(10, 5)}")
print(f"Division: {divide(10, 0)}")
