"""
====================================================================================================================
Interview Definition (1 Line):
====================================================================================================================
Finding the largest element in an array means traversing the array once and updating 
the maximum value whenever a larger element is found.
"""


"""
==================================================================================================================
Algorithm:
==================================================================================================================
"""
# 1. Assume the first element is the largest.

# 2. Traverse the array.

# 3. Compare each element with the current largest.

# 4. If a larger element is found, update the largest value.

# 5. Print the largest element.


# Code 
arr = [10, 25, 7, 89, 45]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)


# Pythonic Solution (Built-in)

arr = [10, 25, 7, 9, 45]
print(max(arr))