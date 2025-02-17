class Solution(object):
    def twoSum(self, nums, target):
        complement_store = {} 

        for i in range(0, len(nums)):

            complement = target - nums[i] 

            if complement in list(complement_store.keys()):
                return [complement_store[complement], i] 
            
            complement_store[nums[i]] = i

