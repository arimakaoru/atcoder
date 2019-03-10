# TLE
import sys

N, M = map(int, sys.stdin.readline().split())
AB = [None] * N
for i in range(N):
    AB[i] = list(map(int, sys.stdin.readline().split()))

AB.sort()
cnt = 0
ans = 0

for a,b in AB:
    if cnt + b < M:
        ans += a * b
        cnt += b
    else:
        ans += a * (M - cnt) 
        break

print(ans)