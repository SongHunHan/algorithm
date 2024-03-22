## 가장 가까운 사대 찾기 --> 정답보기 (이분탐색)

res = 0
m, n, l = map(int, input().split())
gun = sorted(list(map(int, input().split())))

def binary_search(target):
    start, end = 0, len(gun)-1

    while end>=start:
        middle = (start+end) // 2

        if gun[middle] == target:
            return middle
        elif gun[middle] < target:
            start = middle+1
        else:
            end = middle - 1
    return end

for i in range(n):
    x,y = map(int, input().split())
    gun_idx = binary_search(x)

    dist = abs(x- gun[gun_idx]) + y
    if gun_idx == m-1:
        dist_right = abs(x- gun[gun_idx-1]) + y
    else:
        dist_right = abs(x- gun[gun_idx+1]) + y

    dist = min(dist, dist_right)
    if l >= dist:
        res+=1
    
print(res)


    