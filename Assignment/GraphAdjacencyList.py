class Graph :
    def __init__(self , vno):
        self.vertex_count = vno
        self.adjacencyList = {v : [] for v in range(vno)}
    
    def add_edge (self , u , v , weight=1) :
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count :
            self.adjacencyList[u].append((v , weight))
            self.adjacencyList[v].append((u , weight))
        else :
            raise IndexError("Index Error : Cannont Find Index")

    def remove_edge (self , u , v) :
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count :
            self.adjacencyList[u] = [(vertex , weight) for vertex , weight in self.adjacencyList[u] if vertex != v]
            self.adjacencyList[v] = [(vertex , weight) for vertex , weight in self.adjacencyList[v] if vertex !=u]
            
        else :
            raise IndexError("Index Error : Cannont Find Index")
        
    def has_edge (self , u , v) :
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count : 
            # return any(vertex == v for vertex , x in self.adjacencyList[u])
            for vertex, x in self.adjacencyList[u] :
                if vertex == v :
                    return True
                else :
                    return False
        else :
            raise IndexError("Index Error : Cannont Find Index")
    
    def print_adj_list (self) :
        for vertex , n in self.adjacencyList.items() :
            print("V : ",vertex,":",n )


if __name__ == "__main__" :
    graph = Graph(5)
    graph.add_edge(1,3)
    graph.remove_edge(1,3)
    print(graph.adjacencyList)
    print(graph.has_edge(1,3))
    graph.print_adj_list()