class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # empty hash set 

        # for i in range len(nums):
        #     if nums[i] is in hash set:
        #         return true 
        #     add to hash set

        # return false 

        numSet = set()
        for i in range(len(nums)):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
        return False


        # [1, 2, 3, 3]. {1, 2, 3}

        # if 1 in set 
        # if 2 in set 
        # if 3 in set 
        # if 3 in set --> true 

        # [1, 2, 3, 4]. {1, 2, 3, 4}
        # if 1 in set 
        # if 2 in set 
        # if 3 in set 
        # if 4 in set

