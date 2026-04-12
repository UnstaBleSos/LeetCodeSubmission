class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return False
        stack = []
        width = 1
        maxArea = 0
        for x in range(len(heights)):
            while stack and heights[stack[-1]]>heights[x]:
                index = stack[-1]
                stack.pop()
                if stack:
                    width = x- stack[-1] -1
                else:
                    width = x
                maxArea = max(maxArea,heights[index]*width)
            stack.append(x)

        n= len(heights)
        while stack:
                index = stack[-1]
                stack.pop()
                if stack:
                    width = n - stack[-1] -1
                else:
                    width = n
                maxArea = max(maxArea,heights[index]*width)
    
        return maxArea 