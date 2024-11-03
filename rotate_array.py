def rotate(nums, k):
    n = len(nums)
    k = k % n
    if k == 0:
        return

    temp = [0] * n
    for i in range(n):
        new_position = (i + k) % n
        temp[new_position] = nums[i]
    
    for i in range(n):
        nums[i] = temp[i]

arr = [1, 2, 3, 4, 5, 6, 7]
rotate(arr, 3)
print(arr)  
