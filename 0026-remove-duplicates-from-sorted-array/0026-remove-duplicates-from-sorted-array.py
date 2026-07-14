class Solution(object):
    def removeDuplicates(self, nums):
        k,n=0,len(nums)
        if n==0:
            return 0
        for i in range(1,n):
            if nums[k]!=nums[i]:
                nums[k+1]=nums[i]
                k+=1
        return k+1