import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
calendar = [0 for i in range(366)]
res = 0

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x,y+1):
        calendar[i] += 1
    
width, height = 0,0
for i in range(1, 366):
    if calendar[i] == 0:
        res += (width * height)
        width = 0
        height = 0
    else:
        width += 1
        height = max(height, calendar[i])
print(res)