class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return False
        stack = []
        maxArea = 0

        for x in range(len(heights)):

            stack.append(heights[x])

            if stack[-1] >= heights[x]:
                stack.append(heights[x])
            else:
                maxArea = max(maxArea,heights[x]*len(stack))

            print(maxArea)    
            
        

