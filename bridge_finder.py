from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u, visited, parent, disc, low):
        children = 0
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        visited[u] = True

        for v in self.graph[u]:
            if not visited[v]:
                children += 1
                self.bridge_util(v, visited, u, disc, low)
                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    print(f"Bridge found: {u} - {v}")
            elif v != parent:
                low[u] = min(low[u], disc[v])

    def find_bridges(self):
        visited = [False] * self.V
        disc = [-1] * self.V
        low = [-1] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.bridge_util(i, visited, -1, disc, low)

# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.find_bridges()
