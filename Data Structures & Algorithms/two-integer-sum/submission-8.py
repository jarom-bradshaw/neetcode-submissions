class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  test case: nums=[5,5] target=10
        for i in range(len(nums)):
            k = target - nums[i]
            for j in range(len(nums)):
                if k == nums[j] and j != i:
                    return [i,j]
        
# THE QUICK WAY TO DO THIS IS HASHMAP 
# PROBABLY RETURN 