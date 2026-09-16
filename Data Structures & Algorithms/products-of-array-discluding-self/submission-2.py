class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        
        # Pass 1: Calculate prefix products (left to right)
        # out[i] will store the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate suffix products (right to left)
        # Multiply the existing prefix product by the running suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]
            
        return out