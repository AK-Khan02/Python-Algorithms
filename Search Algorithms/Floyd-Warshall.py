def floyd_warshall(weights, num_vertices):
    dist = [[float('infinity') for _ in range(num_vertices)] for _ in range(num_vertices)]
    for i in range(num_vertices):
        dist[i][i] = 0

    for start, end, weight in weights:
        dist[start][end] = weight

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Graph representation
weights = [
    (0, 1, 3),
    (1, 2, -2),
    (2, 3, 5),
    (3, 1, 1),
    (1, 3, 4)
]
num_vertices = 4

# Examples
shortest_paths = floyd_warshall(weights, num_vertices)
print("Shortest paths matrix:")
for row in shortest_paths:
    print(row)
