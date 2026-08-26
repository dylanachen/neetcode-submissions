class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # recursive DFS
        # use a map of a course (0-numCourses) to its list of prerequisites
        # we will also use a set to track the courses currently visiting in this branch of DFS (in order to detect cycles)
        # if the prerequisite list for a course is empty, the course can be taken and we return True out of the DFS
        # otherwise, we add the course to our visit set and iterate through its prerequisite list, calling DFS recursively
        # after visiting all of its prerequisites successfully, we can remove the course from the visit set and turn its prereq list to empty
        # perform DFS over all courses in the possible range
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