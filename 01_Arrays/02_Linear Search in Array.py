""""
==================================================================================================================
Interview Definition (1 line):
==================================================================================================================

Linear Search is a searching algorithm that checks each element of an array 
one by one until the required element is found or the array ends.

"""


"""
==================================================================================================================
Algorithm:
==================================================================================================================
"""

# 1. Start from the first element.

# 2. Compare each element with the target value.

# 3. If the element matches, return its index.

# 4. If the end of the array is reached, return Not Found.


# Code 
arr = [10, 20, 30, 40, 50]
key = 30

for i in range(len(arr)):
    if arr[i] == key:
        print("Found at index:", i)
        break
else:
    print("Not Found")
