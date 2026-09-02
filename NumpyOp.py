import numpy as np

a= np.array([10,20,30,40,50])
b= np.array([1,2,3,4,5])

addition = np.add(a,b)
print("Array A: ",a)
print("Array B: ",b)
print("Addition using np.add(): ",addition)

numbers= np.array([1,4,9,16,25])
square_root= np.sqrt(numbers)
print("Numbers: ",numbers)
print("Square root using np.sqrt(): ",square_root)

x= np.array([1,2,3,4,5])
exponential= np.exp(x)
print("\nArray X: ",x)  
print("Exponential using np.exp(): ",exponential)

numbers=np.array([1,2,3,4,5])
logarithm=np.log(numbers)
print("\nArray Numbers: ",numbers)
print("Logarithm using np.log(): ",logarithm)

marks= np.array([50,60,70,80,90])
new_marks= marks+5
print("\nOriginal marks: ",marks)
print("Marks after adding 5: ",new_marks)

matrix= np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
addition_value=10
result= matrix + addition_value
print("\nOriginal Matrix: ")
print(matrix)
print("\nMatrix after adding 10 using broadcasting: ")
print(result)
