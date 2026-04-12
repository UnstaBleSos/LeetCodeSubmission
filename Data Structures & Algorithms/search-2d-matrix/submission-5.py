class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        array = [element for row in matrix for element in row]
        n = 0
        m = len(array)-1
        print(array)
        while n<=m:
            mid = (n+m) // 2 

            if array[mid] == target:
                return True
            elif array[mid] > target:
                m = mid -1
            else:
                n = mid+1
        
        return False