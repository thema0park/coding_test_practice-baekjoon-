import sys

com_num = int(input())
connected_pair_num = int(input())
graph = [[0]*(com_num+1) for i in range(com_num+1)]
cnt = 0

for i in range(connected_pair_num):
    com_N, com_M = map(int, sys.stdin.readline().split())
    graph[com_N][com_M] = graph[com_M][com_N] = 1

def dfs(start_v, result=[]):
    result.append(start_v)
    global cnt
    #print(start_v, end=' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and w not in result:
            cnt += 1
            dfs(w,result)
            

if __name__ == "__main__":
    dfs(1)
    print(cnt)