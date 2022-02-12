import sys

def dfs(v,group):
    visited[v] = group
    for adj in graph[v]:
        if visited[adj] == 0:
            dfs(adj, -group)

K = int(input())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for i in range(V+1)]
    for i in range(E):
        x, y =  map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    
    for i in range(1, V+1):
        if visited[i] == 0:
            dfs(i, 1)

    print("YES" if all(all(visited[i] == -visited[j] for j in graph[i]) for i in range(1, V+1)) else "NO")