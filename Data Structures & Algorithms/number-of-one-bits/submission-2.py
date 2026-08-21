class Solution:
    def hammingWeight(self, n: int) -> int:
        input_num = bin(n)
        bit_count = 0
        for bit in str(input_num):
            if bit == "1":
                bit_count += 1
        return bit_count

# we would need to take in a recursive thing that takes the number and just turns it into binary, then literally for loop for it.