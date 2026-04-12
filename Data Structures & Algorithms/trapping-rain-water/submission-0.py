class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        total = 0 
        maxleft= 0
        maxright =0
        while left < right:
            current = 0 
            minimum = min(height[left], height[right])
            if height[left]< height[right]:
                if maxleft<height[left]:
                    maxleft = height[left]
                leftin = maxleft - height[left]
                if leftin>0:
                    total = total + leftin
                left +=1
            else:
                if maxright < height[right]:
                    maxright = height[right]
                rightin = maxright - height[right]
                if rightin > 0:
                    total = total +rightin
                right -=1
        return total

            

