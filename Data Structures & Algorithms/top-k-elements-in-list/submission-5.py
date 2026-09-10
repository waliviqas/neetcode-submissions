class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq array 
        # count map 
        # res

        # for loop through nums 
        #     increment count for each val 
        # for both values in count.items()
        #     # index here is the frequency 
        #     append to the key (index) the value (element)
        # for loop starting from back of freq array 
        #     while length of res < k
        #         continue appending values to res
        #     if len of res == k 
        #         return res

        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        for n, c in count.items():
            freq[c].append(n)
        for i in range(len(freq) - 1, -1, -1):
            for f in freq[i]:
                res.append(f)
            if len(res) == k:
                return res


        