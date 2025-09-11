import heapq

class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adjacencyList = {v: [] for v in range(vno)}

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adjacencyList[u].append((v, weight))
            self.adjacencyList[v].append((u, weight))
        else:
            raise IndexError("Index Error : Cannot Find Index")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adjacencyList[u] = [
                (vertex, weight) for vertex, weight in self.adjacencyList[u] if vertex != v
            ]
            self.adjacencyList[v] = [
                (vertex, weight) for vertex, weight in self.adjacencyList[v] if vertex != u
            ]
        else:
            raise IndexError("Index Error : Cannot Find Index")

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            for vertex, _ in self.adjacencyList[u]:
                if vertex == v:
                    return True
            return False
        else:
            raise IndexError("Index Error : Cannot Find Index")

    def print_adj_list(self):
        for vertex, n in self.adjacencyList.items():
            print("V : ", vertex, ":", n)

    def prim_mst(self, start=0):
        """
        Prim's algorithm using a min-heap (priority queue).
        Returns list of edges in MST and total weight.
        """
        visited = [False] * self.vertex_count
        mst_edges = []
        total_weight = 0

        visited[start] = True
        pq = []
        for v, w in self.adjacencyList[start]:
            heapq.heappush(pq, (w, start, v))  # (weight, from, to)

        while pq and len(mst_edges) < self.vertex_count - 1:
            w, u, v = heapq.heappop(pq)
            if visited[v]:
                continue
            visited[v] = True
            mst_edges.append((u, v, w))
            total_weight += w
            for to, wt in self.adjacencyList[v]:
                if not visited[to]:
                    heapq.heappush(pq, (wt, v, to))

        if len(mst_edges) != self.vertex_count - 1:
            print("Warning: Graph is not connected. MST incomplete.")

        return mst_edges, total_weight


if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)

    graph.print_adj_list()
    mst, total = graph.prim_mst(start=0)
    print("\nMST edges:", mst)
    print("Total weight:", total)
