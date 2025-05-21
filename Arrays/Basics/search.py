# searching operation in array
def find_element(arr, n, value):
    for i in range(n):
        if (arr[i] == value):
            return i
    return -1

# Output
arr = [10, 20, 30, 40, 50]
n = len(arr)
value = 30
position = (find_element(arr, n, value))
print(f"found element {value} at position {position}")




