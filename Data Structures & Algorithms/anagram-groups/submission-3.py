class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each word in strs
        #     for each letter in word 
        #         add that letter to array with corresponding index
        #     turn array into key 
        #     array key = append current word 
        # return list(map.values())

        groups = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            key = tuple(arr)
            groups[key].append(s)
        return list(groups.values())
