def subset(l,n,i,nums):
    if i==n:
        print(l)
        return
    l.append(nums[i])
    subset(l,n,i+1,nums)
    l.pop()
    subset(l,n,i+1,nums)
nums=[1,2,3,4,5]
subset([],len(nums),0,nums)
