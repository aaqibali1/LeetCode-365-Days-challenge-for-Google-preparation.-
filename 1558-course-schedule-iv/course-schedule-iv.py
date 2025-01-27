class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for prereq in prerequisites:
            reachable[prereq[0]][prereq[1]] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        return [reachable[query[0]][query[1]] for query in queries]
