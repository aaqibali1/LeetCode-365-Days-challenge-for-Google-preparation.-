from collections import deque

class Solution:
    def isBipartite(self, node, color, adj, c, component):
        color[node] = c
        component.append(node)
        for nbr in adj[node]:
            if color[nbr] == c:
                return False
            if color[nbr] == -1 and not self.isBipartite(nbr, color, adj, 1 - c, component):
                return False
        return True

    def maxGroupsInComponent(self, component, adj, n):
        max_depth = 0
        for start in component:
            depth = [-1] * n
            q = deque([start])
            depth[start] = 0
            while q:
                node = q.popleft()
                for nbr in adj[node]:
                    if depth[nbr] == -1:
                        depth[nbr] = depth[node] + 1
                        max_depth = max(max_depth, depth[nbr])
                        q.append(nbr)
        return max_depth + 1

    def magnificentSets(self, n, edges):
        color = [-1] * n
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        components = []
        for i in range(n):
            if color[i] == -1:
                component = []
                if not self.isBipartite(i, color, adj, 0, component):
                    return -1
                components.append(component)

        return sum(self.maxGroupsInComponent(comp, adj, n) for comp in components)
