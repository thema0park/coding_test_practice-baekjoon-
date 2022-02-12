from collections import deque
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
maze = []
for i in range(N):
    maze.append(list(map(int, input())))

deq = deque()
visit = [[0]*M for i in range(N)]

def bfs(point):
    for i in range(4):
        nx = point[0] + dx[i]
        ny = point[1] + dy[i]

        if N > nx >= 0 and M > ny >= 0 and maze[nx][ny] and visit[nx][ny] == False:
            deq.append((nx, ny))
            visit[nx][ny] = True
            maze[nx][ny] += maze[point[0]][point[1]]

    if deq:
        bfs(deq.popleft())

bfs((0,0))
print(maze[N-1][M-1])