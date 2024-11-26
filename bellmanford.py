graph = [
    [0, 6, 5, 5, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0],
    [0, -2, 0, 0, 0, 0, 0],
    [0, 0, -2, 0, 0, -1, 0],
    [0, 0, 1, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0]
]

n = len(graph)
dist = [999] * (n)
par = [999]* (n)

source = 0
dist[source] = 0

def relax(u, v):
    if dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v]
        par[v] = u

def Bellman_ford():

    for _ in range(n - 1):
        for i in range(n):
            for j in range(n):
                if graph[i][j]:
                    relax(i, j)

    
    for i in range(n):
        for j in range(n):
            if graph[i][j] and dist[j] > dist[i] + graph[i][j]:
                return False
            
        
    return True


if not Bellman_ford():
    print("Graph contains negative weight cycle")

else:
    print("No negative weight cycle")

                