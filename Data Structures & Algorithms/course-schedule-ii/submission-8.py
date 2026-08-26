class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        in_path = set()
        visited = set()
        result = []

        def dfs(course):
            if course in in_path:
                return []
            if course in visited:
                return result

            in_path.add(course)
            for prereq in prereq_map[course]:
                if dfs(prereq) == []:
                    return []
            
            in_path.remove(course)
            visited.add(course)
            result.append(course)

            return True
        
        for course in range(numCourses):
            if dfs(course) == []:
                return []
            
        return result