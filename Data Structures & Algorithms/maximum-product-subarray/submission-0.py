class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        n = len(nums)
        
        max_product = nums[0]
        min_product = nums[0]
        overall = nums[0]

        for i in range(1,n):
            prevmax = nums[i] * max_product
            prevmin = nums[i] * min_product
            new_arr = nums[i]

            max_product = max(prevmax, prevmin, new_arr)
            min_product = min(prevmax, prevmin, new_arr)
            overall = max(overall, max_product)
        
        return overall 