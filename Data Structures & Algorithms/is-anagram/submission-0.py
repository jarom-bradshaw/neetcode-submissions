class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_a = {}
        dict_b = {}
        if len(s) != len(t):
            return False 
        for i in range(len(s)):
            if s[i] in dict_a:
                dict_a[s[i]] += 1
            else:
                dict_a[s[i]] = 1
            if t[i] in dict_b:
                dict_b[t[i]] += 1
            else:
                dict_b[t[i]] = 1
        if dict_a != dict_b:
            return False
        return True

