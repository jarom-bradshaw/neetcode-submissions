class Solution:
    def hammingWeight(self, n: int) -> int:
        input_num = bin(n)
        print(input_num)
        print(n)
        bit_count = 0
        for bit in str(input_num):
            print(bit)
            if bit == "1":
                bit_count += 1
        return bit_count