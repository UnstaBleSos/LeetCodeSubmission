class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        amount = 0 
        while left<right:
            difference = right - left 
            minimum = min(heights[right],heights[left])
            area = minimum*difference
            amount = max(amount,area)
            if heights[left] < heights[right]:
                left+=1
            else:
                right -=1
        return amount
            