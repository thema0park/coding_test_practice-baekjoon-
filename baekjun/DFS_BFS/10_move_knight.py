import sys
from collections import deque
#sys.setrecursionlimit(10**6)

result = []
dx = [1,2,1,2,-1,-2,-1,-2]
dy = [2,1,-2,-1,2,1,-2,-1]

def bfs():
    while dq:
        point = dq.popleft()
        if point[0] == end_point_x and point[1] == end_point_y:
            return 0
        for i in range(len(dx)):
            nx = point[0] + dx[i]
            ny = point[1] + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                dq.append((nx, ny))
                graph[nx][ny] = graph[point[0]][point[1]] + 1
                if nx == end_point_x and ny == end_point_y:
                    return graph[nx][ny]-1

N = int(input())
for i in range(N):
    l = int(input())
    graph = [[0]*l for i in range(l)]
    start_point_x, start_point_y = map(int, input().split())
    end_point_x, end_point_y = map(int, input().split())
    graph[start_point_x][start_point_y] = 1
    dq = deque()
    dq.append((start_point_x, start_point_y))
    #result.append(dfs(start_point_x, start_point_y))
    result.append(bfs())


for res in result:
    print(res)


"""def dfs(x,y):
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < l and 0 <= ny < l:
            dq.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
            
            if nx == end_point_x and ny == end_point_y:
                print(graph[nx][ny]-1, nx, ny)
                return graph[nx][ny]-1"""