class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # empty hash set 
        
        # loop through nums in for loop 
        #     if nums[i] in hash set
        #         return True
        #     add to hash set 
        # return false

        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False