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
                return False
            if course in visited:
                return True

            in_path.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            in_path.remove(course)
            visited.add(course)
            result.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return result