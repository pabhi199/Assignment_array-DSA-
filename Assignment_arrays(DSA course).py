

								#ASSIGNMENT-01#
###--------------------------------------------------------------------------------------##
#QUESTION-01

def find_index(nums,target):
    result=[]
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]==target:
                result.append(i)
                result.append(j)
                
                break
    print(result)
                
            
if __name__=="__main__":
    
    nums =  [2,7,11,15]
    target = 9
    find_index(nums,target)

###########################################################################################################
#QUESTION-02

def remove_val(arr,val):
    for i in arr:
        if i==val:
            arr.remove(i)
    return len(arr)

if __name__=="__main__":
    
    nums = [3,2,2,3]
    val = 3
    print(remove_val(nums,val))
    
############################################################################################################
#QUESTION-03

def find_index(arr,tgt):
    for i in range(len (arr)):
        if arr[len(arr)-1] <tgt:
            return f"To be inserted at index: {len(arr)} "
        elif arr[0]>tgt:
            return f"To be inserted at index: 0 "
            
        else:
            if  arr[i] > tgt and arr[i-1]<tgt:
                return f" to be inserted at index: {i} "
            elif arr[i] == tgt:
                return f" is inserted at index: {i}"
if __name__=="__main__":
    
    nums = [1,3,5,6]
    tgt = 5
    print(find_index(nums,tgt))


############################################################################################################
#QUESTION-04

def out_num(arr):
    string=''
    for i in arr:
        string+=str(i)
    dizit=int(string)+1
    lst=[int(x) for x in str(dizit)]
    return lst

if __name__=="__main__":
    arr=[1,2,3]
    print(out_num(arr))    


############################################################################################################
#QUESTION-05


def merge_array(num1,num2):
    num1=num1+num2
    num1.sort()
    return num1


if __name__=="__main__":
    print(merge_array([1,2,3],[2,5,6]))
    

############################################################################################################
#QUESTION-06

def num_dup(arr):
    lst=[]
    for i in arr:
        if i not in lst:
            lst.append(i)
            
    if len(arr)==len(lst):
        return False
    else:
         return True
        
if __name__=="__main__":
    print(num_dup([1,2,3,1]))
    
############################################################################################################
#QUESTION-07


def arrange(arr):
    arr.sort()
    for i in arr:
        if i==0 :
            arr.remove(i)
            arr.append(0)
    return arr

if __name__=="__main__":
    arr=[0,1,0,3,12]
    print(arrange(arr))    
    
############################################################################################################
#QUESTION-08    

def miss_dup(arr):
    lst=[]
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            lst.append(arr[i])
    for i in range(1,len(arr)+1):
        if i not in arr:
            lst.append(i)
    
    return lst
            
if __name__=="__main__":
    print(miss_dup([1,2,2,4]))               
