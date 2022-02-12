import sys
from collections import deque
sys.setrecursionlimit(10**6)

dx = [0,0, 0, 0, 1,-1]
dy = [0,0, 1,-1, 0, 0]
dz = [1,-1,0, 0, 0, 0]

M, N, H = map(int, sys.stdin.readline().split())
graph = [[] for i in range(H)]

start_point = deque()
for k in range(H):
    for i in range(N):
        graph[k].append(list(map(int, sys.stdin.readline().split())))
        for j in range(M):
            if graph[k][i][j] == 1:
                start_point.append([i,j,k])

def bfs():
    days = 0
    while start_point:
        point = start_point.popleft()
        for i in range(6):
            nx = point[0] + dx[i]
            ny = point[1] + dy[i]
            nz = point[2] + dz[i]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] += graph[point[2]][point[0]][point[1]] + 1
                start_point.append([nx,ny,nz])
        days = graph[point[2]][point[0]][point[1]] -1

    for i in graph:
        for j in i:
            for k in j:
                if k == 0:
                    return -1
    return days

result = bfs()
print(result)