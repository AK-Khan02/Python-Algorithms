def bellman_ford(graph, start):
    distance = {vertex: float('infinity') for vertex in graph}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight

    # Check for negative weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distance[vertex] + weight < distance[neighbor]:
                print("Graph contains a negative weight cycle")
                return None

    return distance

# Graph representation
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'D': 2, 'E': -3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {},
    'E': {'D': -1}
}

# Examples
start_node = 'A'
distances = bellman_ford(graph, start_node)
print(f"Shortest distances from {start_node}: {distances}")
