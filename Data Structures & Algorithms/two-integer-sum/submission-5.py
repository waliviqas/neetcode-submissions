class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash map 

        # for i,n enumarate nums:
        #     diff = target - n
        #     if diff in map:
        #         return (seen[n], i)
        #     add to hash map 

        seen = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i