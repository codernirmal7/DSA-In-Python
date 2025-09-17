from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0  # global timer for discovery times

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_articulation_points(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        ap = [False] * self.V  # articulation point marker

        for i in range(self.V):
            if disc[i] == -1:  # not visited
                self._dfs(i, disc, low, parent, ap)

        # print results
        print("Articulation Points are:")
        for i in range(self.V):
            if ap[i]:
                print(i, end=" ")
        print()

    def _dfs(self, u, disc, low, parent, ap):
        children = 0
        disc[u] = low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if disc[v] == -1:  # if v not visited
                parent[v] = u
                children += 1
                self._dfs(v, disc, low, parent, ap)

                low[u] = min(low[u], low[v])

                # Case 1: u is root and has more than one child
                if parent[u] == -1 and children > 1:
                    ap[u] = True

                # Case 2: u is not root and no back edge from v or its subtree
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:  # back edge
                low[u] = min(low[u], disc[v])

# Example usage:
if __name__ == "__main__" :
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    g.find_articulation_points()
