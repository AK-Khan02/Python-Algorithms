import heapq

def a_star_search(graph, start, goal, h):
    open_set = []
    heapq.heappush(open_set, (0 + h[start], 0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in graph[current]:
            tentative_g_score = current_g + graph[current][neighbor]

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))

    return []

# Example: Graph with heuristic values for each node
graph = {
    'A': {'B': 1, 'C': 3, 'E': 6},
    'B': {'A': 1, 'D': 5},
    'C': {'A': 3, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 2},
    'E': {'A': 6, 'D': 2}
}
h = {
    'A': 10,
    'B': 6,
    'C': 5,
    'D': 2,
    'E': 0
}
start = 'A'
goal = 'E'
path = a_star_search(graph, start, goal, h)
print("A* Path from", start, "to", goal, ":", path)
