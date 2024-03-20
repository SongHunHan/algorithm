from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0 ,1, 1, 1, 0, -1, -1]

n,m = map(int,  input().split())
li = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for i in range(m)] for _ in range(n)]
cnt = 0

def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1
    
    while queue:
        x,y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if visited[nx][ny] == 0 and li[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append([nx,ny])

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and li[i][j] == 1:
            bfs(i,j)
            cnt+=1
print(cnt)