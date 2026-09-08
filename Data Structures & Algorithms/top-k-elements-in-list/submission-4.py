class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        for n, c in count.items():
            freq[c].append(n)
        for j in range(len(freq) - 1, -1, -1):
            if len(res) < k:
                for f in freq[j]:
                    res.append(f)
        return res

