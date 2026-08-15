class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # checking for duplicates 
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


