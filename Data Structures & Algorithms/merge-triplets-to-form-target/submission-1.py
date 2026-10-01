class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        row = len(triplets)
        col = len(triplets[0])
        position = [False] * len(target)
        for i in range(row):
            count =0 
            for j in range(col):
                if triplets[i][j] <= target[j]:
                    count+= 1 
                
            if count == len(target):
                for j in range(col):
                    if triplets[i][j] == target[j]:
                        position[j] = True
        
        if all(position):
            return True
        else:
            return False
       