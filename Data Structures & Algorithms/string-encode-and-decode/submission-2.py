class Solution:

    def encode(self, strs: List[str]) -> str:
        # res = str(str length + pound + sring itself)
        # return string

        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i])) + "#" + strs[i]
        return res 

    def decode(self, s: str) -> List[str]:
        # for loop starting at i = 0
        #     j = i + 1
        #     while j != #
        #         j += 1
        #     len = int(str(string[i:j]))
        #     list.append(j+1:j+1+length)
        # return full list

        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length
        return res
