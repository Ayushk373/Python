import numpy as np

# 1. Generate random numbers between 0 and 1
a = np.random.rand(5)
print("Random numbers using rand():")
print(a)

# 2. Generate random numbers from standard normal distribution
b = np.random.randn(5)
print("\nRandom numbers using randn():")
print(b)

# 3. Generate random integers
c = np.random.randint(1, 50, 5)
print("\nRandom integers using randint():")
print(c)


# 4. Generate numbers from normal distribution
d = np.random.normal(50, 10, 5)
print("\nNumbers using normal():")
print(d)

# Calculate statistics
print("\nStatistics of normal distribution:")
print("Mean =", np.mean(d))
print("Median =", np.median(d))
print("Standard Deviation =", np.std(d))
print("Minimum =", np.min(d))
print("Maximum =", np.max(d))
