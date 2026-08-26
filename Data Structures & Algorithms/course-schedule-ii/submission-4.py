class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        visit_set = set()
        in_path = set()
        result = []

        def dfs(course):
            if course in visit_set:
                return False
            if course in in_path:
                return True
            # if prereq_map[course] == []:
            #     result.append(course)

            visit_set.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            visit_set.remove(course)
            in_path.add(course)
            result.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return result