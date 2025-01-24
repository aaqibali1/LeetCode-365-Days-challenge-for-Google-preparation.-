from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        rGraph = [[] for _ in range(n)]
        degree_in = [0] * n
        safe_nodes = []

        for u, neighbors in enumerate(graph):
            for v in neighbors:
                rGraph[v].append(u)
                degree_in[u] += 1

        queue = deque([i for i in range(n) if degree_in[i] == 0])

        while queue:
            u = queue.popleft()
            safe_nodes.append(u)
            for v in rGraph[u]:
                degree_in[v] -= 1
                if degree_in[v] == 0:
                    queue.append(v)

        return sorted(safe_nodes)
