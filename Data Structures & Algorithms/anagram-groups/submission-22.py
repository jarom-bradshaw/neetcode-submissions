class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        for string in strs:
            key = "".join(sorted(string))
            hashmap.setdefault(key,[])
            hashmap[key].append(string)
        # print(hashmap.values())
        # return hashmap.values()
        return list(hashmap.values())