from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list
        adjList = [[] for _ in range(n + 1)]
        
        # Populate the adjacency list with edges and their weights
        for time in times:
            source, dest, cost = time
            adjList[source].append((dest, cost))
        
        # Priority queue to manage the nodes (node, current_cost)
        pq = [(0, k)]  # (cost, node)
        
        # Initialize costs to infinity
        costs = [float("inf")] * (n + 1)
        costs[k] = 0
        
        # Process the priority queue
        while pq:
            current_cost, current_node = heapq.heappop(pq)
            
            # Skip if the cost is not optimal
            if current_cost > costs[current_node]:
                continue
            
            # Update neighbors
            for neighbor, neighbor_cost in adjList[current_node]:
                new_cost = current_cost + neighbor_cost
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
        
        # Find the maximum time among all reachable nodes
        max_cost = max(costs[1:])  # Exclude costs[0] as it's not used (1-indexed)
        
        # If there's a node that is not reachable, return -1
        return max_cost if max_cost != float("inf") else -1
