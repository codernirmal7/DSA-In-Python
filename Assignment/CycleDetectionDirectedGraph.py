class Graph:
    def __init__ (self , vno) :
        self.vertex_count = vno
        self.adj_list = {i : [] for i in range(vno)}
    
    def add_edge (self , u , v , weight=1) :
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count :
            self.adj_list[u].append((v , weight))
        else :
            raise IndexError("Invalid Index : Cannot Find Index")
        
    def remove_edge (self , u , v) :
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count :
            self.adj_list[u] = [(vertex , weight) for vertex , weight in self.adj_list[u] if vertex != v]
        else :
            raise IndexError("Invalid Index : Cannot Find Index")
        
    def has_edge (self , u , v) :
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count :
            for vertex , weight in self.adj_list[u] :
                if vertex == v :
                    return True
        else :
            raise IndexError("Invalid Index : Cannot Find Index ")
        
    def print_edges (self) :
        for i in self.adj_list.items() :
            print(f"{i}")

    def isCycleDirected(self, visited, current , rec):
        visited[current] = True
        rec[current] = True
        for vertex , weight in self.adj_list[current] :
            if rec[vertex] == True :
                print(True)
            elif not visited[vertex] :
                self.isCycleDirected(visited , vertex , rec)
                

if __name__ == "__main__" :
    g = Graph(4)
    g.add_edge(1,0)
    g.add_edge(0,2)
    g.add_edge(2 , 3)
    g.add_edge(3,0)
    
    
    # print(g.has_edge(1,4))
    # print(g.has_edge(1,5))

    visited = [False for _ in range(g.vertex_count)]
    rec = [False for _ in range(g.vertex_count)]
    g.isCycleDirected(visited, 0 , rec)

    g.print_edges()