class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        result = []
        for i in range(0, len(nums)-2):
            if i>0 and sortednums[i] == sortednums[i-1]:
               continue
            fixed = sortednums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                if fixed+sortednums[left]+sortednums[right] == 0:
                    triplets = [ fixed,sortednums[left], sortednums[right]]
                    result.append(triplets)
                    while left<right and  sortednums[left] == sortednums[left+1]:
                        left +=1
                    while left<right and  sortednums[right] == sortednums[right-1]: 
                        right -=1
                    left +=1
                    right -=1
                elif fixed+sortednums[left]+sortednums[right] < 0:
                    left +=1
                else:
                    right -=1
        return result   