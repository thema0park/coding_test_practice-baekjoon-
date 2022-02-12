import sys
from collections import deque
sys.setrecursionlimit(10**6)

M, N = map(int, sys.stdin.readline().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

deq = deque()

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            deq.append([i,j])

def bfs():
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                deq.append([nx,ny])

bfs()

result = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = (max(result, max(i)))

print(result-1)