import sys
sys.setrecursionlimit(10**6)

T = int(input())
graph = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0
result = []

def dfs(x, y):
    if x < 0 or x > M or y < 0 or y > N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

for i in range(T):
    M, N, K = list(map(int, sys.stdin.readline().split()))
    graph = [[0]*(N+1) for j in range(M+1)]
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for j in range(N):
        for k in range(M):
            if dfs(k, j) == True:
                cnt += 1
    print(cnt)
    cnt = 0