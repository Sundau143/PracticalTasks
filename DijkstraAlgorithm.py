# this library contains INT_MAX definition
import sys


# definition of the "Graph" class
class Graph:
    # adding the vertices to the created graph
    def __init__(self, vertices_amount):
        self.V = vertices_amount
        self.graph = [[0 for column in range(vertices_amount)]
                      for row in range(vertices_amount)]

    # definition of the Dijkstra algorithm function
    def algorithm_solution(self, dist):
        print("Vertex Distance from Source")
        for node in range(self.V):
            # print the distance from source node to every other node
            print(node, "->", dist[node])

    # minimum distance value, from the set of vertices
    def find_minimal_distance(self, dist, sptSet):

        # initialization of minimum distance for next node and the original one
        minimal = sys.maxsize

        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V):
            if dist[v] < minimal and sptSet[v] is False:
                minimal = dist[v]
                min_index = v

        return min_index

    # the implementation of Dijkstra algorithm
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation 
    def dijkstra_algorithm(self, src):
        distance = [sys.maxsize] * self.V
        distance[src] = 0
        sptSet = [False] * self.V
        for i in range(self.V):

            # pick the minimum distance vertex from
            # the set of vertices which are not yet added
            # u variable is always equal to src in first iteration
            u = self.find_minimal_distance(distance, sptSet)

            # Put the minimum distance vertex in the  
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                        sptSet[v] is False and \
                        distance[v] > distance[u] + self.graph[u][v]:
                    distance[v] = distance[u] + self.graph[u][v]
        self.algorithm_solution(distance)


# setting a size of graph
new_graph = Graph(8)
# initialising graph with the adjacency matrix
new_graph.graph = [[0, 8, 2, 4, 3, 0, 0, 0],
                   [8, 0, 0, 0, 6, 3, 0, 0],
                   [2, 0, 0, 0, 0, 7, 0, 4],
                   [4, 0, 0, 0, 1, 0, 0, 0],
                   [3, 6, 0, 1, 0, 0, 4, 0],
                   [0, 3, 7, 0, 0, 0, 3, 1],
                   [0, 0, 0, 0, 4, 3, 0, 5],
                   [0, 0, 4, 0, 0, 1, 5, 0]]

# calling the function to find the minimal distances between source and all vertices
new_graph.dijkstra_algorithm(0)
