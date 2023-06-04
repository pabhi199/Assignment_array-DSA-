


####-----------------------------------------------------ASSIGNMENT 06--------------------------------------------####

###=================QUESTION #1================================###

def findPermutation(s):
    perm = []
    low, high = 0, len(s) + 1

    for c in s:
        if c == 'I':
            perm.append(low)
            low += 1
        elif c == 'D':
            perm.append(high)
            high -= 1

    perm.append(low)
    return perm


s = "IDID"
result = findPermutation(s)
print(result)



###=================QUESTION #2================================###

def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = divmod(mid, n)
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
result = searchMatrix(matrix, target)
print(result)


###=================QUESTION #3================================###

def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 1
    while i < n and arr[i] > arr[i - 1]:
        i += 1

    if i == 1 or i == n:
        return False

    while i < n and arr[i] < arr[i - 1]:
        i += 1

    return i == n


arr = [2, 1]
result = validMountainArray(arr)
print(result)


###=================QUESTION #4================================###

def findMaxLength(nums):
    max_length = 0
    sum_map = {0: -1}
    running_sum = 0

    for i, num in enumerate(nums):
        if num == 1:
            running_sum += 1
        else:
            running_sum -= 1

        if running_sum in sum_map:
            max_length = max(max_length, i - sum_map[running_sum])
        else:
            sum_map[running_sum] = i

    return max_length


nums = [0, 1]
result = findMaxLength(nums)
print(result)


###=================QUESTION #5================================###

def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort()
    min_product_sum = 0

    for i in range(len(nums1)):
        min_product_sum += nums1[i] * nums2[-i - 1]

    return min_product_sum


nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
result = minProductSum(nums1, nums2)
print(result)


###=================QUESTION #6================================###

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

###=================QUESTION #7================================###

def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    while num <= n * n:
        # Traverse top row from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse right column from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse bottom row from right to left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Traverse left column from bottom to top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


n = 3
result = generateMatrix(n)
for row in result:
    print(row)


###=================QUESTION #8================================###

def multiply(mat1, mat2):
    m = len(mat1)  # Number of rows in mat1
    k = len(mat1[0])  # Number of columns in mat1 / Number of rows in mat2
    n = len(mat2[0])  # Number of columns in mat2
    
    # Initialize the result matrix with zeros
    result = [[0] * n for _ in range(m)]
    
    # Perform matrix multiplication
    for i in range(m):
        for j in range(n):
            for l in range(k):
                result[i][j] += mat1[i][l] * mat2[l][j]
    
    return result


mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]

result = multiply(mat1, mat2)
for row in result:
    print(row)
