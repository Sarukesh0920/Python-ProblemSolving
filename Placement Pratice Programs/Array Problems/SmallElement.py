def small_arr(arr):
    smaller=arr[0]
    for num in arr:
        if num<smaller:
            smaller=num
    return smaller

arr=[9,7,8,5,3,6]
print("Smallest number is:",small_arr(arr))