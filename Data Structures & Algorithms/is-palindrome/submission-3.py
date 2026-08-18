class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_arr = []
        for i in range(len(s)):
            if s[i].isalnum():
                string_arr.append(s[i].lower()) # Remember to take care of cases as well
        start = 0
        end = len(string_arr) - 1
        # for i in range(len(string_arr)):
        while start < end:
            if string_arr[start] != string_arr[end]:
                return False
            start += 1
            end -= 1
        return True