class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # in this case we are essentially shifting it to the right and modding it by two, because each one to the left goes double, 1,2,4,8,16 etc. So this way, we go through all of those and it works. Because we know this is a 32 bit number, it becomes O(1) instead of O(n).
            res += n % 2
            n = n >> 1
        return res

        