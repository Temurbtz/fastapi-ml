def find_kth_largest(nums, k):
    largest = [float('-inf')] * k

    for num in nums:
        for j in range(k):
            if num > largest[j]:
                for m in range(k - 1, j, -1):
                    largest[m] = largest[m - 1]
                largest[j] = num
                break

    return largest[-1]

kth_largest = find_kth_largest([3, 2, 1, 5, 6, 4], 2)
print(kth_largest) 