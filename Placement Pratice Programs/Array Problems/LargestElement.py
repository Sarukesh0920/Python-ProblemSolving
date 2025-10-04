def large_arr(arr):
    element=arr[0]
    for i in arr:
        if i>element:
            element=i
    return element

arr=[5,9,4,6,7,8]
print("Largest number is :",large_arr(arr))
