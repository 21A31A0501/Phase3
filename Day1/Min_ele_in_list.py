def solveIt(index, nums, n):
    if index == n:
        return 1000000000
    minEleInRightPart = solveIt(index + 1, nums, n)
    if nums[index] < minEleInRightPart:
        return nums[index]
    return minEleInRightPart

nums = [1, 2, 3, 4, 11, 22]
result = solveIt(0, nums, len(nums))
print(result)



#parent to child
''''
def findMin(index,n,nums,res):
    if index==n:
        print("Min is:",res)
        return 
    if nums[index]<res:
        res=nums[index]
    findMin(index+1,n,nums,res)
nums=[1311,65,340,45,87,28]
n=len(nums)
findMin(0,n,nums,nums[n-1])
'''

#child to parent
def findMin(index,n,nums,res):
    if index==n-1:
        return res
    if nums[index]<res:
        res=nums[index]
    min=findMin(index+1,n,nums,res)
    return min
nums=[1311,65,340,45,87,12]
n=len(nums)
print(findMin(0,n,nums,nums[n-1]))

