def lengthOfLIS(nums):
        n=len(nums)
        def recursive(prevIndex,currIndex):
            include=0
            if currIndex==n:
                return 0
            if prevIndex==-1 or nums[prevIndex]<nums[currIndex]:
                include=1+recursive(currIndex,currIndex+1)
            exclude=recursive(prevIndex,currIndex+1)
            return max(include,exclude)
        #return recursive(-1,0)
        
        #currindex--->0 to n-1
        #prevIndex--->-1 to n-1--->add 1--->1 to n
        cache=[[-1]*n for i in range(n+1)]
        def memoization(prevIndex,currIndex):
            if currIndex==n:
                return 0
            elif cache[prevIndex+1][currIndex]!=-1:
                return cache[prevIndex+1][currIndex]
            include=0
            if prevIndex==-1 or nums[prevIndex]<nums[currIndex]:
                include=1+memoization(currIndex,currIndex+1)
            exclude=memoization(prevIndex,currIndex+1)
            cache[prevIndex+1][currIndex]=max(include,exclude)
            return cache[prevIndex+1][currIndex]
        #return memoization(-1,0)
        
        def tabulation():
            res=[1]*n
            finalList=1
            for currIndex in range(1,n):
                for prevIndex in range(currIndex):
                    if nums[currIndex]>nums[prevIndex]:
                        res[currIndex]=max(res[currIndex],res[prevIndex]+1)
                finalList=max(finalList,res[currIndex])
            return finalList
        return tabulation()
nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
