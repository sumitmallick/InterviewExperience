# Problem Statement: Minimum Cost to Connect All Points
# Description: You are given a set of points on a 2D plane. Each point is represented as a pair of integers (x, y). The cost of connecting two points (x1, y1) and (x2, y2) is defined as the Manhattan distance between them: |x1 - x2| + |y1 - y2|.
# Your task is to find the minimum cost to connect all points with each other, such that every point is connected to at least one other point. You can assume that there are no duplicate points.
# Input: A list of points represented as pairs of integers [(x1, y1), (x2, y2), ..., (xn, yn)].
# Output: Return the minimum cost to connect all the points.
# Constraints:
# 1 <= points.length <= 1000
# 10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.
# Example: 
# Input:
# = [(0,0), (2,2), (3,10), (5,2), (7,0)]

# Output: 20
# Explanation:

# Here's one possible way to connect the points with the minimum cost:

# 1. Connect (0,0) and (2,2) with a cost of 4 (|0-2| + |0-2|).
# 2. Connect (2,2) and (5,2) with a cost of 3 (|2-5| + |2-2|).
# 3. Connect (5,2) and (7,0) with a cost of 4 (|5-7| + |2-0|).
# 4. Connect (2,2) and (3,10) with a cost of 9 (|2-3| + |2-10|).

# The total cost is 4 + 3 + 4 + 9 = 20.

# Note that there may be other ways to connect the points with the same minimum cost.
import heapq

def min_cost_to_connect_all_points(points):
    n = len(points)
    graph = {m: [] for m in range(n)}

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            cost = abs(x1-x2) + abs(y1- y2)
            graph[i].append((cost, j))
            graph[j].append((cost, i))
    
    visited = set()
    start = 0

    visited.add(start)
    min_val = graph[start]
    heapq.heapify(min_val)
    all_cost = 0

    while min_val:
        cost, node = heapq.heappop(min_val)
        if node not in visited:
            visited.add(node)
            all_cost += cost
            for nearby_cost, near_val in graph[node]:
                if near_val not in visited:
                    heapq.heappush(min_val, (nearby_cost, near_val))
    
    return all_cost


print(min_cost_to_connect_all_points([(0,0), (2,2), (3,10), (5,2), (7,0)]))
# Output: 20

# Time Complexity: O(n+m) -> n is the number of points and m is the number of edges
# Space Complexity: O(n^2)
