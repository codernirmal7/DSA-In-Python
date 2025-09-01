class Stack :
    def __init__(self):
        self.my_list = []

    def is_empty (self) :
        if len(self.my_list) == 0 :
            return True
        else :
            return False
        
    def push (self , data) :
        self.my_list.insert(0,data)

    def pop (self) :
        if not self.is_empty() :
            self.my_list.pop(0)

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

    def topo_logical_sorting(self, visited, current , stack):
        visited[current] = True
        for vertex , weight in self.adj_list[current] :
            if not visited[vertex] :
                self.topo_logical_sorting(visited  , vertex, stack)

        stack.push(current)
            

if __name__ == "__main__" :
    g = Graph(6)
    stack = Stack()
    g.add_edge(5,0)
    g.add_edge(4,0)
    g.add_edge(5,2)
    g.add_edge(4,1)
    g.add_edge(2,3)
    g.add_edge(3,1)
    
    
    # print(g.has_edge(1,4))
    # print(g.has_edge(1,5))

    visited = [False for _ in range(g.vertex_count)]
    for i in range(g.vertex_count) :
        if not visited[i] :
            g.topo_logical_sorting(visited , i , stack)
    print(stack.my_list)
    g.print_edges()