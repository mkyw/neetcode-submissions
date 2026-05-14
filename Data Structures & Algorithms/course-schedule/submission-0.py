class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            m[course].append(prereq)
        
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if m[course] == []:
                return True
            
            visit.add(course)

            for prereq in m[course]:
                if not dfs(prereq):
                    return False
            
            visit.remove(course)
            m[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
