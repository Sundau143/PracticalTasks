
# definition very big constant to simulate the infinity
INFINITY = 9999999
# definition of matrix sizes
V = 8
# creation of matrix of size 8x8
graph = [[0, 2, 0, 4, 3, 0, 8, 0],
         [2, 0, 4, 6, 0, 0, 0, 7],
         [0, 4, 0, 0, 0, 5, 0, 1],
         [4, 6, 0, 0, 1, 0, 0, 0],
         [3, 0, 0, 1, 0, 4, 6, 0],
         [0, 0, 5, 0, 4, 0, 0, 3],
         [8, 0, 0, 0, 6, 0, 0, 3],
         [0, 7, 1, 0, 0, 3, 3, 0]]
# saved vertexes are stored in this array
# selected will become true otherwise false
selected_edges = [0, 0, 0, 0, 0, 0, 0, 0]
# at start, the number of edges is set to zero
edge_number = 0
# the number of edge in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in graph
# choose 0th vertex and make it true
selected_edges[0] = True
# print for edge and weight
print("Edge -> Weight\n")
while edge_number < V - 1:
    # For every vertex in the set S, find the all adjacent vertices
    # calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INFINITY
    # the indexes of printed elements
    # they are initialized as zero
    a = 0
    b = 0
    for i in range(V):
        if selected_edges[i]:
            for j in range(V):
                if (not selected_edges[j]) and graph[i][j]:
                    # not in selected and there is an edge
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        a = i
                        b = j
    # the output of selected edges and weights into console
    print(str(a) + " - " + str(b) + " -> " + str(graph[a][b]))
    selected_edges[b] = True
    edge_number += 1

