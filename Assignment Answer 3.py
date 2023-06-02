
##----------------------------------------ASSIGNMENT #3-----------------------------------------##

###=================QUESTION #1================================###

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closestSum = float('inf')
    
    for i in range(n - 2):
        currentNum = nums[i]
        left = i + 1
        right = n - 1
        
        while left < right:
            currentSum = currentNum + nums[left] + nums[right]
            
            if currentSum == target:
                return currentSum
            
            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum
            
            if currentSum > target:
                right -= 1
            else:
                left += 1
    
    return closestSum


threeSumClosest([-1,2,1,-4],1)
    
    
    
    
###=================QUESTION #2================================###

def fourSum(nums, target):
    n = len(nums)
    result = []
    nums.sort()

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result

fourSum([1,0,-1,0,-2,2],0)



###=================QUESTION #3================================###

def nextPermutation(nums):
    n = len(nums)
    i = n - 1

    # Find the first pair of adjacent elements where nums[i] > nums[i-1]
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1

    if i == 0:
        
        nums.reverse()
    else:
        j = n - 1
        
        while nums[j] <= nums[i - 1]:
            j -= 1

        
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        
        left = i
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums
        

print(nextPermutation([1,2,3]))


###=================QUESTION #4================================###

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

searchInsert([1,3,5,6],5)

###=================QUESTION #5================================###

def plusOne(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

    if carry:
        digits.insert(0, carry)

    return digits


plusOne([1,2,3])


###=================QUESTION #6================================###

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

singleNumber([2,2,1])


###=================QUESTION #7================================###

def findMissingRanges(nums, lower, upper):
    missing_ranges = []
    prev = lower - 1
    for num in nums + [upper + 1]:
        if num - prev > 1:
            lst=[]
            lst.append(prev+1)
            lst.append(num-1)
            missing_ranges.append(lst)
        prev = num
    return missing_ranges
    
findMissingRanges([0,1,3,50,75],0,99)    


###=================QUESTION #8================================###

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True


intervals = [[0,30],[5,10],[15,20]]
canAttendMeetings(intervals)
    