import sys

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

print(graph)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

num = []
cnt = 0
result = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()
print(result)
for i in (num):
    print(i)