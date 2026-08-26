class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        visit_set = set()

        def dfs(course):
            if course in visit_set:
                return False
            if prereq_map[course] == []:
                return True
            
            visit_set.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            visit_set.remove(course)
            prereq_map[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True