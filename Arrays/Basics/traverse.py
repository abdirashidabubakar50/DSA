# This operation traverses through all the elements present in linear Array
def traverse_array(arr, n):
    for i in range(n):
        print(arr[i])
arr = [10, 20 , 30, 40, 50]
n = len(arr)
print("All the elements in the array are: ")
traverse_array(arr, n)

