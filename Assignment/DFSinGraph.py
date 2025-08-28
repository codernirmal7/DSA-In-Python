class Graph : 
    def __init__ (self , vno) : 
        self.vertex_count = vno 
        self.adj_list = {i : [] for i in range(vno)} 
        
    def add_edge (self , u , v , weight=1) : 
            if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count : 
                self.adj_list[u].append((v , weight)) 
                self.adj_list[v].append((u , weight)) 
            else :
                raise IndexError("Invalid Index : Index not found") 
            
    def delete_edge (self , u , v) : 
            if 0 <=u < self.vertex_count and 0 <= v < self.vertex_count : 
                self.adj_list[u] = [(vertex , weight) for vertex , weight in self.adj_list[u] if vertex != v] 
                self.adj_list[v] = [(vertex , weight) for vertex , weight in self.adj_list[v] if vertex != u] 
            else : 
                raise IndexError("Invalid Index : Index not found") 
            
    def has_edge (self , u , v) : 
            if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count : 
                return any(vertex == v for vertex , x in self.adj_list[u]) 
            
    def print_all_vertex (self) : 
            for vertex , weight in self.adj_list.items() : 
                print(vertex , weight) 
                
    # def DFS (self , current , checked_vertices ) : 
    #         print(current) 
    #         checked_vertices[current] = True 
    #         for vertex , x in self.adj_list[current] : 
    #             if not checked_vertices[vertex] : 
    #                 self.DFS(vertex , checked_vertices)
    
    
    # For disjoint edges
    def DFS (self , current , checked_vertices ) : 
            print(current)
            checked_vertices[current] = True 
            for vertex , x in self.adj_list[current] : 
                if not checked_vertices[vertex] : 
                    self.DFS(vertex , checked_vertices)
                    
                    
if __name__ == "__main__" : 
    g = Graph(7) 
    checked_vertices = []
    for _ in range(g.vertex_count) : 
        checked_vertices.append(False) 
    
    # g.add_edge(0,1)
    # g.add_edge(1,2)
    # g.add_edge(2,3)
    # g.add_edge(4,5)
    # g.add_edge(5,6)
    
    g.add_edge(0,1) 
    g.add_edge(0,2) 
    g.add_edge(1,3) 
    g.add_edge(2,4) 
    g.add_edge(4,5) 
    g.add_edge(3,5) 
    g.add_edge(5,6)
    
    for i in range(g.vertex_count) :
        if not checked_vertices[i] :
            g.DFS(i , checked_vertices) 
        
    # g.print_all_vertex()
