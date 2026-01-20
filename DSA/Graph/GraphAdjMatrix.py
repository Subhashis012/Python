class Graph:
    def __init__(self, vertex):
        self.mat = [[0] * vertex for _ in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest):
        if (0 <= src < self.size) and (0 <= dest < self.size):
            self.mat[src][dest] = 1 # For directed graph and For undirected graph
            self.mat[dest][src] = 1  # For undirected graph
        else:
            print("Invalid vertex")
    
    def display(self):
        for row in self.mat:
            print(" ".join(map(str, row)))
            # print(*row)


G = Graph(5)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.display()