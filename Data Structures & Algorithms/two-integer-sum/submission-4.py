class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i in range (len(nums)):
            second = target - nums[i]
            if second in seen:
                return [seen[second],i]
            seen[nums[i]]=i
        # time complexity is O(n) and space O(n)
        '''for i in range (len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    sum = nums[i]+nums[j]
                    if sum == target:
                        return [i,j]
            takes O(n^2)
            O(1)
        '''
        '''
        for i in range (len(nums)):
            second = target - nums[i]
            if second in nums:
                return [i,nums.index(second)]
        takes O(n^2)
        '''
