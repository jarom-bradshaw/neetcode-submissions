class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The solution here is probably to use a hashmap. We can use 
        # a hashmap that will count the different anagrams. I should 
        # probably go back and look at how the single anagram was solve
        #  on the video first.
        # Let's brute force with sorted force with O(n^2)
        hashmap = {}
        for string in strs:
            hashmap.setdefault("".join(sorted(string)),[]) # Strings are iterable, but immutable. so we use sorted, instead of .sort(), which modifies a value, instead of returning a val unlike sorted.
            hashmap["".join(sorted(string))].append(string)
        # print(hashmap) # I don't think neetcode let's me do that. oh welp.
        # I am counting how many similar ones there are, which I don't need.
        answer_list = []
        for key_val_pair in hashmap:
            # print(key_val_pair)
            answer_list.append(hashmap[key_val_pair])

        return answer_list
