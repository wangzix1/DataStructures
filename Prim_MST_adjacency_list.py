###Prim MST adjacency list O(ElogV)
###traverse all vertices using BFS and use a min heap to store the vertices not yet included in MST

from heapq import heappush, heappop
from itertools import count
###tie breaking

def minimum_spanning_tree_cost(graph):
    """
    return the sum of costs of the edges in the MST   
    """
    tiebreak = count().__next__
    total = 0
    explored = set()
    start = next(iter(graph))
    unexplored = [(0, tiebreak(), start)]
    while unexplored:
        cost,_, winner = heappop(unexplored)
        if winner not in explored:
            explored.add(winner)
            total += cost
            for neighbor, cost in graph[winner]:
                if neighbor not in explored:
                    heappush(unexplored, (cost, tiebreak(), neighbor))
    return total

