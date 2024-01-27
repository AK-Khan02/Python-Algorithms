def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

# Example 1: A simple graph
graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = set()
print("DFS Example 1:")
dfs(graph1, 'A', visited)

print("\n")

# Example 2: A more complex graph
graph2 = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['5'],
    '4': ['6'],
    '5': ['6'],
    '6': ['7'],
    '7': []
}
visited = set()
print("DFS Example 2:")
dfs(graph2, '1', visited)
