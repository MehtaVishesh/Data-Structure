class Graph:
    def __init__ (self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, v1, v2):
        if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[v1].remove(v2)
                self.adjacency_list[v2].remove(v1)
                return True
            except ValueError:
                pass
        return False
        
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for otherVertex in self.adjacency_list[vertex]:
                self.adjacency_list[otherVertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")


graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

graph.remove_vertex("D")

graph.print_graph()
