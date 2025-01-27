class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Initialize the reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Mark direct prerequisites
        for a, b in prerequisites:
            reachable[a][b] = True
        
        # Step 2: Apply Floyd-Warshall algorithm to find all-pairs reachability
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        
        # Step 3: Answer each query
        return [reachable[u][v] for u, v in queries]