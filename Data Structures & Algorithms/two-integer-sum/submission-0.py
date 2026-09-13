class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n= target-nums[i]
            if n in nums[i+1:]:
                j= nums[i+1:].index(n)+i+1
                return [i,j]