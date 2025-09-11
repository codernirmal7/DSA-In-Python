class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = {i: [] for i in range(vno)}

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
        else:
            raise IndexError("Invalid Index : Cannot Find Index")

    def bellman_ford(self, source):
        # Step 1: Initialize distances
        distance = [float("inf")] * self.vertex_count
        distance[source] = 0

        # Step 2: Relax edges (V - 1 times)
        for _ in range(self.vertex_count - 1):
            for u in self.adj_list:
                for v, w in self.adj_list[u]:
                    if distance[u] != float("inf") and distance[u] + w < distance[v]:
                        distance[v] = distance[u] + w

        # Step 3: Check for negative-weight cycles
        for u in self.adj_list:
            for v, w in self.adj_list[u]:
                if distance[u] != float("inf") and distance[u] + w < distance[v]:
                    print("Graph contains negative weight cycle")
                    return None

        return distance


if __name__ == "__main__":
    vertices = 5  
    g = Graph(vertices)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    source = 0
    distances = g.bellman_ford(source)

    if distances:
        print(f"Shortest distances from vertex {source}:")
        for i, d in enumerate(distances):
            print(f"  To {i} → {d}")
