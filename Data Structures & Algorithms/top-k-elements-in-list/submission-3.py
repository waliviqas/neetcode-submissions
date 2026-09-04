class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = []
        
        # freq = [[] for i in range(len(nums))]

        # for each loop through nums:
        #     increment the key val by 1
        # for each pair get count.items()
        #     add through the value (index) to freq table 

        # for loop start from back of freq
        #     if the one that we are on is empty
        #         continue 
            
        #     while values exist in curr index
        #         append to res
        #     if res length = k
        #         return res

            res = []
            map = {}
            freq = [[] for i in range(len(nums) + 1)]

            for n in nums:
                map[n]  = map.get(n, 0) + 1
            for n, c in map.items():
                freq[c].append(n)
            for i in range(len(freq) - 1, 0, -1):
                if not freq[i]:
                    continue
                for f in freq[i]:
                    res.append(f)
                    if len(res) == k:
                        return res


