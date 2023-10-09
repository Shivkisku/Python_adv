class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def reverse(self):
        reversed_graph = Graph()

        for u in self.graph:
            for v in self.graph[u]:
                reversed_graph.add_edge(v, u)

        return reversed_graph

    def __str__(self):
        return str(self.graph)


# Example usage:
if __name__ == "__main__":
    original_graph = Graph()
    original_graph.add_edge("A", "B")
    original_graph.add_edge("B", "C")

    print("Original Graph:")
    print(original_graph)

    reversed_graph = original_graph.reverse()

    print("\nReversed Graph:")
    print(reversed_graph)
