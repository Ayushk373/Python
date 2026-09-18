def fib(n, memo={}):

    # Already calculated?
    if n in memo:
        return memo[n]

    # Base case
    if n <= 1:
        return n

    # Calculate and store
    memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]


print(fib(10))
