class Graph :
    def __init__ (self , vno) :
        self.vertex_count = vno
        self.adjacency_matrix = [[0] * vno for i in range(vno)]

    
    def add_edge (self , u , v , weight=1) :
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count :
            self.adjacency_matrix[u][v] = weight
            self.adjacency_matrix[v][u] = weight
        else :
            raise IndexError("Invalid Index : Cannot find the index")
        
    def remove_edge (self , u , v) :
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count :
            self.adjacency_matrix[u][v] = 0
            self.adjacency_matrix[v][u] = 0
        else :
            raise IndexError("Invalid Index : Cannot find the index")
        
    def has_edge (self , u , v) :
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count :
            # if (self.adjacency_matrix[u][v] !=0 and self.adjacency_matrix[v][u] != 0) :
            #     return True
            # else :
            #     return False
            return self.adj_matrix[u][v] !=0
        else :
            raise IndexError("Invalid Index : Cannot find the index")
        
    
    def print_adj_matrix (self) :
        for row_list in self.adjacency_matrix :
            print(" ".join(map(str,row_list)))


if __name__ == "__main__" :
    graph = Graph(3)
    graph.add_edge(1,1)
    # graph.remove_edge(1,2)
    print(graph.has_edge(1,2))
    graph.print_adj_matrix()