def factorial_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


num = 5
print(f"The factorial of {num} is {factorial_loop(num)}")

