def solveIt(index, nums, n):
    if index == n:
        return 0
    maxEleInRightPart = solveIt(index + 1, nums, n)
    if nums[index] > maxEleInRightPart:
        return nums[index]
    return maxEleInRightPart

nums = [1, 2, 3, 4, 11, 22]
result = solveIt(0, nums, len(nums))
print(result)


#parent to child
''''
def findMax(index,n,nums,res):
    if index==n:
        print("Max is:",res)
        return 
    if nums[index]>res:
        res=nums[index]
    findMax(index+1,n,nums,res)
nums=[1311,65,340,45,87,28]
n=len(nums)
findMax(0,n,nums,nums[0])
'''

#child to parent
''''
def findMax(index,n,nums,res):
    if index==n:
        return res
    if nums[index]>res:
        res=nums[index]
    max=findMax(index+1,n,nums,res)
    return max
nums=[13,65,340,45,87,28]
n=len(nums)
result=findMax(0,n,nums,nums[0])
print("Max is:",result)
'''


''''
def findMaxInWay1(index, nums, n, result):
    if index == n:
        print("Max ele is:", result)
        return 
    if nums[index] > result:
        result = nums[index]
    findMaxInWay1(index + 1, nums, n, result)
 
nums = [12, 32, 11, 10]
result = findMaxInWay1(0, nums, len(nums), 0)
 
 
def findMaxInWay2(index, nums, n):
    if index == n - 1:
        return nums[index]
    nextGreater = findMaxInWay2(index + 1, nums, n)
    if nextGreater < nums[index]:
        return nums[index]
    return nextGreater 
 
nums = [12, 32, 11, 10]
result = findMaxInWay2(0, nums, len(nums))
print("Max ele:", result)
'''