class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for course, pre in prerequisites:
            adjList[pre].append(course)      # pre unlocks course

        path = set()    # courses on the CURRENT dfs path
        safe = set()    # courses fully explored, proven cycle-free

        def dfs(course):
            if course in path:
                return False                 # looped back onto my own path: cycle
            if course in safe:
                return True                  # already proven fine, skip the work

            path.add(course)                 # step onto the path
            for nxt in adjList[course]:
                if not dfs(nxt):
                    return False             # a cycle below me = a cycle, stop now
            path.remove(course)              # step off the path (backtrack)
            safe.add(course)                 # everything below me is clean
            return True

        for c in range(numCourses):          # graph may be in separate pieces
            if not dfs(c):
                return False
        return True