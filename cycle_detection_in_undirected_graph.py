from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True
        return False

    def has_cycle(self):
        visited = [False] * len(self.graph)
        for vertex in self.graph:
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, -1):
                    return True
        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

has_cycle = g.has_cycle()
print(has_cycle)  # Output: True
