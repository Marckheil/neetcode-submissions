class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for course, pre in prerequisites:
            adjList[pre].append(course)      # pre unlocks course

        
        path = set()
        safe = set()

        def dfs(course):
            if course in path:
                return False
            if course in safe:
                return True
            
            path.add(course)
            for nxt in adjList[course]:
                if not dfs(nxt):
                    return False
                
            path.remove(course)
            safe.add(course)
            return True
        
                
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
