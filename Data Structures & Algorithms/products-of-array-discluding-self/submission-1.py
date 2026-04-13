class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solved =[]
        output = []
        multiple =1
        for i,x in enumerate(nums):
            output.append(multiple)
            multiple*=x

        right =[]
        right = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            right[i] = multiple
            multiple *= nums[i]
        
        result=[]
        for i in range(len(nums)):
            result.append(output[i]*right[i])
        
        return result
        
        

       
        
            
            