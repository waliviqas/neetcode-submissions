class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # res array 
        # sort nums

        # for loop going through all of nums 
        #     check for duplicate 
        #         continue 
        #     empty set 
        #     for loop starting at i + 1 through nums
        #         c = -nums[i] - nums[j]
        #         if c in seen:
        #             store in var called trip 
        #             if not res or res[-1] != trip 
        #                 append to res
        #         add nums[j] to res
        # return res

        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            seen = set()
            for j in range(i + 1, len(nums)):
                c = -nums[i] - nums[j]
                if c in seen:
                    trip = [nums[i], c, nums[j]]
                    if not res or res[-1] != trip:
                        res.append(trip)
                seen.add(nums[j])
        return res