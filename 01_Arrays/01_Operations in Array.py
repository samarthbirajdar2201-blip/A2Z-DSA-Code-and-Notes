# CREATE - make an array
arr = [10, 20, 30, 40, 50]
print("Array:", arr)

# OUTPUT - print each element
for i in arr:
    print(i)

# INPUT - add value from user
x = int(input("Enter a number to add: "))
arr.append(x)
print("After adding:", arr)

# UPDATE - change value at index 2
arr[2] = 99
print("After update:", arr)

# DELETE - remove value at index 0
del arr[0]
print("After delete:", arr)                                                          