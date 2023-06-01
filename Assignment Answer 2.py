



##--------------------------------------------ASSIGNMENT-2--------------------------------------##

#QUESTION #1

def arrayPairSum(nums):
    nums.sort()
    sum = 0
    for i in range(0, len(nums), 2):
        sum += nums[i]
    return sum


nums = [1, 4, 3, 2]
print(arrayPairSum(nums))



#QUESTION #2

def maxCandies(candyType):
    uniqueCandies = set()
    for candy in candyType:
        uniqueCandies.add(candy)
    
    maxCandies = len(candyType) // 2
    uniqueCount = len(uniqueCandies)
    
    return min(maxCandies, uniqueCount)

candyType = [1, 1, 2, 2, 3, 3]
print(maxCandies(candyType))



#QUESTION #3

def findLHS(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    
    max_length = 0
    for num in nums:
        if num + 1 in num_counts:
            length = num_counts[num] + num_counts[num + 1]
            if length > max_length:
                max_length = length
    
    return max_length

nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums))



#QUESTION #4

def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
        if count == n:
            return True
    return count >= n

flowerbed = [1, 0, 0, 0, 1]
n = 1
print(canPlaceFlowers(flowerbed, n))


#QUESTION #5

def maximumProduct(nums):
    nums.sort()
    max_product1 = nums[-1] * nums[-2] * nums[-3]
    max_product2 = nums[0] * nums[1] * nums[-1]
    return max(max_product1, max_product2)

nums = [1, 2, 3]
print(maximumProduct(nums))



#QUESTION #6

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))



#QUESTION #7

def monotonic(num):
    inc=True
    dec=True
    for i in range(0,len(num)-1):
        if num[i]>num[i+1]:
            inc=False
    for i in range(0,len(num)-1):
        if num[i+1]>num[i]:
            dec=False
    return inc or dec

if __name__=="__main__":
    print(monotonic([1,2,2,3]))


#QUESTION #8

def minimumScore(nums, k):
    min_num = float('inf')
    max_num = float('-inf')

    for num in nums:
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    if max_num - min_num <= 2 * k:
        return max_num - min_num

    score1 = max_num - k - (min_num + k)
    score2 = max_num - (min_num + 2 * k)

    return min(score1, score2)

if __name__=="__main__":
    nums = [1]
    k = 0
    print(minimumScore(nums, k))




