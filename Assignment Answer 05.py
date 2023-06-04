



####-----------------------------------------------------ASSIGNMENT 05--------------------------------------------####

###=================QUESTION #1================================###

def construct2DArray(original, m, n):
    if len(original) != m * n:
        return []

    result = [[0] * n for _ in range(m)]

    for i in range(len(original)):
        row = i // n
        col = i % n
        result[row][col] = original[i]

    return result

original = [1, 2, 3, 4]
m = 2
n = 2
result = construct2DArray(original, m, n)
print(result)


###=================QUESTION #2================================###

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

###=================QUESTION #3================================###

def sortedSquares(nums):
    result = []

    for num in nums:
        result.append(num * num)

    result.sort()

    return result


nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)

###=================QUESTION #4================================###

def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    result1 = set1 - set2
    result2 = set2 - set1
    return [list(result1), list(result2)]

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDisappearedNumbers(nums1, nums2)
print(result)


###=================QUESTION #5================================###

def findTheDistanceValue(arr1, arr2, d):
    distance = 0

    for num1 in arr1:
        found = False

        for num2 in arr2:
            if abs(num1 - num2) <= d:
                found = True
                break

        if not found:
            distance += 1

    return distance

arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
result = findTheDistanceValue(arr1, arr2, d)
print(result)


###=================QUESTION #6================================###

def findDuplicates(nums):
    result = []

    for num in nums:
        index = abs(num) - 1

        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] *= -1

    return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
result = findDuplicates(nums)
print(result)


###=================QUESTION #7================================###

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


nums = [3, 4, 5, 1, 2]
result = findMin(nums)
print(result)


###=================QUESTION #8================================###

from collections import Counter

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []

    counter = Counter(changed)
    original = []

    for num in sorted(changed):
        if counter[num] == 0:
            continue
        if counter[num * 2] == 0:
            return []
        
        original.append(num)
        counter[num] -= 1
        counter[num * 2] -= 1

    return original


changed = [1, 3, 4, 2, 6, 8]
result = findOriginalArray(changed)
print(result)
