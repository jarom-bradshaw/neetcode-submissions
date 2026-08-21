class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        for string in strs:
            key = "".join(sorted(string))
            hashmap.setdefault(key,[])
            hashmap[key].append(string)
        return list(hashmap.values())