


####-----------------------------------------------------ASSIGNMENT 04--------------------------------------------####

###=================QUESTION #1================================###

def findCommonElements(arr1, arr2, arr3):
    i = j = k = 0
    result = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i += 1
        elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
            j += 1
        else:
            k += 1

    return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
result = findCommonElements(arr1, arr2, arr3)
print(result)


###=================QUESTION #2================================###

def findDistinctIntegers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    distinct_nums1 = list(set1 - set2)
    distinct_nums2 = list(set2 - set1)
    return [distinct_nums1, distinct_nums2]


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDistinctIntegers(nums1, nums2)
print(result)


###=================QUESTION #3================================###

def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            result[j][i] = matrix[i][j]

    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose(matrix)
print(result)


###=================QUESTION #4================================###

def arrayPairSum(nums):
    nums.sort()
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum

nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print(result)


###=================QUESTION #5================================###

def arrangeCoins(n):
    left = 0
    right = n

    while left <= right:
        mid = left + (right - left) // 2
        sum_mid = mid * (mid + 1) // 2

        if sum_mid <= n:
            left = mid + 1
        else:
            right = mid - 1

    return right
    
n = 5
result = arrangeCoins(n)
print(result)
    

###=================QUESTION #6================================###

def sortedSquares(nums):
    result = []

    for num in nums:
        result.append(num * num)

    result.sort()

    return result


nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)


###=================QUESTION #7================================###

def maxCount(m, n, ops):
    min_row = m
    min_col = n

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    return min_row * min_col

m = 3
n = 3
ops = [[2, 2], [3, 3]]
result = maxCount(m, n, ops)
print(result)


###=================QUESTION #8================================###

def shuffle(nums, n):
    nums1 = nums[:n]
    nums2 = nums[n:]
    result = []

    for i in range(n):
        result.append(nums1[i])
        result.append(nums2[i])

    return result

nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
print(result)
