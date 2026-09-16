stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Peek
print("Top:", stack[-1])

# Pop
print("Removed:", stack.pop())

print("Stack after pop:", stack)

# Check empty
print("Is empty:", len(stack) == 0)
