# initializing the number of vertices
nV = 8
# initializing the infinity as an extremely large number
INF = 999


# function which implements the Floyd algorithm
def floyd_algorithm(source_graph):
    # initialisation of the minimal distances matrix
    distance = list(map(lambda i: list(map(lambda j: j, i)), source_graph))
    # adding vertices to the graph in a loop
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                # the matrix element is the sum of minimal distances between the required vertices
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    # printing the solution to the console
    # the solution is the matrix of minimal distances
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


# filling the adjacency matrix for the task graph
graph = [[0, 8, 2, 4, 3, INF, INF, INF],
         [8, 0, INF, INF, 6, 3, INF, INF],
         [2, INF, 0, INF, INF, 7, INF, 4],
         [4, INF, INF, 0, 1, INF, INF, INF],
         [3, 6, INF, 1, INF, 0, 4, INF],
         [INF, 3, 7, INF, INF, 0, 3, 1],
         [INF, INF, INF, INF, 4, 3, 0, 5],
         [INF, INF, 4, INF, INF, 1, 5, 0]]
print('The matrix of minimal distances:')
# calling the previously defined function for the Floyd algorithm
floyd_algorithm(graph)
