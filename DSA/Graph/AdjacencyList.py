class Graph:
    def __init__(self):
        self.adjList = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []

    def add_edge(self, src, dest):
        if src not in self.adjList:
            self.add_vertex(src)
        if dest not in self.adjList:
            self.add_vertex(dest)
        self.adjList[src].append(dest)  # For directed graph
        self.adjList[dest].append(src)  # For undirected graph

    def printGraph(self):
        for vertex in self.adjList:
            print(vertex, "->", self.adjList[vertex])

G = Graph()
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,4)
G.add_edge(4,3)
G.add_edge(2,4)
G.add_edge(3,5)
G.add_edge(4,5)
G.printGraph()