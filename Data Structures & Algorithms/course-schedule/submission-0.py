class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        path = {i:[] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            path[prereq].append(course)
        
        visited = {}

        def dfs(course):
            visited[course] = "visiting"
            
            for neighbour in path[course]:
                if neighbour not in visited:
                    if not dfs(neighbour):
                        return False
                elif visited[neighbour] == "visiting":
                        return False
                elif visited[neighbour] == "visited":
                    continue
            visited[course] = "visited"
            return True
        
        for course in range(0,numCourses-1):
            if course not in visited:
               if not dfs(course):
                return False

        return True

                
            

