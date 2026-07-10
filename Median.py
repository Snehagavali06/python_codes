# Input two sorted arrays
arr1 = [1, 3]
arr2 = [2]

# Merge the arrays
arr = arr1 + arr2
arr.sort()

n = len(arr)

# Find the median
if n % 2 == 0:
    median = (arr[n//2 - 1] + arr[n//2]) / 2
else:
    median = arr[n//2]

print("Median =", median)
