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
            return any(vertex == v for vertex , x in self.adjacencyList[u])
        else :
            raise IndexError("Index Error : Cannont Find Index")
    
    def print_adj_list (self) :
        for vertex , n in self.adjacencyList.items() :
            print("V : ",vertex,":",n )

    def dfs (self , curr , vis , dt , low , time , par) :
        vis[curr] = True
        time[0] += 1   
        dt[curr] = low[curr] = time[0]

        for vertex , weight in self.adjacencyList[curr] :
            if vertex == par :
                continue
            elif not vis[vertex] :
                self.dfs(vertex , vis , dt , low , time , curr)
                low[curr] = min(low[curr] , low[vertex])
                if dt[curr] < low[vertex] :
                    print(f"Bridge is : {curr} --- {vertex}")
            else:
                low[curr] = min(low[curr], dt[vertex])
    
    def get_bridge (self) :
        dt = [None] * self.vertex_count
        low = [None] * self.vertex_count
        time = [0]
        vis = []
        for _ in range(self.vertex_count) : 
            vis.append(False) 
        
        for i in range(self.vertex_count) :
            if not vis[i] :
                self.dfs(i , vis , dt , low , time , -1)
    

if __name__ == "__main__" :
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)

    graph.add_edge(1,2)

    graph.add_edge(3,4)

    graph.get_bridge()
    
