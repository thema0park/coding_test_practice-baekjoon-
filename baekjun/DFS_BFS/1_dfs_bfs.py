import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for i in range(N+1)]

for value in range(M):
    peak_index_1, peak_index_2 = map(int, sys.stdin.readline().split())
    graph[peak_index_1][peak_index_2] = 1
    graph[peak_index_2][peak_index_1] = 1

def bfs(start_peak):
    discoverd = [start_peak]
    result = []
    result.append(start_peak)
    
    while result:
        v = result.pop(0)
        print(v, end=' ')

        for w in range(len(graph[start_peak])):
            if graph[v][w] == 1 and (w not in discoverd):
                discoverd.append(w)
                result.append(w)

def dfs(start_peak, discoverd = []):
    discoverd.append(start_peak)
    print(start_peak, end=' ')
    for w in range(len(graph[start_peak])):
        if graph[start_peak][w] == 1 and (w not in discoverd):
            dfs(w, discoverd)

if __name__ == "__main__":
    dfs(V)
    print()
    bfs(V)