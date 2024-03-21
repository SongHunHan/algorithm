from math import sqrt
n,m = map(int, input().split())
li = [list(input()) for i in range(n)]
res = -1

def check_sqrt(n):
    return int(sqrt(n)) ** 2 == n

for i in range(n):                          # 행 시작지점
    for j in range(m):                      # 열 시작지점
        for di in range(-n, n):             # 행 방향 증가량
            for dj in range(-m, m):         # 열 방향 증가량
                if di == 0 and dj == 0: 
                    continue
                num = ""
                ni, nj = i, j
                while 0 <= ni < n and 0 <= nj < m:
                    num += li[ni][nj]
                    if check_sqrt(int(num)):
                        res = max(res, int(num))
                    ni += di
                    nj += dj
print(res)
