class Solution:

    def encode(self, strs: List[str]) -> str:
        # Takes a list of strs and joins them. We can join with some non ascii char
        # print(strs)
        result = []
        for string in strs:
            result.append(str(len(string)))
            result.append("#")
            result.append(string)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        # Split, based on that same non ascii char.
        print(s)
        # if not s:
        #     return []
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length

            res.append(s[start:end])
            i = end
        return res