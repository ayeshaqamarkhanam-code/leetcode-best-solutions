class Solution(object):
    def twoSum(self, nums, target):
        hash_table={}
        for i in range(len(nums)):
            if (target-nums[i]) in hash_table:
                j=hash_table[target-nums[i]]
                return i,j
            else:
                hash_table[nums[i]]=i