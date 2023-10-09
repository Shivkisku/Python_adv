class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1

def maximum_spanning_tree(graph):
    edges = [(weight, u, v) for u, neighbors in enumerate(graph) for v, weight in neighbors if u < v]
    edges.sort(reverse=True)  # Sort edges in descending order of weight
    n = len(graph)
    mst = []

    uf = UnionFind(n)

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))

    return mst

# Example usage:
graph = [
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (1, 2), (1, 4)],
    [(2, 0), (2, 1), (2, 4)],
    [(3, 0)],
    [(4, 1), (4, 2)],
]

mst = maximum_spanning_tree(graph)
print(mst)
