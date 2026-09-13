class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        views ={}
        for i in range(len(nums)):
            n= target-nums[i]
            if n in views:
                return[views[n],i]
            views[nums[i]]=i
        