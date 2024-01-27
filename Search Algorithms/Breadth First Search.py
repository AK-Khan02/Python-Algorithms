from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node] - visited)

# Example 1: A simple graph
graph1 = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
print("BFS Example 1:")
bfs(graph1, 'A')

print("\n")

# Example 2: A more complex graph
graph2 = {
    '1': {'2', '3'},
    '2': {'1', '4', '5'},
    '3': {'1', '5'},
    '4': {'2', '6'},
    '5': {'2', '3', '6'},
    '6': {'4', '5', '7'},
    '7': {'6'}
}
print("BFS Example 2:")
bfs(graph2, '1')
