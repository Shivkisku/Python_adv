def transitive_closure(graph):
    n = len(graph)
    closure = [[0] * n for _ in range(n)]

    def dfs(u, v):
        closure[u][v] = 1
        for neighbor in graph[v]:
            if closure[u][neighbor] == 0:
                dfs(u, neighbor)

    for i in range(n):
        dfs(i, i)

    return closure

# Example usage:
graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]

closure = transitive_closure(graph)
for row in closure:
    print(row)
