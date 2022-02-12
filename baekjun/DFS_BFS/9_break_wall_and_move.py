from collections import deque
import sys

def bfs():
    while point:
        start_point = point.popleft()
        x,y,z = start_point
        if x == N-1 and y == M-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][z] == 0: # and visited[nx][ny][z] == 0
                if graph[nx][ny] == 0:
                    point.append((nx,ny,z))
                    visited[nx][ny][z] = visited[x][y][z] + 1

                if z == 0 and graph[nx][ny] == 1:
                    # 딱 한 번만 벽 뿌수는게 가능
                    point.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][z] + 1
   
    return -1

N, M = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

point = deque() # x,y,break_flag
point.append((0,0,0))
visited[0][0][0] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

cnt = 0

print(bfs())