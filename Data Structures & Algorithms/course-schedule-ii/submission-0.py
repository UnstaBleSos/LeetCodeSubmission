class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        path = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            path[prereq].append(course)
        visited = {}

        def dfs(course):
            visited[course] = "visiting"

            for neighbor in path[course]:
                print(neighbor)
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False
                elif visited[neighbor] == "visiting":
                    return False
                elif visited[neighbor] == "visited":
                    continue
            
            visited[course] = "visited"
            output.append(course)
            return True

        for course in range(0,numCourses):
            if course not in visited:
                if not dfs(course):
                    return []
        
        return list(reversed(output))
            