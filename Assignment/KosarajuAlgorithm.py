from collections import defaultdict

class Kosaraju :
    def __init__ (self , vertices) :
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge (self , u , v) :
        self.graph[u].append(v)
    

    # Step 1: DFS to fill stack by finishing times
    def _dfs_fill_order (self , v , visited  , stack) :
        visited[v] = True
        for nbr in self.graph[v] :
            if not visited[nbr] :
                self._dfs_fill_order(nbr , visited , stack)

        stack.append(v)
    
    # Step 2: Create a reversed graph
    def _get_transpose(self) :
        g_t = Kosaraju(self.V)
        for u in self.graph :
            for v in self.graph[u] :
                g_t.add_edge(v , u)
        return g_t
    
    # Step 3: DFS on transposed graph
    def _dfs_util (self , v , visited , component ) :
        visited[v] = True
        component.append(v)
        for nbr in self.graph[v] :
            if not visited[nbr] :
                self._dfs_util(nbr , visited , component)

    # Main function to find and print SCCs
    def find_SCCs (self) :
        stack = []
        visited = [False] * self.V

        # Step 1: Fill vertices in stack according to their finish time
        for i in range(self.V) :
            if not visited[i] :
                self._dfs_fill_order(i , visited , stack)

        # Step 2: Get the transposed graph
        gr = self._get_transpose()

        # Step 3: Process all vertices in order defined by Stack
        visited = [False] * self.V
        sccs = []
        while stack :
            v = stack.pop()
            if not visited[v] :
                component = []
                gr._dfs_util(v , visited , component)
                sccs.append(component)
        
        return sccs
    

if __name__ == "__main__":
    g = Kosaraju(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print("Strongly Connected Components:")
    for comp in g.find_SCCs():
        print(comp)
