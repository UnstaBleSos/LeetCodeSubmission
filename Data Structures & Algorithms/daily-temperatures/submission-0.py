class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output= [0]*len(temperatures)
        index = 0 
        for x in range(len(temperatures)):
           while stack and temperatures[x] > temperatures[stack[-1]]:
            output[stack[-1]]=(x-stack[-1])
            stack.pop()
           stack.append(x)
        
        return output
                

