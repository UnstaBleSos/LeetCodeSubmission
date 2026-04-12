class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])

        array = [element for row in matrix for element in row]
        n = 0
        m = row*col -1
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