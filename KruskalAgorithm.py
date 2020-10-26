# definition of the "graph" class
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # definition of function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # the function to search an element in the graph
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # the function to search an element in the graph
    def apply_union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    #  definition of the Kruskal algorithm
    def kruskal_algorithm(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d -> %d" % (u, v, weight))


# creation of the graph object
# initializing te size of the graph
graph = Graph(8)
# adding the edges to the created graph
graph.add_edge(0, 2, 4)
graph.add_edge(0, 2, 2)
graph.add_edge(0, 1, 8)
graph.add_edge(0, 4, 3)
graph.add_edge(1, 5, 3)
graph.add_edge(1, 4, 6)
graph.add_edge(2, 3, 6)
graph.add_edge(2, 7, 4)
graph.add_edge(2, 5, 7)
graph.add_edge(2, 4, 1)
graph.add_edge(4, 6, 4)
graph.add_edge(5, 7, 1)
graph.add_edge(5, 6, 3)
graph.add_edge(6, 7, 5)

# creation the minimal tree with the previously defined function
graph.kruskal_algorithm()
