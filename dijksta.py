graph=[
    [0,7,9,0,0,4],
    [7,0,10,15,0,0],
    [9,10,0,11,0,2],
    [0,15,11,0,6,0],
    [0,0,0,6,0,9],
    [4,0,2,0,9,0]]

visited = [0] * 6 
d = [999] * 6
par = [-1] * 6

source = 0
d[source] = 0

def extract_min(d, visited):
    return min((d[i], i) for i in range(len(d)) if not visited[i])[1]
        
def relax(u, v, graph):
    if d[v] > graph[u][v] + d[u]:
        d[v] = graph[u][v] + d[u]
        par[v] = u

def Dijkstra(graph, visited, d):
    for i in range(len(d)):
        u = extract_min(d, visited)
        
        for v in range(len(d)):
            if (not visited[v] and graph[u][v]):
                relax(u, v, graph)
            visited[u] = 1


if __name__ == "__main__":
    Dijkstra(graph=graph, visited=visited, d=d)
    print(d, par)