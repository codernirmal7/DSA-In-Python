import heapq

class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = {i: [] for i in range(vno)}

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
        else:
            raise IndexError("Invalid Index : Cannot Find Index")

    def dijkstras(self, start):
        dist = [float("inf")] * self.vertex_count
        prev = [None] * self.vertex_count
        visited = [False] * self.vertex_count

        dist[start] = 0
        pq = [(0, start)]   # heap stores (distance, node)

        while pq:
            d, node = heapq.heappop(pq)

            if visited[node]:
                continue
            visited[node] = True

            for neighbor, weight in self.adj_list[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    prev[neighbor] = node
                    heapq.heappush(pq, (dist[neighbor], neighbor))

        # Print results
        for i in range(self.vertex_count):
            if dist[i] == float("inf"):
                print(f"No path from {start} to {i}")
            else:
                path = self.reconstruct_path(prev, start, i)
                print(f"Shortest path {start} → {i} = {path} with cost {dist[i]}")

    def reconstruct_path(self, prev, start, target):
        path = []
        at = target
        while at is not None:
            path.append(at)
            at = prev[at]
        path.reverse()
        if path[0] == start:
            return path
        return []


if __name__ == "__main__":
    g = Graph(6)

    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 3, 7)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 4, 3)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 3, 2)
    g.add_edge(4, 5, 5)

    g.dijkstras(0)
