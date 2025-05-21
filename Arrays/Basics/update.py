# updating an existing elment from the array at a given index
def update_array(arr, index, value):
    arr[index] = value

arr = [10, 20 , 30 , 40 , 50]
index = 4
value = 60
update_array(arr, index, value)
print(arr)

