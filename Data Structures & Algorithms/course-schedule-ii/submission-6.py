class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        visit_set = set()
        in_path = set()
        result = []

        def dfs(course):
            if course in in_path:
                return result
            if course in visit_set:
                return []

            visit_set.add(course)
            for prereq in prereq_map[course]:
                if dfs(prereq) == []:
                    return []
            
            visit_set.remove(course)
            prereq_map[course] = []
            in_path.add(course)

            return result.append(course)
        
        for course in range(numCourses):
            if dfs(course) == []:
                return []
            
        return result